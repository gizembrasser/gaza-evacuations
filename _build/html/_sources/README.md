## Setup

### 1. Create a Virtual Environment (Recommended)
Using a virtual environment helps keep dependencies isolated.

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Required Dependencies
Make sure you have pip installed, then run:

```
pip install -r requirements.txt
```

## Fetch Displacement Data from Gaza Maps

The `gazamaps` command allows you to fetch the latest displacement zone data from the Gaza Maps API and save it as a CSV file. Each row in the file contains metadata about a displacement order, including:

- `id`: Unique identifier for the displacement order.
- `date`: Issue date of the displacement order.
- `source`: Source of the order (usually the [official IDF Twitter account](https://x.com/AvichayAdraee)).
- `link`: Link to the order's metadata on Gaza Maps.
- `map_idf`: Link to the map provided by the IDF.
- `map_full`: A readable version of the IDF's forced displacement order.
- `map_zoom`: A zoomed in readable version of the IDF's forced displacement order.
- `displacement_blocks`: Population blocks ordered to be displaced.
- `labeled_safe_blocks`: Population blocks designated "humanitarian area".
- `area_sq_km_displacement`: Area impacted for displacement.
- `area_sq_km_labeled_safe`: Area designated as "humanitarian area".

### Usage

Run the following command and choose a file name (e.g., `displacement25-07-2025.csv`):

```bash
python main.py gazamaps --output <file_name>
```

## Enrich Displacement Data with Extra Tweet Information

The `enrich` command will visit each IDF's tweet URL collected by Gaza Maps, and extract the tweet text and timestamp. These extra values will be added to the enriched data.

### Usage

Run the following command and choose your CSV file in the data folder (e.g., `displacement25-07-2025.csv`):

```bash
python main.py enrich --input <file_name>
```
