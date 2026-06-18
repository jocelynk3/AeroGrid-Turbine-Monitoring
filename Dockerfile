FROM python:3.11-slim

WORKDIR /app

COPY analyse_turbines.py .
COPY telemetry_data.xlsx .

COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "analyse_turbines.py"]
