import requests
import pandas as pd
import argparse
from datetime import datetime

USGS_URL = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson"

def fetch_and_save(output_csv):
    r = requests.get(USGS_URL)
    r.raise_for_status()
    data = r.json()
    rows = []
    for feature in data["features"]:
        prop = feature["properties"]
        geom = feature["geometry"]
        id = feature["id"]
        time_ms = prop["time"]
        magnitude = prop.get("mag")
        place = prop.get("place")
        tsunami = prop.get("tsunami")
        event_type = prop.get("type")
        lat, lon, depth_km = None, None, None
        if geom and geom["type"] == "Point":
            lon, lat, depth_km = geom["coordinates"]
        time_iso = datetime.utcfromtimestamp(time_ms / 1000).isoformat()
        rows.append({
            "id": id,
            "time_iso": time_iso,
            "time_ms": time_ms,
            "magnitude": magnitude,
            "place": place,
            "latitude": lat,
            "longitude": lon,
            "depth_km": depth_km,
            "tsunami": tsunami,
            "event_type": event_type
        })
    df = pd.DataFrame(rows)
    df.to_csv(output_csv, index=False)
    print(f"Saved {len(df)} records to {output_csv}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=str, default="data/earthquakes_last30.csv")
    args = parser.parse_args()
    fetch_and_save(args.output)