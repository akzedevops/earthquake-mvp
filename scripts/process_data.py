import pandas as pd
import argparse

def process(input_csv, output_csv):
    df = pd.read_csv(input_csv)
    df['date'] = pd.to_datetime(df['time_iso']).dt.date
    stats = df.groupby('date').agg(
        count=('id', 'count'),
        avg_magnitude=('magnitude', 'mean')
    ).reset_index()
    stats.to_csv(output_csv, index=False)
    print(f"Saved daily stats to {output_csv}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, default="data/earthquakes_last30.csv")
    parser.add_argument("--output", type=str, default="data/daily_stats.csv")
    args = parser.parse_args()
    process(args.input, args.output)