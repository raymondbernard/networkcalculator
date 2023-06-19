'''By Ray Bernard ray.bernard@outlook.com
     MIT License '''
from ipaddress import IPv4Network, IPv4Address
import csv 



class Network_Calculator:
    def __init__(self, ip_cidr):
        """
        Constructor of the NetworkCalculator class

        Parameters:
            ip_cidr (str): The IP address with CIDR notation.

        Returns:
            None
        """
        # Splitting the ip and cidr
        self.ip, self.cidr = ip_cidr.split('/')
        self.cidr = int(self.cidr)

        # Creating IPv4 Network object
        self.network = IPv4Network(f"{self.ip}/{self.cidr}", strict=False)

    def get_subnet_mask(self):
        """
        Returns the subnet mask for the network.

        Parameters:
            None

        Returns:
            str: The subnet mask of the network.
        """
        return str(self.network.netmask)

    def get_network_id(self):
        """
        Returns the network ID for the network.

        Parameters:
            None

        Returns:
            str: The network ID of the network.
        """
        return str(self.network.network_address)

    def get_next_network(self):
        """
        Returns the network ID of the next network.

        Parameters:
            None

        Returns:
            str: The network ID of the next network.
        """
        return str(IPv4Address(self.network.network_address + (1 << (32 - self.cidr))))

    def get_broadcast_id(self):
        """
        Returns the broadcast ID for the network.

        Parameters:
            None

        Returns:
            str: The broadcast ID of the network.
        """
        return str(self.network.broadcast_address)

    def get_first_ip(self):
        """
        Returns the first usable IP for the network.

        Parameters:
            None

        Returns:
            str: The first usable IP address of the network.
        """
        return str(IPv4Address(self.network.network_address + 1))

    def get_last_ip(self):
        """
        Returns the last usable IP for the network.

        Parameters:
            None

        Returns:
            str: The last usable IP address of the network.
        """
        return str(IPv4Address(self.network.broadcast_address - 1))

    def get_total_ips(self):
        """
        Returns the total number of usable IP for the network.

        Parameters:
            None

        Returns:
            int: The total number of usable IP addresses in the network.
        """
        return (1 << (32 - self.cidr)) - 2 if self.cidr < 31 else (1 << (32 - self.cidr))

    def print_network_info(ip_list):
        """
        Prints information about a list of networks.

        Parameters:
            ip_list (list): A list of IP addresses with CIDR notation.

        Returns:
            None
        """
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format('CIDR', 'Subnet Mask', 'Network ID', 'Next Network', 'Broadcast ID', 'First IP', 'Last IP', 'Total IPs'))

        for ip_cidr in ip_list:
            net_calc = Network_Calculator(ip_cidr)

            print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
                ip_cidr,
                net_calc.get_subnet_mask(),
                net_calc.get_network_id(),
                net_calc.get_next_network(),
                net_calc.get_broadcast_id(),
                net_calc.get_first_ip(),
                net_calc.get_last_ip(),
                str(net_calc.get_total_ips())
            ))
        
    def write_to_csv(ip_list, filename):
        """
        Writes information about a list of networks to a CSV file.

        Parameters:
            ip_list (list): A list of IP addresses with CIDR notation.
            filename (str): The name of the CSV file to write to.

        Returns:
            None
            """
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['CIDR', 'Subnet Mask', 'Network ID', 'Next Network', 'Broadcast ID', 'First IP', 'Last IP', 'Total IPs'])

            for ip_cidr in ip_list:
                net_calc = Network_Calculator(ip_cidr)

                writer.writerow([
                    ip_cidr,
                    net_calc.get_subnet_mask(),
                    net_calc.get_network_id(),
                    net_calc.get_next_network(),
                    net_calc.get_broadcast_id(),
                    net_calc.get_first_ip(),
                    net_calc.get_last_ip(),
                    str(net_calc.get_total_ips())
                ])



    
# if __name__ == '__main__':
#     # Use it like this:
#     ip_list = ['198.51.100.0/22 ', '192.168.1.10/26', '172.16.0.5/16']

#     # Call the function with the list of CIDR IP addresses
#     Network_Calculator.print_network_info(ip_list)

#     # Call the function with the list of CIDR IP addresses and the filename
#     Network_Calculator.write_to_csv(ip_list, 'network.csv')