# Algolia Search Integration for cmap

This directory contains tools for integrating the cmap colormap catalog with Algolia search.

## Upload to Algolia

The `upload_to_algolia.py` script extracts all colormaps from the cmap catalog and uploads them to Algolia, making them searchable through the Algolia search engine.

### Prerequisites

- Python 3.8+
- Algolia account with API access
- Required Python packages:
  - `algoliasearch`
  - `cmap` (this package)
  - `numpy`

```bash
pip install algoliasearch
```

### Usage

```bash
# Basic usage with credentials provided as arguments
./upload_to_algolia.py --app-id YOUR_APP_ID --api-key YOUR_API_KEY

# Using environment variables for credentials
export ALGOLIA_APP_ID=YOUR_APP_ID
export ALGOLIA_API_KEY=YOUR_API_KEY
./upload_to_algolia.py

# Recreate the index from scratch
./upload_to_algolia.py --recreate-index

# Dry run (preview records without uploading)
./upload_to_algolia.py --dry-run

# Specify a custom index name
./upload_to_algolia.py --index-name custom_index_name

# Change the URL prefix for colormap preview links
./upload_to_algolia.py --prefix-url https://example.com/colormaps/
```

### Options

- `--app-id`: Algolia Application ID (can also be set via `ALGOLIA_APP_ID` env variable)
- `--api-key`: Algolia API Key (can also be set via `ALGOLIA_API_KEY` env variable)
- `--index-name`: Algolia index name (default: `cmap_catalog`)
- `--prefix-url`: URL prefix for colormap preview links (default: `https://cmap.readthedocs.io/en/latest/catalog/`)
- `--recreate-index`: Recreate the Algolia index from scratch (if not specified, records will be updated)
- `--dry-run`: Print records that would be uploaded but don't actually upload

### What is uploaded

Each colormap is uploaded to Algolia with the following attributes:

- `objectID`: The qualified name of the colormap (e.g., "matplotlib:viridis")
- `name`: The short name of the colormap (e.g., "viridis")
- `qualified_name`: The fully qualified name (e.g., "matplotlib:viridis")
- `namespace`: The namespace of the colormap (e.g., "matplotlib")
- `category`: The category of the colormap (e.g., "sequential", "diverging", "cyclic", etc.)
- `interpolation`: The interpolation method for the colormap
- `tags`: Any tags associated with the colormap
- `authors`: List of authors
- `license`: License information
- `source`: Source of the colormap
- `info`: Description of the colormap
- `aliases`: List of aliases for the colormap
- `color_samples`: Array of hex color samples representing the colormap
- `url`: URL to the colormap in the documentation
- `has_name_conflict`: Whether the short name is ambiguous (exists in multiple namespaces)

### Index Configuration

When `--recreate-index` is used, the index is configured with the following settings:

- **Searchable Attributes** (in order of priority):
  - name
  - qualified_name
  - namespace
  - tags
  - category
  - info
  - authors

- **Facet Attributes** (for filtering):
  - namespace
  - category
  - tags
  - license
  - interpolation
  - authors

- **Custom Ranking**:
  - Sort by category (descending)
  - Then alphabetically by name (ascending)
