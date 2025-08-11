import pandas as pd
import argparse
import os

def process(input_csv, output_csv):
    # Ensure directory exists
    output_dir = os.path.dirname(output_csv)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    df = pd.read_csv(input_csv)
    # Robust timestamp parsing
    df["date"] = pd.to_datetime(df["time_iso"], format="mixed").dt.date
    stats = {
        "count": len(df),
        "avg_magnitude": df["magnitude"].mean(),
        "min_magnitude": df["magnitude"].min(),
        "max_magnitude": df["magnitude"].max(),
    }
    pd.DataFrame([stats]).to_csv(output_csv, index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, required=True)
    parser.add_argument("--output", type=str, required=True)
    args = parser.parse_args()
    process(args.input, args.output)