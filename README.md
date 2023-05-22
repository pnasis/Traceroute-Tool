# Traceroute Tool
A traceroute tool is a network diagnostic utility used to trace the path that network packets take from a source host to a destination host over an IP network. It provides valuable information about the routers or intermediate devices (hops) that the packets traverse through. The tool helps in identifying network connectivity issues, network congestion points, and potential bottlenecks.

When a traceroute is performed, the tool sends out a series of ICMP (Internet Control Message Protocol) or UDP (User Datagram Protocol) packets with increasing TTL (Time to Live) values. The TTL field specifies the maximum number of hops a packet can traverse before being discarded. Each router encountered along the path decrements the TTL value of the packet by one and, if the TTL reaches zero, the router discards the packet and sends an ICMP Time Exceeded message back to the source host.

By sending multiple packets with increasing TTL values, the traceroute tool can map the path taken by the packets to the destination. It collects the IP addresses and round-trip times (RTTs) of the intermediate routers and presents them in a formatted output, usually displayed as a table. This information helps in understanding the network topology and diagnosing network connectivity issues.

Traceroute is commonly used by network administrators, system administrators, and users who need to troubleshoot network problems, measure network performance, or analyze network routes. It provides insights into the routing infrastructure of the Internet and assists in identifying the point of failure or delay in network communication.

## Installation
You don't need to install any libraries, because it's already preinstalled.

## Usage

```Bash
# To run the program
python3 tracerouteTool.py <host>

```

## Contributing

>Pull requests are welcome. **For major changes, please open an issue first
to discuss what you would like to change.**


## License

>This project is under [Apache 2.0](https://choosealicense.com/licenses/apache-2.0/) licence.
