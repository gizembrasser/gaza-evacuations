import asyncio
import argparse
import pandas as pd
from utils.x_scraper import enrich
from utils.gazamaps_api import fetch_displacement_data
import os

csv_folder = os.path.join(os.getcwd(), 'data', 'csv')
if not os.path.exists(csv_folder):
    os.makedirs(csv_folder)


def main():
    parser = argparse.ArgumentParser(description="Collect displacement data from Gaza Maps API and enrich with corresponding IDF tweet info.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Subcommand to fetch displacement data from Gaza Maps API
    gazamaps_parser = subparsers.add_parser("gazamaps", help="Fetch displacement data from Gaza Maps API")
    gazamaps_parser.add_argument(
        "--output",
        type=str,
        required=True,
        help="Output path for the CSV file (e.g., displacement25-07-2025.csv)"
    )

    # Subcommand to enrich the displacement data with tweet information
    enrich_parser = subparsers.add_parser("enrich", help="Enrich the displacement data from Gaza Maps with corresponding IDF tweet info.")
    enrich_parser.add_argument(
        "--input",
        type=str,
        required=True,
        help="Input path for the CSV file to enrich (e.g., displacement25-07-2025.csv)"
    )

    args = parser.parse_args()

    if args.command == "gazamaps":
        output_path = os.path.join(csv_folder, args.output)
        fetch_displacement_data(save_path=output_path)
    
    if args.command == "enrich":
        input_path = os.path.join(csv_folder, args.input)
         # Load original CSV and run enrichment
        df = pd.read_csv(input_path)
        enriched_df = asyncio.run(enrich(df))
        
        enriched_df.to_csv(input_path.replace(".csv", "_enriched.csv"), index=False)
        print(f"Enriched data saved to {input_path.replace('.csv', '_enriched.csv')}")



if __name__ == "__main__":
    main()


