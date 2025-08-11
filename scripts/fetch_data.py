import requests
import pandas as pd
import argparse
import os

def fetch_and_save(output_csv):
    # Ensure directory exists
    output_dir = os.path.dirname(output_csv)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Fetch USGS Earthquake data (last 30 days)
    url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.csv"
    r = requests.get(url)
    r.raise_for_status()
    with open("temp_eq.csv", "wb") as f:
        f.write(r.content)
    df = pd.read_csv("temp_eq.csv")
    df.rename(columns={"mag": "magnitude"}, inplace=True)
    # Keep relevant columns and convert time to ISO format
    df["time_iso"] = pd.to_datetime(df["time"]).dt.strftime("%Y-%m-%dT%H:%M:%S")
    df = df[["id", "time_iso", "magnitude", "place", "latitude", "longitude", "depth"]]
    df.to_csv(output_csv, index=False)
    os.remove("temp_eq.csv")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=str, required=True)
    args = parser.parse_args()
    fetch_and_save(args.output)
