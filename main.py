"""Integrates the measurement and analysis modules, 
    simulating a metrology application.
"""

from measurements.temperature import TemperatureSensor
from analysis.data_analysis import DataAnalyzer

def main():
    sensor = TemperatureSensor()
    analyzer = DataAnalyzer(sensor.measurements)

    for _ in range(5):
        measurement = sensor.take_measurement()
        print(f"New Measurement: {measurement}")

    avg_temp = analyzer.average_temperature()
    print(f"Average Temperature: {avg_temp}")

if __name__ == "__main__":
    main()
