import scapy.all as scapy

# Implement your ICMP receiver here

def capture(packet):
    if packet.haslayer(scapy.ICMP) and packet[scapy.IP].ttl == 1:
        packet.show()

scapy.sniff(filter = "icmp", prn = capture, count = 1)
