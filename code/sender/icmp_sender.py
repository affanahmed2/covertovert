import scapy.all as scapy

# Implement your ICMP sender here

packet = scapy.IP(dst="receiver", ttl=1) / scapy.ICMP()
scapy.send(packet)
