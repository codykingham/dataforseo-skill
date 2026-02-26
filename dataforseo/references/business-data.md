# Business Data API Reference

Tools for searching business listings on Google Maps, including filters for refining results by rating, category, location, and more.

---

### business_data_business_listings_filters
**Description**: Here you will find all the necessary information about filters that can be used with Business Data API business listings endpoints. Please, keep in mind that filters are associated with a certain object in the result array, and should be specified accordingly.
**Endpoint**: `GET /v3/business_data/business_listings/available_filters`
**AI-condensed**: No (supportOnlyFullResponse -- use `--full-response`)

#### Parameters
| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| tool | string | No | -- | The name of the tool to get filters for. If omitted, returns filters for all tools. Valid values: `business_data_business_listings_search`, `business_data_business_listings_categories_aggregation` |

#### Example
```bash
echo '{}' | python3 $SKILL_DIR/scripts/dataforseo.py \
  --endpoint /v3/business_data/business_listings/available_filters \
  --method GET --full-response
```

```bash
echo '{"tool":"business_data_business_listings_search"}' | python3 $SKILL_DIR/scripts/dataforseo.py \
  --endpoint /v3/business_data/business_listings/available_filters \
  --method GET --full-response
```

---

### business_data_business_listings_search
**Description**: Business Listings Search API provides results containing information about business entities listed on Google Maps in the specified categories. You will receive the address, contacts, rating, working hours, and other relevant data
**Endpoint**: `POST /v3/business_data/business_listings/search/live`
**AI-condensed**: Yes

#### Parameters
| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| description | string | No | -- | Description of the business entity. Up to 200 characters |
| title | string | No | -- | Name of the business entity. Up to 200 characters |
| categories | string[] | No | -- | Business categories to search for. Up to 10 categories |
| location_coordinate | string | No | -- | GPS coordinates in `"latitude,longitude,radius"` format. Radius in km (min 1, max 100000). Example: `"53.476225,-2.243572,200"` |
| limit | number | No | 10 | Max number of returned businesses. Min 1, max 1000 |
| offset | number | No | 0 | Offset in the results array. Use for pagination |
| filters | array | No | -- | Filter array (max 8 filters). Use `business_data_business_listings_filters` to see available fields. See `$SKILL_DIR/references/filters-and-sorting.md` |
| order_by | string[] | No | -- | Sorting rules (max 3). Format: `["field,desc"]`. Example: `["rating.value,desc","rating.votes_count,desc"]` |
| is_claimed | boolean | No | true | Whether the business is verified by its owner on Google Maps |

#### Example
```bash
echo '{"categories":["restaurant"],"location_coordinate":"40.7128,-74.0060,10","limit":10,"is_claimed":true}' | \
  python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/business_data/business_listings/search/live
```

```bash
echo '{"title":"pizza","location_coordinate":"40.7128,-74.0060,5","filters":["rating.value",">",4],"order_by":["rating.value,desc"],"limit":20}' | \
  python3 $SKILL_DIR/scripts/dataforseo.py --endpoint /v3/business_data/business_listings/search/live
```
