#!/usr/bin/env python
"""
Upload colormap catalog to Algolia.

This script extracts all colormaps from the cmap catalog and uploads them to Algolia,
making them searchable through the Algolia search engine.
"""

import argparse
import base64
import logging
import os
import sys
from typing import Any

from algoliasearch.search.client import SearchClientSync

import cmap

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("cmap_algolia")


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Upload colormap catalog to Algolia.")
    parser.add_argument(
        "--app-id",
        help="Algolia Application ID. Can also be set via ALGOLIA_APP_ID env variable.",
    )
    parser.add_argument(
        "--api-key",
        help="Algolia API Key. Can also be set via ALGOLIA_API_KEY env variable.",
    )
    parser.add_argument(
        "--index-name",
        default="cmap_catalog",
        help="Algolia index name. Default: cmap_catalog",
    )
    parser.add_argument(
        "--prefix-url",
        default="https://cmap-docs.rtfd.io/en/latest/catalog/",
        help="URL prefix for colormap preview links. Default: https://cmap-docs.rtfd.io/en/latest/catalog/",
    )
    parser.add_argument(
        "--recreate-index",
        action="store_true",
        help="Recreate the Algolia index from scratch. If not specified, records will be updated.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print records that would be uploaded but don't actually upload.",
    )
    return parser.parse_args()


def get_algolia_credentials(args: argparse.Namespace) -> tuple[str, str]:
    """Get Algolia credentials from args or environment variables."""
    app_id = args.app_id or os.environ.get("ALGOLIA_APP_ID")
    api_key = args.api_key or os.environ.get("ALGOLIA_API_KEY")

    if not app_id or not api_key:
        logger.error(
            "Algolia credentials not provided. Use --app-id and --api-key arguments "
            "or set ALGOLIA_APP_ID and ALGOLIA_API_KEY environment variables."
        )
        sys.exit(1)

    return app_id, api_key


def colormap_to_dict(cm_item: cmap.CatalogItem, prefix_url: str) -> dict[str, Any]:
    """Convert a CatalogItem to a dictionary for Algolia."""
    # Generate a simplified RGB representation for the colormap
    # This can be used to create a preview image or to display the colormap in search results
    try:
        cm = cmap.Colormap(cm_item.qualified_name)
        # Sample the colormap at 10 evenly spaced points
        samples = 10
        # Create color samples manually

        # # Convert RGB values (0-1) to hex color codes
        # rgb_values = cm(np.linspace(0, 1, samples))
        # color_samples = [
        #     f"#{int(r * 255):02x}{int(g * 255):02x}{int(b * 255):02x}"
        #     for r, g, b, *_ in rgb_values
        # ]

        # Generate a base64 encoded PNG image of the colormap
        # Using small dimensions to keep the file size small
        png_data = cm._repr_png_(width=256, height=1)
        image_base64 = base64.b64encode(png_data).decode("ascii")
    except Exception as e:
        logger.warning(
            f"Could not generate color samples for {cm_item.qualified_name}: {e}"
        )
        # color_samples = []
        image_base64 = ""

    # Determine if this has a short name conflict
    # (i.e. if the short name would be ambiguous)
    short_name = cm_item.name
    has_name_conflict = False

    catalog = cmap.Catalog()
    try:
        resolved = catalog.resolve(short_name)
        has_name_conflict = resolved != cm_item.qualified_name
    except KeyError:
        pass

    # Create dictionary for Algolia
    return {
        "objectID": cm_item.qualified_name,
        "name": cm_item.name,
        "namespace": cm_item.namespace,
        "category": cm_item.category,
        "interpolation": cm_item.interpolation,
        "tags": cm_item.tags,
        "authors": cm_item.authors,
        "license": cm_item.license,
        "source": cm_item.source,
        "info": cm_item.info,
        "aliases": cm_item.aliases,
        # "color_samples": color_samples,
        # https://cmap-docs.rtfd.io/en/latest/catalog/sequential/bids:magma/
        "url": f"{prefix_url}/{cm_item.category}/{cm_item.qualified_name}/",
        "has_name_conflict": has_name_conflict,
        "image_base64": image_base64 if "image_base64" in locals() else "",
    }


def upload_to_algolia(
    records: list[dict[str, Any]],
    app_id: str,
    api_key: str,
    index_name: str,
    recreate_index: bool = False,
    dry_run: bool = False,
) -> None:
    """Upload records to Algolia."""
    if dry_run:
        logger.info(f"Dry run mode. Would upload {len(records)} records:")
        for record in records[:2]:  # Print only the first two as an example
            logger.info(record)
        if len(records) > 2:
            logger.info(f"... and {len(records) - 2} more records")
        return

    # Initialize Algolia client
    client = SearchClientSync(app_id, api_key)

    # Configure index settings if recreating
    if recreate_index:
        logger.info(f"Recreating index {index_name}")
        client.clear_objects(index_name=index_name)

        # Configure index settings for colormap search
        client.set_settings(
            index_name=index_name,
            index_settings={
                "searchableAttributes": [
                    "name",
                    "qualified_name",
                    "namespace",
                    "tags",
                    "category",
                    "info",
                    "authors",
                ],
                "attributesForFaceting": [
                    "searchable(namespace)",
                    "category",
                    "tags",
                    "license",
                    "interpolation",
                    "authors",
                ],
                "customRanking": [
                    "desc(category)",  # Sort by category
                    "asc(name)",  # Then alphabetically by name
                ],
            },
        )

    # Upload records
    logger.info(f"Uploading {len(records)} records to Algolia index '{index_name}'")
    results = client.save_objects(index_name=index_name, objects=records)
    obj_ids = [result.object_ids[:5] for result in results[:5]]
    logger.info(f"Upload complete. Object IDs: {obj_ids}...")


def main() -> None:
    """Main entry point."""
    args = parse_args()
    app_id, api_key = get_algolia_credentials(args)

    # Load the colormap catalog
    logger.info("Loading colormap catalog")
    catalog = cmap.Catalog()

    # Get unique keys that refer to actual colormaps (not aliases)
    # We use prefer_short_names=False to ensure we get the fully qualified names
    unique_keys = catalog.unique_keys(prefer_short_names=False)
    logger.info(f"Found {len(unique_keys)} unique colormaps")

    # Convert each colormap to a record for Algolia
    records = []
    for key in unique_keys:
        try:
            cm_item = catalog[key]
            record = colormap_to_dict(cm_item, args.prefix_url)
            records.append(record)
        except Exception as e:
            logger.error(f"Error processing colormap {key}: {e}")

    logger.info(f"Prepared {len(records)} records for Algolia")

    # Upload to Algolia
    upload_to_algolia(
        records=records,
        app_id=app_id,
        api_key=api_key,
        index_name=args.index_name,
        recreate_index=args.recreate_index,
        dry_run=args.dry_run,
    )


if __name__ == "__main__":
    main()
