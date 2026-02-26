#!/usr/bin/env python3
"""DataForSEO API client script.

A single-file Python 3.10+ stdlib-only client for the DataForSEO API.
Ported from the TypeScript MCP server implementation.

Usage:
    echo '{"keyword": "seo"}' | python3 scripts/dataforseo.py \\
        --endpoint /v3/serp/google/organic/live/advanced

    python3 scripts/dataforseo.py \\
        --endpoint /v3/keywords_data/google_trends/categories/live \\
        --method GET

    echo '{"target": "example.com"}' | python3 scripts/dataforseo.py \\
        --endpoint /v3/backlinks/summary/live \\
        --fields "items.*.backlinks,items.*.rank"
"""

import argparse
import base64
import json
import os
import sys
import urllib.error
import urllib.request

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

BASE_URL = "https://api.dataforseo.com"

# ---------------------------------------------------------------------------
# Utility: map_array_to_numbered_keys
# ---------------------------------------------------------------------------


def map_array_to_numbered_keys(arr: list) -> dict:
    """Convert a list to a dict with 1-based string keys.

    Example:
        ['a', 'b'] -> {'1': 'a', '2': 'b'}
    """
    return {str(i + 1): val for i, val in enumerate(arr)}


# ---------------------------------------------------------------------------
# Filter normalization: remove_nested
# ---------------------------------------------------------------------------


def remove_nested(filters):
    """Recursively unwrap singly-nested arrays in filter expressions.

    Matches the TypeScript ``removeNested`` method exactly: for each element
    in the array, if the element is an array of length 1 whose sole item is
    also an array, replace it with the recursively-unwrapped inner array.

    Returns *None* unchanged if *filters* is ``None``.
    """
    if filters is None:
        return None
    if not isinstance(filters, list):
        return filters
    if len(filters) == 0:
        return filters

    for i in range(len(filters)):
        if (
            isinstance(filters[i], list)
            and len(filters[i]) == 1
            and isinstance(filters[i][0], list)
        ):
            filters[i] = remove_nested(filters[i][0])

    return filters


# ---------------------------------------------------------------------------
# Field filtering (dot-notation with wildcard support)
# ---------------------------------------------------------------------------


def _parse_field_paths(fields: list[str]) -> list:
    """Parse field path strings into path lists.

    Handles array bracket notation: ``items[0]`` -> ``['items', '0']``
    """
    result = []
    for field in fields:
        if "[" in field:
            base, index = field.split("[", 1)
            result.append([base, index.rstrip("]")])
        else:
            result.append(field)
    return result


def _extract_and_set_value(source, target: dict, path: list[str]) -> None:
    """Recursively extract a value from *source* along *path* and set it in *target*."""
    if not path:
        return

    current_key, *remaining_path = path

    if not remaining_path:
        # Final key
        if current_key == "*":
            if isinstance(source, list):
                target.update({str(i): v for i, v in enumerate(source)})
            elif isinstance(source, dict):
                target.update(source)
        elif isinstance(source, dict) and current_key in source:
            target[current_key] = source[current_key]
        return

    # Not final key -- go deeper
    if current_key == "*":
        # Wildcard in the middle
        if isinstance(source, list):
            # Source is an array -- iterate each element
            for idx, item in enumerate(source):
                if isinstance(target, list):
                    while len(target) <= idx:
                        target.append({})
                    if not isinstance(target[idx], dict):
                        target[idx] = {}
                    _extract_and_set_value(item, target[idx], remaining_path)
                else:
                    # target is a dict -- store by string index
                    key = str(idx)
                    if key not in target:
                        target[key] = {}
                    _extract_and_set_value(item, target[key], remaining_path)
        elif isinstance(source, dict):
            # Source is an object -- iterate its keys
            for key in source:
                if key not in target:
                    target[key] = {}
                _extract_and_set_value(source[key], target[key], remaining_path)
    elif isinstance(source, dict) and current_key in source:
        source_value = source[current_key]
        if isinstance(source_value, list):
            if current_key not in target:
                target[current_key] = []
            # If next path element is '*', consume it and fan out
            effective_remaining = remaining_path
            if remaining_path and remaining_path[0] == "*":
                effective_remaining = remaining_path[1:]
            for idx, item in enumerate(source_value):
                while len(target[current_key]) <= idx:
                    target[current_key].append({})
                if effective_remaining:
                    if not isinstance(target[current_key][idx], dict):
                        target[current_key][idx] = {}
                    _extract_and_set_value(item, target[current_key][idx], effective_remaining)
                else:
                    # Wildcard at end with array -- copy all items
                    target[current_key][idx] = item
        elif isinstance(source_value, dict):
            if current_key not in target:
                target[current_key] = {}
            _extract_and_set_value(source_value, target[current_key], remaining_path)


def filter_fields(data, field_spec: str):
    """Filter *data* to include only the fields described by *field_spec*.

    *field_spec* is a comma-separated string of dot-notation paths with
    optional ``*`` wildcards.  Returns a new dict with only the matched
    fields, or the original *data* if *field_spec* is empty/None.
    """
    if data is None:
        return None
    if not field_spec:
        return data

    fields = [f.strip() for f in field_spec.split(",") if f.strip()]
    if not fields:
        return data

    parsed = _parse_field_paths(fields)
    result: dict = {}

    for field in parsed:
        path = field if isinstance(field, list) else field.split(".")
        _extract_and_set_value(data, result, path)

    return result


# ---------------------------------------------------------------------------
# Field configuration (singleton-like helpers)
# ---------------------------------------------------------------------------

_field_config_cache: dict | None = None


def load_field_config(path: str) -> dict | None:
    """Load field configuration from a JSON file.

    Returns ``None`` if the file does not exist or has invalid format.
    """
    global _field_config_cache

    if not os.path.isfile(path):
        _debug_log(f"Field config file not found: {path}")
        return None

    try:
        with open(path, "r", encoding="utf-8") as fh:
            parsed = json.load(fh)

        if (
            not isinstance(parsed, dict)
            or "supported_fields" not in parsed
            or not isinstance(parsed["supported_fields"], dict)
        ):
            _debug_log(f"Invalid field config format in {path}")
            return None

        _field_config_cache = parsed
        return parsed
    except (json.JSONDecodeError, OSError) as exc:
        _debug_log(f"Error loading field config: {exc}")
        return None


def query_field_config(config: dict, tool_name: str) -> list[str] | None:
    """Return the field list for *tool_name* from *config*, or ``None``."""
    if not config or "supported_fields" not in config:
        return None
    return config["supported_fields"].get(tool_name)


def clear_field_config():
    """Clear the cached field configuration.  Returns ``None``."""
    global _field_config_cache
    _field_config_cache = None
    return None


# ---------------------------------------------------------------------------
# URL building
# ---------------------------------------------------------------------------


def build_url(endpoint: str, full_response: bool = False, force_full: bool = False) -> str:
    """Construct the full DataForSEO API URL.

    Appends ``.ai`` to the endpoint when *full_response* is False **and**
    *force_full* is False.
    """
    url = f"{BASE_URL}{endpoint}"
    if not full_response and not force_full:
        url += ".ai"
    return url


# ---------------------------------------------------------------------------
# Auth header
# ---------------------------------------------------------------------------


def build_auth_header(username: str, password: str) -> str:
    """Build a Basic-Auth ``Authorization`` header value."""
    token = base64.b64encode(f"{username}:{password}".encode()).decode()
    return f"Basic {token}"


# ---------------------------------------------------------------------------
# Response validation
# ---------------------------------------------------------------------------


def validate_ai_response(response: dict) -> bool:
    """Validate an AI-condensed response.

    The ``status_code`` field (e.g. 20000) is divided by 100; the quotient
    must equal exactly 200.  This matches the TypeScript implementation which
    checks ``status_code / 100 !== 200``.
    """
    code = response.get("status_code", 0)
    if code / 100 != 200:
        msg = response.get("status_message", "Unknown error")
        raise ValueError(f"API Error: {msg} (Code: {code})")
    return True


def validate_full_response(response: dict) -> bool:
    """Validate a full DataForSEO response.

    Checks (matching TypeScript ``validateResponseFull``):
    1. Outer ``status_code / 100 === 200``
    2. ``tasks`` list is non-empty
    3. First task ``status_code / 100 === 200``
    4. ``tasks_error`` count is 0
    """
    # 1. Outer status
    outer_code = response.get("status_code", 0)
    if outer_code / 100 != 200:
        msg = response.get("status_message", "Unknown error")
        raise ValueError(f"API Error: {msg} (Code: {outer_code})")

    # 2. Tasks non-empty
    tasks = response.get("tasks", [])
    if not tasks:
        raise ValueError("No tasks in response")

    # 3. First task status
    task = tasks[0]
    task_code = task.get("status_code", 0)
    if task_code / 100 != 200:
        msg = task.get("status_message", "Unknown error")
        raise ValueError(f"Task Error: {msg} (Code: {task_code})")

    # 4. tasks_error count
    tasks_error = response.get("tasks_error", 0)
    if tasks_error > 0:
        raise ValueError(f"Tasks Error: {tasks_error} tasks failed")

    return True


# ---------------------------------------------------------------------------
# Configuration from env
# ---------------------------------------------------------------------------


def _parse_bool_env(name: str, default: bool = False) -> bool:
    """Parse a boolean-ish environment variable."""
    val = os.environ.get(name, "")
    if val.lower() in ("true", "1"):
        return True
    if val.lower() in ("false", "0"):
        return False
    return default


def get_config() -> dict:
    """Build a config dict from environment variables."""
    return {
        "username": os.environ.get("DATAFORSEO_USERNAME", ""),
        "password": os.environ.get("DATAFORSEO_PASSWORD", ""),
        "full_response": _parse_bool_env("DATAFORSEO_FULL_RESPONSE"),
        "simple_filter": _parse_bool_env("DATAFORSEO_SIMPLE_FILTER"),
        "debug": _parse_bool_env("DEBUG"),
    }


# ---------------------------------------------------------------------------
# Debug logging
# ---------------------------------------------------------------------------


def _debug_log(*args, **kwargs):
    """Print debug info to stderr."""
    print(*args, file=sys.stderr, **kwargs)


# ---------------------------------------------------------------------------
# HTTP request
# ---------------------------------------------------------------------------


def make_request(
    endpoint: str,
    method: str = "POST",
    body=None,
    full_response: bool = False,
    force_full: bool = False,
    username: str = "",
    password: str = "",
    wrap_array: bool = True,
    debug: bool = False,
) -> dict:
    """Execute an HTTP request against the DataForSEO API.

    Returns a dict with ``{"status": "ok", "result": ...}`` on success
    or ``{"status": "error", "message": ...}`` on failure.
    """
    url = build_url(endpoint, full_response=full_response, force_full=force_full)
    auth = build_auth_header(username, password)

    headers = {
        "Authorization": auth,
        "Content-Type": "application/json",
    }

    data_bytes = None
    if body is not None and method.upper() == "POST":
        payload = body
        if wrap_array and isinstance(payload, dict):
            payload = [payload]
        data_bytes = json.dumps(payload).encode("utf-8")

    if debug:
        _debug_log(f"Request: {method} {url}")
        if data_bytes:
            _debug_log(f"Body: {data_bytes.decode()}")

    req = urllib.request.Request(
        url,
        data=data_bytes,
        headers=headers,
        method=method.upper(),
    )

    try:
        with urllib.request.urlopen(req) as resp:
            raw = resp.read()
            response_data = json.loads(raw)

        # Validate
        if full_response or force_full:
            validate_full_response(response_data)
            result = response_data["tasks"][0]["result"]
        else:
            validate_ai_response(response_data)
            result = response_data

        return {"status": "ok", "result": result}

    except urllib.error.HTTPError as exc:
        msg = f"HTTP {exc.code}: {exc.reason}"
        if debug:
            _debug_log(msg)
        return {"status": "error", "message": msg}
    except urllib.error.URLError as exc:
        msg = str(exc.reason)
        if debug:
            _debug_log(msg)
        return {"status": "error", "message": msg}
    except (ValueError, json.JSONDecodeError) as exc:
        return {"status": "error", "message": str(exc)}
    except Exception as exc:
        return {"status": "error", "message": str(exc)}


# ---------------------------------------------------------------------------
# CLI main
# ---------------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(
        description="DataForSEO API client",
    )
    parser.add_argument(
        "--endpoint",
        required=True,
        help="API endpoint path, e.g. /v3/serp/google/organic/live/advanced",
    )
    parser.add_argument(
        "--method",
        default="POST",
        choices=["GET", "POST"],
        help="HTTP method (default: POST)",
    )
    parser.add_argument(
        "--full-response",
        action="store_true",
        default=None,
        help="Force full response mode (skip .ai suffix)",
    )
    parser.add_argument(
        "--fields",
        default=None,
        help="Comma-separated field filter (dot-notation, supports wildcards)",
    )
    parser.add_argument(
        "--field-config",
        default=None,
        help="Path to field configuration JSON file",
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        default=None,
        help="Enable debug output to stderr",
    )
    parser.add_argument(
        "--no-wrap-array",
        action="store_true",
        help="Don't auto-wrap POST body in [{...}]",
    )

    args = parser.parse_args()

    # Merge env config with CLI flags
    config = get_config()
    debug = args.debug if args.debug is not None else config["debug"]
    full_response = args.full_response if args.full_response is not None else config["full_response"]

    username = config["username"]
    password = config["password"]

    if not username or not password:
        output = {"status": "error", "message": "DATAFORSEO_USERNAME and DATAFORSEO_PASSWORD must be set"}
        print(json.dumps(output))
        sys.exit(1)

    # Read body from stdin for POST
    body = None
    if args.method == "POST" and not sys.stdin.isatty():
        raw_input = sys.stdin.read().strip()
        if raw_input:
            try:
                body = json.loads(raw_input)
            except json.JSONDecodeError as exc:
                output = {"status": "error", "message": f"Invalid JSON input: {exc}"}
                print(json.dumps(output))
                sys.exit(1)

    # Load field config if specified
    field_config = None
    config_path = args.field_config or os.environ.get("FIELD_CONFIG_PATH")
    if config_path:
        field_config = load_field_config(config_path)

    # Make the request
    result = make_request(
        endpoint=args.endpoint,
        method=args.method,
        body=body,
        full_response=full_response,
        force_full=args.full_response or False,
        username=username,
        password=password,
        wrap_array=not args.no_wrap_array,
        debug=debug,
    )

    # Apply field filtering
    if result["status"] == "ok" and args.fields:
        result["result"] = filter_fields(result["result"], args.fields)

    # Output
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
