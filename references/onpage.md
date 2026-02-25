# OnPage API Reference

The OnPage module provides tools for analyzing individual web pages. It supports content parsing (extracting structured content from any URL), instant page analysis (SEO optimization data), and Lighthouse audits (Google's open-source page quality measurement).

## Table of Contents

- [on_page_content_parsing](#on_page_content_parsing)
- [on_page_instant_pages](#on_page_instant_pages)
- [on_page_lighthouse](#on_page_lighthouse)
- [Suggested Workflows](#suggested-workflows)

---

### on_page_content_parsing

**Description**: This endpoint allows parsing the content on any page you specify and will return the structured content of the target page, including link URLs, anchors, headings, and textual content.
**Endpoint**: `POST /v3/on_page/content_parsing/live`
**AI-condensed**: Yes

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| url | string | Yes | - | URL of the page to parse |
| enable_javascript | boolean | No | - | Enable JavaScript rendering |
| custom_user_agent | string | No | - | Custom User-Agent header |
| accept_language | string | No | - | Accept-Language header value |

> Note: The API request always includes `markdown_view: true`, so the response will contain a markdown representation of the page content.

#### Example

```bash
echo '{"url": "https://example.com/blog/article"}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/on_page/content_parsing/live
```

---

### on_page_instant_pages

**Description**: Using this function you will get page-specific data with detailed information on how well a particular page is optimized for organic search.
**Endpoint**: `POST /v3/on_page/instant_pages`
**AI-condensed**: Yes

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| url | string | Yes | - | URL to analyze |
| enable_javascript | boolean | No | - | Enable JavaScript rendering |
| custom_js | string | No | - | Custom JavaScript code to execute |
| custom_user_agent | string | No | - | Custom User-Agent header |
| accept_language | string | No | - | Language header for accessing the website. All locale formats are supported (xx, xx-XX, xxx-XX, etc.). Note: if you do not specify this parameter, some websites may deny access; in this case, pages will be returned with "type":"broken" in the response array. |

#### Example

```bash
echo '{"url": "https://example.com", "enable_javascript": true, "accept_language": "en-US"}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/on_page/instant_pages
```

---

### on_page_lighthouse

**Description**: The OnPage Lighthouse API is based on Google's open-source Lighthouse project for measuring the quality of web pages and web apps.
**Endpoint**: `POST /v3/on_page/lighthouse/live/json`
**AI-condensed**: Yes

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| url | string | Yes | - | URL of the page to parse |
| enable_javascript | boolean | No | - | Enable JavaScript rendering |
| custom_user_agent | string | No | - | Custom User-Agent header |
| accept_language | string | No | - | Accept-Language header value |
| result | enum | No | - | Specify which Lighthouse result property to return. One of: `audits`, `configSettings`, `categories`, `categoryGroups`, `timing`, `i18n`, `stackPacks`. When specified, only the selected property is included in the response (other Lighthouse result properties are removed). |

#### Example

```bash
echo '{"url": "https://example.com", "result": "categories"}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/on_page/lighthouse/live/json
```

---

## Suggested Workflows

### 1. Identify Technical Performance Issues Affecting Crawlability and Ranking

Audit a page for crawlability issues, including robots.txt restrictions, noindex tags, and broken internal links.

1. **Analyze the page with instant pages** using `on_page_instant_pages`:
   ```bash
   echo '{"url": "https://example.com/page", "enable_javascript": true, "accept_language": "en-US"}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/on_page/instant_pages
   ```

2. **Review results**: Check for robots.txt restrictions, noindex tags, and broken internal links. Highlight what is preventing Google from indexing or ranking the page.

### 2. Detect Missing or Duplicate Meta Tags Hurting SEO

Review a page for missing or duplicate meta title and meta description tags.

1. **Parse the page content** using `on_page_content_parsing`:
   ```bash
   echo '{"url": "https://example.com/page", "enable_javascript": true}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/on_page/content_parsing/live
   ```

2. **Analyze the page for SEO signals** using `on_page_instant_pages`:
   ```bash
   echo '{"url": "https://example.com/page", "enable_javascript": true, "accept_language": "en-US"}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/on_page/instant_pages
   ```

3. **Review results**: Check if meta title and meta description tags are too long, too short, missing, or duplicated, and recommend fixes.

### 3. Check for Slow Load Time and Mobile Compatibility Issues

Analyze a page for speed and mobile usability.

1. **Run a Lighthouse audit** using `on_page_lighthouse`:
   ```bash
   echo '{"url": "https://example.com/page", "result": "audits"}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/on_page/lighthouse/live/json
   ```

2. **Get Lighthouse categories overview** using `on_page_lighthouse`:
   ```bash
   echo '{"url": "https://example.com/page", "result": "categories"}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/on_page/lighthouse/live/json
   ```

3. **Analyze with instant pages** using `on_page_instant_pages`:
   ```bash
   echo '{"url": "https://example.com/page", "enable_javascript": true, "accept_language": "en-US"}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/on_page/instant_pages
   ```

4. **Review results**: Identify what is slowing the page down or making it hard to use on mobile. Include measurements and give practical steps to improve performance.

### 4. Evaluate Internal Linking and Crawl Depth for Better Indexing

Check how well a page is connected internally and whether it is buried too deep in the site structure.

1. **Analyze the page** using `on_page_instant_pages`:
   ```bash
   echo '{"url": "https://example.com/page", "enable_javascript": true, "accept_language": "en-US"}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/on_page/instant_pages
   ```

2. **Parse the content for link structure** using `on_page_content_parsing`:
   ```bash
   echo '{"url": "https://example.com/page", "enable_javascript": true}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/on_page/content_parsing/live
   ```

3. **Review results**: Determine if the page lacks internal links that could help search engines find and rank it. Include data for each issue or metric.

### 5. Analyze Keyword Optimization and Content Gaps

Evaluate how well a page is optimized for a target keyword.

1. **Parse the page content** using `on_page_content_parsing`:
   ```bash
   echo '{"url": "https://example.com/page", "enable_javascript": true}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/on_page/content_parsing/live
   ```

2. **Analyze SEO optimization** using `on_page_instant_pages`:
   ```bash
   echo '{"url": "https://example.com/page", "enable_javascript": true, "accept_language": "en-US"}' | python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/on_page/instant_pages
   ```

3. **Review results**: Analyze on-page SEO elements like title, meta description, headings (H1-H6), internal links, and keyword usage. Extract and parse all content elements (headings, paragraphs, alt attributes, etc.) and check for keyword placement and semantic relevance. Identify missing keyword placements and content gaps that could affect relevance and ranking.
