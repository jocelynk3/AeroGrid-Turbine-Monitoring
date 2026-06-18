import pandas as pd


# Load telemetry data
df = pd.read_excel("telemetry_data.xlsx")


# Calculate turbine metrics
turbine_metrics = df.groupby("turbine_id").agg(
    Average_Temperature=("temperature_c", "mean"),
    Maximum_Vibration=("vibration_mm_s", "max")
)


# Apply anomaly rules
failing_turbines = turbine_metrics[
    (turbine_metrics["Average_Temperature"] > 85.0)
    |
    (turbine_metrics["Maximum_Vibration"] > 15.0)
]


# Display failing turbines
print("Turbines requiring maintenance:")

for turbine in failing_turbines.index:
    print(turbine)


# Save results
failing_turbines.to_csv("failing_turbines.csv")

