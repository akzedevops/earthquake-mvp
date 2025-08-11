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

def test_process_mixed_timestamp_formats():
    """Test that process_data.py can handle mixed timestamp formats (with and without microseconds)"""
    from scripts.process_data import process
    import tempfile
    
    # Create test CSV with mixed timestamp formats
    test_data = """id,time_iso,magnitude,place,latitude,longitude,depth
ew1234567890,2025-08-11T16:08:38,2.5,Northern California,37.8,-122.4,10.0
ew1234567891,2025-08-11T14:30:15.123456,3.2,Southern California,34.0,-118.2,15.0
ew1234567892,2025-08-10T09:45:22,1.8,Nevada,39.5,-119.8,5.0
ew1234567893,2025-08-10T22:12:45.789,4.1,Alaska,64.8,-147.7,25.0"""
    
    # Create temporary files
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as input_file:
        input_file.write(test_data)
        input_path = input_file.name
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as output_file:
        output_path = output_file.name
    
    try:
        # Test processing - this should not raise an error
        process(input_path, output_path)
        
        # Verify output
        assert os.path.exists(output_path)
        stats = pd.read_csv(output_path)
        assert "count" in stats.columns
        assert "avg_magnitude" in stats.columns
        assert stats["count"].iloc[0] == 4
        assert abs(stats["avg_magnitude"].iloc[0] - 2.9) < 0.1  # Approximate check
        
    finally:
        # Cleanup
        if os.path.exists(input_path):
            os.remove(input_path)
        if os.path.exists(output_path):
            os.remove(output_path)