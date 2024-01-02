'''By Ray Bernard ray.bernard@outlook.com
     MIT License '''
import csv

class BandwidthCalculator:
    """
    A class used to calculate the disk space, bandwidth, and transfer time required for different media throughputs and read/write ratios.
    """

    def __init__(self, media_throughput, read_ratio, write_ratio, initial_data_size):
        """
        Constructs all the necessary attributes for the BandwidthCalculator object.
        """
        self.media_throughput = self.convert_to_mbps(media_throughput)
        self.read_ratio = read_ratio / 100  # Convert the read ratio to a decimal
        self.write_ratio = write_ratio / 100  # Convert the write ratio to a decimal
        self.initial_data_size = self.convert_to_gb(initial_data_size)

        # Validate the inputs
        if not (0 <= self.read_ratio <= 1 and 0 <= self.write_ratio <= 1):
            raise ValueError("Read and write ratios must be between 0 and 100.")
        if self.read_ratio + self.write_ratio != 1:
            raise ValueError("Read and write ratios must add up to 100.")
        if self.media_throughput <= 0:
            raise ValueError("Media throughput must be greater than 0.")
        if self.initial_data_size <= 0:
            raise ValueError("Initial data size must be greater than 0.")

    def convert_to_mbps(self, media_throughput):
        """
        Converts the media throughput to Mbps.
        """
        size, unit = media_throughput.split()
        size = float(size)
        if unit.lower() == 'gbps':
            size *= 1000
        elif unit.lower() == 'tbps':
            size *= 1000000
        return size

    def convert_to_gb(self, initial_data_size):
        """
        Converts the initial data size to GB.
        """
        size, unit = initial_data_size.split()
        size = float(size)
        if unit.lower() == 'tb':
            size *= 1024  # 1 TB = 1024 GB
        elif unit.lower() == 'pb':
            size *= 1024 * 1024  # 1 PB = 1024 TB = 1024 * 1024 GB
        return size

    def calculate(self):
        """
        Calculates the disk space and bandwidth required.
        """
        # Convert Mbps to GBps
        throughput_in_gbps = self.media_throughput / 1000 / 8  # 1 Mbps = 1/8 MBps = 1/8/1024 GBps

        # Calculate disk space required for reads and writes (in GB)
        disk_space_read = self.initial_data_size * self.read_ratio
        disk_space_write = self.initial_data_size * self.write_ratio

        # Calculate bandwidth required for reads and writes (in Mbps)
        bandwidth_read = self.media_throughput * self.read_ratio
        bandwidth_write = self.media_throughput * self.write_ratio

        # Calculate transfer time in seconds
        transfer_time_seconds = self.transfer_time()

        # Convert transfer time to a more readable format
        transfer_time_readable = self.convert_seconds_to_time(transfer_time_seconds)

        return [f"{self.media_throughput} Mbps", f"{int(self.read_ratio * 100)}:{int(self.write_ratio * 100)}", 
                f"{self.initial_data_size} GB", f"{disk_space_read} GB", f"{disk_space_write} GB", 
                f"{bandwidth_read} Mbps", f"{bandwidth_write} Mbps", transfer_time_readable]


    def transfer_time(self):
        """
        Calculates the total time required to transfer the initial data size at the media throughput.
        """
        # Convert media throughput from Mbps to GBps
        throughput_in_GBps = self.media_throughput / 8 / 1024  # 1 Mbps = 1/8 MBps = 1/8/1024 GBps
        
        # Calculate time for one operation (either read or write)
        time_for_one_operation_seconds = (self.initial_data_size / 2) / throughput_in_GBps

        # Total transfer time for both operations (read and write)
        # The original code had this correctly, but the result seems to be for one operation only.
        # We double the time to account for both read and write operations.
        total_transfer_time_seconds = time_for_one_operation_seconds * 2

        return total_transfer_time_seconds * 2


    def convert_seconds_to_time(self, seconds):
        """
        Converts the given time in seconds to a more human-readable format.
        """
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        seconds = seconds % 60
        return f"{hours} hours, {minutes} minutes, {seconds:.2f} seconds"

    def write_to_csv(self, filename):
        """
        Writes the results to a CSV file.
        """
        row = self.calculate()
        headers = ["Media Throughput", "Read/Write Ratio", "Initial Data Size", "Disk Space Required (Read)", 
                   "Disk Space Required (Write)", "Bandwidth Required (Read)", "Bandwidth Required (Write)", "Transfer Time"]
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerow(row)

    def print_to_console(self):
        """
        Prints the results to the console.
        """
        row = self.calculate()
        headers = ["Media Throughput", "Read/Write Ratio", "Initial Data Size", "Disk Space Required (Read)", 
                   "Disk Space Required (Write)", "Bandwidth Required (Read)", "Bandwidth Required (Write)", "Transfer Time"]
        
        print("{:<20} {:<20} {:<20} {:<30} {:<30} {:<25} {:<25} {:<20}".format(*headers))
        print("{:<20} {:<20} {:<20} {:<30} {:<30} {:<25} {:<25} {:<20}".format(*row))

# Example usage
if __name__ == "__main__":
    bc = BandwidthCalculator('1 Gbps', 50, 50, '1 TB')
    total_time_seconds = bc.transfer_time() 
    print(f"Total Transfer Time (seconds): {total_time_seconds}")
    total_time_readable = bc.convert_seconds_to_time(total_time_seconds)
    print(f"Total Transfer Time: {total_time_readable}")


