import os
import subprocess
import datetime
import socket


time = datetime.datetime.now()

print("Network Watchdog Initialized ...")

ping_result = os.popen("ping -c 5 google.com").read()

print("Date_Time: {time}")
print(ping_result)
print("Resolved IP Address of nitrkl.ac.in")
ip_address = socket.gethostbyname("nitrkl.ac.in")
print(f"IP Address: {ip_address}")
print("THE END ......")

with open("watchdog_log.txt", "a") as f:
    print("Network Watchdog Initialized ...", file=f)
    print("Date_Time: {time}", file=f)
    print(ping_result, file=f)
    print("Resolved IP Address of nitrkl.ac.in", file=f)
    print(f"IP Address: {ip_address}", file=f)
    print("THE END ......", file=f)



    
    