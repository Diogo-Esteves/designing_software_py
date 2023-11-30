"""Simulates a temperature sensor and collects measurements.

Returns:
    Dict: timestamp and temperature.
"""

import random
import time

class TemperatureSensor:
    def __init__(self):
        self.measurements = []

    def take_measurement(self):
        temperature = random.uniform(20.0, 30.0)
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        self.measurements.append(
            {
                "timestamp": timestamp,
                "temperature": temperature
            }
        )
        return {"timestamp": timestamp, "temperature": temperature}
