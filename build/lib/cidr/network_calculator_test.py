'''By Ray Bernard ray.bernard@outlook.com
     MIT License '''
import unittest
from ipaddress import IPv4Network, IPv4Address
from network_calculator import Network_Calculator


class TestNetworkCalculator(unittest.TestCase):
    def setUp(self):
        self.net_calc = Network_Calculator('192.168.1.0/24')

    def test_get_subnet_mask(self):
        self.assertEqual(self.net_calc.get_subnet_mask(), '255.255.255.0')

    def test_get_network_id(self):
        self.assertEqual(self.net_calc.get_network_id(), '192.168.1.0')

    def test_get_next_network(self):
        self.assertEqual(self.net_calc.get_next_network(), '192.168.2.0')

    def test_get_broadcast_id(self):
        self.assertEqual(self.net_calc.get_broadcast_id(), '192.168.1.255')

    def test_get_first_ip(self):
        self.assertEqual(self.net_calc.get_first_ip(), '192.168.1.1')

    def test_get_last_ip(self):
        self.assertEqual(self.net_calc.get_last_ip(), '192.168.1.254')

    def test_get_total_ips(self):
        self.assertEqual(self.net_calc.get_total_ips(), 254)

if __name__ == '__main__':
    unittest.main()
