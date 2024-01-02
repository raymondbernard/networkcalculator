'''By Ray Bernard ray.bernard@outlook.com
     MIT License '''
import unittest
from bandwidth_calculator import BandwidthCalculator  # Make sure this matches the file name where the class is defined

class TestBandwidthCalculator(unittest.TestCase):

    def test_transfer_time(self):
        calculator = BandwidthCalculator('1 Gbps', 50, 50, '1 TB')
        result_seconds = calculator.transfer_time() 
        result_formatted = calculator.convert_seconds_to_time(result_seconds)
        expected_result = '4 hours, 39 minutes, 37.22 seconds'
        self.assertEqual(result_formatted, expected_result)

    def test_invalid_ratios(self):
        with self.assertRaises(ValueError):
            BandwidthCalculator('1 Gbps', 60, 50, '1 TB')

    def test_invalid_media_throughput(self):
        with self.assertRaises(ValueError):
            BandwidthCalculator('0 Gbps', 50, 50, '1 TB')

    def test_invalid_initial_data_size(self):
        with self.assertRaises(ValueError):
            BandwidthCalculator('1 Gbps', 50, 50, '0 TB')

    def test_transfer_time(self):
        calculator = BandwidthCalculator('1 Gbps', 50, 50, '1 TB')
        result_seconds = calculator.transfer_time()
        result_formatted = calculator.convert_seconds_to_time(result_seconds)
        expected_result = '4 hours, 39 minutes, 37.22 seconds'
        self.assertEqual(result_formatted, expected_result)


if __name__ == '__main__':
    unittest.main()
