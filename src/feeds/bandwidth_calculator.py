'''By Ray Bernard ray.bernard@outlook.com
     MIT License '''
import csv

class Bandwidth_Calculator(object):
    """
    A class used to calculate the disk space, bandwidth, and transfer time required for different media throughputs and read/write ratios.

    ...

    Attributes
    ----------
    media_throughput : float
        The media throughput in Mbps.
    read_ratio : float
        The read ratio as a decimal.
    write_ratio : float
        The write ratio as a decimal.
    initial_data_size : float
        The initial data size in GB.
    media_throughput_unit : str
        The unit of the media throughput ('Mbps', 'Gbps', or 'Tbps').
    initial_data_size_unit : str
        The unit of the initial data size ('GB', 'TB', or 'PB').

    Methods
    -------
    convert_to_mbps(media_throughput):
        Converts the media throughput to Mbps.
    convert_to_gb(initial_data_size):
        Converts the initial data size to GB.
    calculate():
        Calculates the disk space and bandwidth required and returns them as a list.
    write_to_csv(filename):
        Writes the results to a CSV file.
    transfer_time():
        Calculates the time required to transfer the initial data size at the media throughput.
    """

    def __init__(self, media_throughput, read_ratio, write_ratio, initial_data_size):
        """
        Constructs all the necessary attributes for the BandwidthCalculator object.

        Parameters
        ----------
            media_throughput : str
                The media throughput as a string with the value and unit separated by a space (e.g., '1 Gbps').
            read_ratio : float
                The read ratio as a percentage (e.g., 50 for 50%).
            write_ratio : float
                The write ratio as a percentage (e.g., 50 for 50%).
            initial_data_size : str
                The initial data size as a string with the value and unit separated by a space (e.g., '1 TB').
        """

        self.media_throughput = self.convert_to_mbps(media_throughput)
        self.read_ratio = read_ratio / 100  # Convert the read ratio to a decimal
        self.write_ratio = write_ratio / 100  # Convert the write ratio to a decimal
        self.initial_data_size = self.convert_to_gb(initial_data_size)
        self.media_throughput_unit = media_throughput.split()[1]
        self.initial_data_size_unit = initial_data_size.split()[1]

        # Validate the inputs
        if not (0 <= self.read_ratio <= 1 and 0 <= self.write_ratio <= 1):
            raise ValueError("Read and write ratios must be between 0 and 100.")
        if self.read_ratio + self.write_ratio != 1:
            raise ValueError("Read and write ratios must add up to 100.")
        if self.media_throughput <= 0:
            raise ValueError("Media throughput must be greater than 0.")
        if self.initial_data_size <= 0:
            raise ValueError("Initial data size must be greater than 0.")
        
        self.print_to_console()

    def convert_to_mbps(self, media_throughput):
        """
        Converts the media throughput to Mbps.

        Parameters
        ----------
            media_throughput : str
                The media throughput as a string with the value and unit separated by a space (e.g., '1 Gbps').

        Returns
        -------
            size : float
                The media throughput in Mbps.
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

        Parameters
        ----------
            initial_data_size : str
                The initial data size as a string with the value and unit separated by a space (e.g., '1 TB').

        Returns
        -------
            size : float
                The initial data size in GB.
        """

        size, unit = initial_data_size.split()
        size = float(size)
        if unit.lower() == 'tb':
            size *= 1000
        elif unit.lower() == 'pb':
            size *= 1000000
        return size

    def calculate(self):
        """
        Calculates the disk space and bandwidth required.

        Returns
        -------
        list
            A list containing the media throughput, read/write ratio, initial data size, disk space required for reads,
            disk space required for writes, bandwidth required for reads, bandwidth required for writes and time taken to transfer the initial data size at the given media throughput.
        """

        T = self.media_throughput
        R = self.read_ratio
        W = self.write_ratio

        DSR = (T * R) / 8
        DSW = (T * W) / 8
        BWR = T * R
        BWW = T * W
        Time = self.transfer_time()

        return [f"{T/1000 if self.media_throughput_unit == 'Gbps' else T} {self.media_throughput_unit}", f"{int(R*100)}:{int(W*100)}", f"{self.initial_data_size/1000 if self.initial_data_size_unit == 'TB' else self.initial_data_size} {self.initial_data_size_unit}", f"{DSR} MBps", f"{DSW} MBps", f"{BWR} Mbps", f"{BWW} Mbps", f"{Time} seconds"]

    def transfer_time(self):
        """
        Calculates the time required to transfer the initial data size at the media throughput.

        Returns
        -------
        time : float
            The transfer time in seconds.
        """

        # Convert Mbps to GBps
        media_throughput_in_gbps = self.media_throughput / 1000 / 8
        time = self.initial_data_size / media_throughput_in_gbps
        return time
    
    def convert_seconds_to_time(self, seconds):
        """
        Converts the given time in seconds to a more human-readable format (hours, minutes, and seconds).

        Parameters
        ----------
        seconds : float
            The time in seconds.

        Returns
        -------
        str
            The time in a more human-readable format (hours, minutes, and seconds).
        """

        hours = int(seconds // 3600)
        seconds %= 3600
        minutes = int(seconds // 60)
        seconds %= 60

        hours_text = f"{hours} hour" if hours == 1 else f"{hours} hours"
        minutes_text = f"{minutes} minute" if minutes == 1 else f"{minutes} minutes"
        seconds_text = f"{seconds:.1f} second" if seconds == 1 else f"{seconds:.1f} seconds"

        return f"{hours_text} {minutes_text} {seconds_text}"




    def transfer_time(self):
        """
        Calculates the time required to transfer the initial data size at the media throughput.

        Returns
        -------
        str
            The time required to transfer the initial data size at the media throughput in a more human-readable format (hours, minutes, and seconds).
        """

        # Calculate the time in seconds
        time_seconds = self.initial_data_size * 8000 / self.media_throughput  # the factor 8000 comes from conversion from GB to bits (1GB = 8000Mb)
        return self.convert_seconds_to_time(time_seconds)

    def write_to_csv(self, filename):
        """
        Writes the results to a CSV file.

        Parameters
        ----------
            filename : str
                The name of the CSV file to write to.
        """

        row = self.calculate()
        headers = ["Media Throughput", "Read/Write Ratio", "Initial Data Size", "Disk Space Required (Read)", "Disk Space Required (Write)", "Bandwidth Required (Read)", "Bandwidth Required (Write)", "Transfer Time"]
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerow(row)

    def print_to_console(self):
        """
        Prints the results to the console.
        """

        row = self.calculate()
        headers = ["Media Throughput", "Read/Write Ratio", "Initial Data Size", "Disk Space Required (Read)", "Disk Space Required (Write)", "Bandwidth Required (Read)", "Bandwidth Required (Write)", "Transfer Time"]
        
        # Print headers
        print("{:<20} {:<20} {:<20} {:<30} {:<30} {:<25} {:<25} {:<20}".format(*headers))

        # Print values
        print("{:<20} {:<20} {:<20} {:<30} {:<30} {:<25} {:<25} {:<20}".format(*row))




# if __name__ == "__main__":
#     # Create a BandwidthCalculator object
#     bc = Bandwidth_Calculator('1 Gbps', 50, 50, '1 TB')

#     # Write the results to a CSV file
#     bc.write_to_csv('feeds.csv')
