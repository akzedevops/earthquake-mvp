import pandas as pd
import os

def test_fetch_and_process():
    from scripts.fetch_data import fetch_and_save
    from scripts.process_data import process

    # Fetch
    out_csv = "data/test_eq.csv"
    fetch_and_save(out_csv)
    assert os.path.exists(out_csv)
    df = pd.read_csv(out_csv)
    assert "id" in df.columns
    assert "time_iso" in df.columns

    # Process
    out_stats = "data/test_stats.csv"
    process(out_csv, out_stats)
    stats = pd.read_csv(out_stats)
    assert "count" in stats.columns
    assert "avg_magnitude" in stats.columns

    # Cleanup
    os.remove(out_csv)
    os.remove(out_stats)