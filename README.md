# Network Calculator

### The What and Why of Network Calculations
In networking, IP addresses and subnet masks are crucial for defining the structure and reach of the network. However, doing these calculations manually can be cumbersome and error-prone. This is where Python, with its vast library support and simplicity, can be a lifesaver.

In this article, we'll delve into a Python class called I have created called the 'NetworkCalculator'. It is designed to automate common network calculation tasks. To fully understand this, it is recommended you have some basic knowledge of IP addresses, subnet masks, network IDs, broadcast IDs, and CIDR notation. There are a tone of online resources to help your understanding. 

The NetworkCalculator class is initialized with an IP address in CIDR notation as input. CIDR (Classless Inter-Domain Routing) notation represents an IP address and its associated routing prefix. 

For instance, '192.168.1.10/24' is an example of an IP address in CIDR notation.
The __init__ method splits the IP address and the CIDR subnet prefix, and an IPv4Network object is created with these. The strict=False parameter allows the IP address part to be any IP address inside the network.

### Network Calculator Methods you can use in your code 
```

After creating the NetworkCalculator object, Here are several methods can we create and us to perform network calculations:

get_subnet_mask(): Returns the subnet mask of the network. The subnet mask defines the size of the network.

get_network_id(): Returns the Network ID. This is the first IP address in the network and it identifies the network itself.

get_next_network(): Returns the Network ID of the next network. It's calculated by adding 2^(32 - CIDR) to the network address.

get_broadcast_id(): Returns the last IP address in the network, which is used for broadcasting messages to all devices in the network.

get_first_ip(): Returns the first usable IP address in the network. It's simply the Network ID plus one.

get_last_ip(): Returns the last usable IP address in the network, which is one less than the broadcast ID.

get_total_ips(): Returns the total number of usable IP addresses in the network.
```

```python

pip install networkcalculator

```


### how to use the code 
```python 

from cidr.networkcalculator  import Network_Calculator

# Use it like this:
ip_list = ['198.51.100.0/22 ', '192.168.1.10/26', '172.16.0.5/16']

# Call the function with the list of CIDR IP addresses
Network_Calculator.print_network_info(ip_list)

# Call the function with the list of CIDR IP addresses and the filename of your output file
Network_Calculator.write_to_csv(ip_list, 'network.csv')

```

### Output 

| CIDR            | Subnet Mask     | Network ID   | Next Network | Broadcast ID   | First IP     | Last IP        | Total IPs |
| --------------- | --------------- | ------------ | ------------ | -------------- | ------------ | -------------- | --------- |
| 198.51.100.0/22 | 255.255.252.0   | 198.51.100.0 | 198.51.104.0 | 198.51.103.255 | 198.51.100.1 | 198.51.103.254 | 1022      |
| 192.168.1.10/26 | 255.255.255.192 | 192.168.1.0  | 192.168.1.64 | 192.168.1.63   | 192.168.1.1  | 192.168.1.62   | 62        |
| 172.16.0.5/16   | 255.255.0.0     | 172.16.0.0   | 172.17.0.0   | 172.16.255.255 | 172.16.0.1   | 172.16.255.254 | 65534     |
|                 |                 |              |              |                |              |                |           |

### Bandwidth Calculator  

```python
from feeds.bandwidth_calculator import Bandwidth_Calculator


# Create a BandwidthCalculator object

bc = Bandwidth_Calculator('1 Gbps', 50, 50, '1 TB') # thoughtput , reads %, writes /%, Initial data size 

# Write the results to a CSV file
bc.write_to_csv('feeds.csv')


```

| Media Throughput | Read/Write Ratio | Initial Data Size | Disk Space Required (Read) | Disk Space Required (Write) | Bandwidth Required (Read) | Bandwidth Required (Write) | Transfer Time                           |
| ---------------- | ---------------- | ----------------- | -------------------------- | --------------------------- | ------------------------- | -------------------------- | --------------------------------------- |
| 1.0 Gbps         | 50:50            | 1.0 TB            | 62.5 MBps                  | 62.5 MBps                   | 500.0 Mbps                | 500.0 Mbps                 | 2 hours 13 minutes 20.0 seconds seconds |
|                  |                  |                   |                            |                             |                           |                            |                                         |







### About: 
Ray Bernard is a seasoned technologist specializing in cloud-based platforms, data science, and AI. He co-founded SuprFanz, a revolutionary cloud-based marketing company, and has held key roles at EMC, Ticket Master, and Compaq. As an Affiliate Developer, Systems Engineer, and Community Advocate, he demonstrated exceptional technical prowess and innovative thinking. Ray also taught Internet/Intranet Management & Design at Columbia University, further contributing to the field. With his vast experience and proactive problem-solving approach, he consistently drives digital transformation. 
Contact him: ray.bernard@outlook.com 
LinkedIn : https://www.linkedin.com/in/ray-bernard-960382/
Git : https://github.com/raymondbernard/