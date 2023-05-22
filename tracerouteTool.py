import sys
import socket
import struct
import time

def traceroute(host):
    dest_ip = socket.gethostbyname(host)
    max_hops = 30
    port = 33434
    icmp = socket.getprotobyname('icmp')
    udp = socket.getprotobyname('udp')

    print(f'Traceroute to {host} ({dest_ip}), {max_hops} hops max.\n')

    for ttl in range(1, max_hops + 1):
        # create sockets
        recv_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
        send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, udp)
        send_socket.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)

        # set timeout for recv_socket
        timeout = struct.pack("ll", 5, 0)
        recv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVTIMEO, timeout)

        # bind the recv_socket to a random port
        recv_socket.bind(("", port))

        # send an empty packet to the destination
        send_socket.sendto(b"", (host, port))

        current_address = None
        current_name = None
        try:
            # receive the packet and get the address and name of the router
            _, current_address = recv_socket.recvfrom(512)
            current_address = current_address[0]
            try:
                current_name = socket.gethostbyaddr(current_address)[0]
            except socket.error:
                current_name = current_address
        except socket.error:
            pass
        finally:
            send_socket.close()
            recv_socket.close()

        if current_address is not None:
            current_hop = f'{ttl:<3}'
            current_hop += f'{current_address: <18}'
            current_hop += f'{current_name}'
            print(current_hop)
        else:
            print(f'{ttl:<3} * * *')
        
        if current_address == dest_ip:
            break

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python traceroute.py <host>')
        sys.exit(1)
    host = sys.argv[1]
    traceroute(host)

