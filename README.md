# AeroGrid Turbine Monitoring
Engineering project: IoT turbine telemetry analysis and cloud monitoring solution

## Purpose:
This project analyses offshore wind turbine IoT telemetry data.

## Anomaly Rules:

A turbine requires maintenance if:

- Average Temperature > 85°C
- Vibration > 15 mm/s


## Running Locally

Install dependencies:

pip install -r requirements.txt


Run:

python analyse_turbines.py

## Output

The script analyses turbine telemetry data and identifies turbines requiring maintenance based on:

- Average temperature > 85°C
- Maximum vibration > 15 mm/s

Results are displayed in the terminal and saved to failing_turbines.csv.


## Technology Used

- Python
- Pandas
- Docker
- IoT telemetry analysis

