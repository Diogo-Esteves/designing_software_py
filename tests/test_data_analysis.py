# tests/test_data_analysis.py
import unittest
from measurements.temperature import TemperatureSensor
from analysis.data_analysis import DataAnalyzer

class TestDataAnalyzer(unittest.TestCase):
    def test_average_temperature(self):
        sensor = TemperatureSensor()
        analyzer = DataAnalyzer(sensor.measurements)

        for _ in range(5):
            sensor.take_measurement()

        avg_temp = analyzer.average_temperature()
        self.assertIsInstance(avg_temp, (float, type(None)))

if __name__ == "__main__":
    unittest.main()
