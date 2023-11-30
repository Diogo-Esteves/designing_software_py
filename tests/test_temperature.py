# tests/test_temperature.py
import unittest
from measurements.temperature import TemperatureSensor

class TestTemperatureSensor(unittest.TestCase):
    def test_take_measurement(self):
        sensor = TemperatureSensor()
        measurement = sensor.take_measurement()

        self.assertIn("timestamp", measurement)
        self.assertIn("temperature", measurement)
        self.assertIsInstance(measurement["temperature"], float)

if __name__ == "__main__":
    unittest.main()
