from scapy.all import *

target_ip = "127.0.0.1"
target_port = 80

print("Sending Demo Packets...")

for i in range(5):
 ip = IP(dst=target_ip)
 tcp = TCP(dport=target_port, flags="S", sport=RandShort())
 packet = ip / tcp
 send(packet, verbose=False)
 print(f"Sent Demo Packets{i + 1}")

print("Demo Over")
