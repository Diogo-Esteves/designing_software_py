"""Performs basic analysis on the collected temperature data.

Returns:
    Dict: timestamp and temperature.
"""

class DataAnalyzer:
    def __init__(self, measurements):
        self.measurements = measurements

    def average_temperature(self):
        temperatures = [entry["temperature"] for entry in self.measurements]
        return sum(temperatures) / len(temperatures) if temperatures else None
