import pandas as pd
import plotly.express as px
import argparse

def visualize(input_csv, output_html):
    df = pd.read_csv(input_csv)
    # Handle negative magnitudes for sizing
    df['magnitude_size'] = df['magnitude'].clip(lower=0.1)  # Minimum size of 0.1
    fig = px.scatter_map(
        df,
        lat="latitude",
        lon="longitude",
        color="magnitude",
        size="magnitude_size",
        hover_name="place",
        hover_data=["time_iso", "depth_km"],
        color_continuous_scale="Viridis",
        size_max=12,
        zoom=1,
        height=600,
    )
    fig.write_html(output_html)
    print(f"Map saved to {output_html}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, default="data/earthquakes_last30.csv")
    parser.add_argument("--output", type=str, default="maps/earthquakes_map.html")
    args = parser.parse_args()
    visualize(args.input, args.output)