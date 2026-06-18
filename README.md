# AeroGrid-Turbine-Monitoring
Engineering project: IoT turbine telemetry analysis and cloud monitoring solution

# AeroGrid Turbine Monitoring

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


## Technology Used

- Python
- Pandas
- Docker
- IoT telemetry analysis
