# Read a file of ip:port pairs, output a dict mapping each ip to a sorted list of unique ports.

# Let's first generate a .txt file of random ip:port combo

import random
from collections import defaultdict

def generateIPFile(amount: int, port_lower_limit: int, port_upper_limit: int):
    ip = "10.0.0" # /24 subnet let's say
    port = 0

    with open("random_IP.txt", "w") as file:
        for i in range(amount):
            port = random.randint(port_lower_limit, port_upper_limit)
            host = random.randint(1,254)
            curr_ip = f"{ip}.{host}"
            file.write(f"{curr_ip}:{port}\n")

generateIPFile(100, 0,1023)

IPDict = defaultdict(set)

with open("random_IP.txt", "r") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue

        parts = line.split(":")
        if len(parts) == 2:
            ip = parts[0]
            try:
                port = int(parts[1])
                IPDict[ip].add(port)
            except ValueError:
                print("Invalid port")

for ip,ports in IPDict.items():
    IPDict[ip] = sorted(list(ports))

print(IPDict)