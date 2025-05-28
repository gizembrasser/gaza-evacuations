import asyncio
import pandas as pd
from x_scraper import scrape_tweet

async def main(df):
    """Enrich a DataFrame containing tweet URLs with tweet text and timestamp."""
    texts = []
    timestamps = []

    for i, url in enumerate(df["source"].to_list()):
        print(f"Scraping {i+1}/{len(df)}: {url}")

        text, timestamp = await scrape_tweet(url)
        texts.append(text)
        timestamps.append(timestamp)
    
    df["source_text"] = texts
    df["source_timestamp"] = timestamps
    return df


if __name__ == "__main__":
    # Load original CSV and run enrichment
    df = pd.read_csv("data/displacement.csv")
    enriched_df = asyncio.run(main(df))

    # Save result
    enriched_df.to_csv("data/displacement_enriched.csv", index=False)
    print("Saved to data/displacement_enriched.csv")


