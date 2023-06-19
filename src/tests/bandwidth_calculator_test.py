'''By Ray Bernard ray.bernard@outlook.com
     MIT License '''
import unittest
from bandwidth_calculator import Bandwidth_Calculator

class TestBandwidthCalculator(unittest.TestCase):
    """
    A class used to test the BandwidthCalculator class.

    Methods
    -------
    test_calculate():
        Tests the calculate method of the BandwidthCalculator class.
    test_invalid_ratios():
        Tests that the BandwidthCalculator class raises a ValueError when the read and write ratios do not add up to 100.
    test_invalid_media_throughput():
        Tests that the BandwidthCalculator class raises a ValueError when the media throughput is not greater than 0.
    test_invalid_initial_data_size():
        Tests that the BandwidthCalculator class raises a ValueError when the initial data size is not greater than 0.
    test_transfer_time():
        Tests the transfer_time method of the BandwidthCalculator class.
    """
    def test_calculate(self):
        # Create a BandwidthCalculator object
        bc = Bandwidth_Calculator('1 Gbps', 50, 50, '1 TB')

        # Define the expected result
        expected_result = ['1.0 Gbps', '50:50', '1.0 TB', '62.5 MBps', '62.5 MBps', '500.0 Mbps', '500.0 Mbps',
                        '2 hours 13 minutes 20.0']

        # Calculate the result
        result = bc.calculate()

        # Compare the result and expected result (excluding the "seconds" at the end)
        self.assertEqual(result[:-1], expected_result[:-1])
        self.assertEqual(result[-1].rstrip(" seconds"), expected_result[-1])



    def test_invalid_ratios(self):
        """
        Tests that the BandwidthCalculator class raises a ValueError when the read and write ratios do not add up to 100.

        The test checks that the constructor of the BandwidthCalculator class raises a ValueError when the read and write ratios do not add up to 100.
        """

        with self.assertRaises(ValueError):
            Bandwidth_Calculator('1 Gbps', 60, 50, '1 TB')

    def test_invalid_media_throughput(self):
        """
        Tests that the BandwidthCalculator class raises a ValueError when the media throughput is not greater than 0.

        The test checks that the constructor of the BandwidthCalculator class raises a ValueError when the media throughput is not greater than 0.
        """

        with self.assertRaises(ValueError):
            Bandwidth_Calculator('0 Gbps', 50, 50, '1 TB')

    def test_invalid_initial_data_size(self):
        """
        Tests that the BandwidthCalculator class raises a ValueError when the initial data size is not greater than 0.

        The test checks that the constructor of the BandwidthCalculator class raises a ValueError when the initial data size is not greater than 0.
        """

        with self.assertRaises(ValueError):
            Bandwidth_Calculator('1 Gbps', 50, 50, '0 TB')

    def test_transfer_time(self):
        calculator = Bandwidth_Calculator('1 Gbps', 50, 50, '1 TB')
        result = calculator.transfer_time()
        expected_result = '2 hours 13 minutes 20.0 seconds'  # 8000 seconds is equivalent to 2 hours 13 minutes and 20 seconds
        self.assertEqual(result, expected_result)



if __name__ == '__main__':
    unittest.main()
