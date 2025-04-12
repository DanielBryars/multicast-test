# multicast_sender.py
import socket
import time
import struct

MCAST_GRP = '239.255.0.1'
MCAST_PORT = 5007

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
ttl = struct.pack('b', 1)  # Stay within local network
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

i=0
while True:
    i=i+1
    hostname = socket.gethostname()
    message = f"Hello Multicast:{i} from:'{hostname}'"
    sock.sendto(message.encode("utf-8"), (MCAST_GRP, MCAST_PORT))
    print("Sent")
    time.sleep(1)
