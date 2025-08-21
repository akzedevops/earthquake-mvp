# Earthquake Data Analysis MVP

A minimal viable product for analyzing and visualizing earthquake data from the USGS (United States Geological Survey) API. This project provides a complete data pipeline from fetching real-time earthquake data to processing statistics and creating interactive visualizations.

## Features

- **Data Fetching**: Automatically downloads the latest 30 days of earthquake data from USGS
- **Data Processing**: Generates statistical summaries including count, average, min, and max magnitudes
- **Interactive Visualization**: Creates interactive maps using Plotly to display earthquake locations and magnitudes
- **Streamlit Dashboard**: Web-based dashboard for exploring earthquake data with date filtering
- **Docker Support**: Containerized application for easy deployment
- **Automated Testing**: Comprehensive test suite using pytest
- **Build Automation**: Makefile for streamlined development workflow

## Prerequisites

- Python 3.11 or higher
- pip (Python package installer)
- Docker (optional, for containerized deployment)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/akzedevops/earthquake-mvp.git
   cd earthquake-mvp
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify installation**
   ```bash
   make test
   ```

## Usage

### Data Pipeline Commands

The project includes a Makefile for easy data pipeline management:

```bash
# Download latest earthquake data (last 30 days)
make fetch

# Process data to generate statistics
make process

# Create interactive visualization map
make visualize

# Run all pipeline steps
make fetch process visualize

# Run tests
make test
```

### Streamlit Dashboard

Launch the interactive web dashboard:

```bash
streamlit run app_streamlit.py
```

The dashboard provides:
- Interactive earthquake map with magnitude-based color coding and sizing
- Date range filtering for data exploration
- Real-time statistics display (total earthquakes, average magnitude)
- Hover details showing location, time, and depth information

### Docker Deployment

Build and run the application using Docker:

```bash
# Build the Docker image
docker build -t earthquake-mvp .

# Run the container
docker run -p 8080:8080 earthquake-mvp
```

Access the application at `http://localhost:8080`

## Project Structure

```
earthquake-mvp/
├── scripts/
│   ├── fetch_data.py          # Downloads earthquake data from USGS API
│   ├── process_data.py        # Processes data and generates statistics
│   └── visualize_map.py       # Creates interactive Plotly maps
├── src/
│   └── utils.py               # Utility functions for data handling
├── tests/
│   └── test_data_pipeline.py  # Test suite for data pipeline
├── data/                      # Data directory (created after running pipeline)
│   ├── earthquakes_last30.csv # Raw earthquake data
│   └── daily_stats.csv       # Processed statistics
├── maps/                      # Generated maps directory
│   └── earthquakes_map.html  # Interactive HTML map
├── app_streamlit.py          # Streamlit web dashboard
├── requirements.txt          # Python dependencies
├── Dockerfile               # Container configuration
├── Makefile                # Build automation
└── README.md               # This file
```

## Data Sources

- **USGS Earthquake API**: https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.csv
- **Data Coverage**: Global earthquakes from the last 30 days
- **Update Frequency**: Real-time (data refreshed with each fetch)
- **Data Fields**: 
  - ID, timestamp, magnitude, location description
  - Latitude, longitude, depth
  - Processed into ISO format timestamps

## Data Pipeline Details

1. **Fetch Stage** (`scripts/fetch_data.py`):
   - Downloads CSV data from USGS API
   - Cleans and standardizes column names
   - Converts timestamps to ISO format
   - Saves processed data to `data/earthquakes_last30.csv`

2. **Process Stage** (`scripts/process_data.py`):
   - Calculates summary statistics (count, avg, min, max magnitude)
   - Handles timestamp parsing for various formats
   - Outputs results to `data/daily_stats.csv`

3. **Visualize Stage** (`scripts/visualize_map.py`):
   - Creates interactive Plotly scatter mapbox
   - Color and size coding based on earthquake magnitude
   - Saves HTML map to `maps/earthquakes_map.html`

## Development

### Running Tests

```bash
# Run all tests
PYTHONPATH=. python -m pytest tests/ -v

# Run specific test
PYTHONPATH=. python -m pytest tests/test_data_pipeline.py -v
```

### Adding New Features

1. Add new scripts to the `scripts/` directory
2. Add corresponding Make targets to the `Makefile`
3. Create tests in the `tests/` directory
4. Update requirements.txt if new dependencies are needed

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Make your changes
4. Add tests for new functionality
5. Run the test suite (`make test`)
6. Commit your changes (`git commit -am 'Add new feature'`)
7. Push to the branch (`git push origin feature/new-feature`)
8. Create a Pull Request

## Dependencies

- **requests**: HTTP library for API calls
- **pandas**: Data manipulation and analysis
- **plotly**: Interactive plotting and visualization
- **streamlit**: Web application framework
- **pytest**: Testing framework

See `requirements.txt` for specific version requirements.

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.

## Troubleshooting

### Common Issues

1. **Module Import Errors**: Ensure you're running commands from the project root directory and set `PYTHONPATH=.` if needed

2. **Data Fetch Failures**: Check internet connectivity and USGS API availability

3. **Map Display Issues**: Ensure Plotly is properly installed and the output HTML file is accessible

4. **Streamlit Port Issues**: Use a different port with `streamlit run app_streamlit.py --server.port 8501`

### Support

For issues and questions:
- Check existing [GitHub Issues](https://github.com/akzedevops/earthquake-mvp/issues)
- Create a new issue with detailed description and error logs
- Include system information (Python version, OS) when reporting bugs

---

**Note**: This is a minimum viable product (MVP) designed for educational and demonstration purposes. For production use, consider adding error handling, data validation, logging, and monitoring capabilities.