import ipaddress

ip = "192.168.0.1"

address = ipaddress.ip_address(ip)

print(address + 256)
