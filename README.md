# DataForSEO Skill for Claude Code

A [Claude Code skill](https://docs.anthropic.com/en/docs/claude-code/skills) that queries the [DataForSEO API](https://dataforseo.com/) for SEO data — SERP results, keyword research, backlink analysis, domain analytics, content analysis, AI optimization, and more.

Ported from DataForSEO's official [MCP server](https://github.com/dataforseo/mcp-server-typescript) (TypeScript) into a single Python script with zero external dependencies (stdlib only, Python 3.10+). Covers **9 modules** and **79 endpoints**.

## Install

```bash
git clone https://github.com/codykingham/dataforseo-skill.git
cd dataforseo-skill
./install.sh
```

This copies the skill into `~/.claude/skills/dataforseo/`. Claude Code will pick it up automatically on the next session.

## Setup

Set your DataForSEO API credentials as environment variables (e.g. in `~/.zshrc` or `~/.bashrc`):

```bash
export DATAFORSEO_USERNAME="your-login"
export DATAFORSEO_PASSWORD="your-api-password"
```

Optional environment variables:

| Variable | Default | Description |
|----------|---------|-------------|
| `DATAFORSEO_FULL_RESPONSE` | `false` | Return full API responses instead of AI-condensed |
| `DATAFORSEO_SIMPLE_FILTER` | `false` | Use simplified filter syntax |
| `FIELD_CONFIG_PATH` | — | Path to a custom field config JSON for response filtering |
| `DEBUG` | `false` | Enable debug logging to stderr |

## Usage

Once installed, just ask Claude about SEO topics in natural language:

> "What are the top-ranking pages for 'best coffee beans' in the US?"

> "Show me the backlink profile for example.com"

> "What's the search volume trend for 'ai agents' over the last 12 months?"

> "Find competitor domains for nytimes.com"

Claude will automatically invoke the skill, pick the right endpoint, and return the results.

## Available Modules

| Module | Endpoints | Description |
|--------|-----------|-------------|
| SERP | 7 | Google/Bing/Yahoo organic SERP results and YouTube search |
| Keywords Data | 6 | Google Ads search volume, Google Trends, DataForSEO Trends |
| Backlinks | 20 | Backlink profiles, anchors, referring domains, competitors |
| DataForSEO Labs | 21 | Keyword research, competitor analysis, domain rankings |
| OnPage | 3 | Content parsing, instant page audits, Lighthouse scores |
| AI Optimization | 13 | LLM mentions tracking, AI search data, ChatGPT scraping |
| Business Data | 2 | Business listings search and filters |
| Domain Analytics | 4 | WHOIS data, technology stack detection |
| Content Analysis | 3 | Citation search, content summaries, phrase trends |

See the [reference docs](dataforseo/references/) for detailed endpoint documentation.

## Development

Tests live at the repo root and don't get installed with the skill:

```bash
python -m pytest tests/ -v
```

## Repo Structure

```
dataforseo-skill/
├── dataforseo/           # Installable skill (copied to ~/.claude/skills/)
│   ├── SKILL.md          # Skill manifest with frontmatter
│   ├── scripts/
│   │   └── dataforseo.py # Single-file API client (stdlib only)
│   └── references/       # Endpoint documentation (10 files)
├── tests/                # Test suite (67 tests)
├── install.sh            # One-command installer
└── README.md
```

## License

MIT
