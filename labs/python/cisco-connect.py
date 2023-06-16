#! /usr/bin/env python

from netmiko import ConnectHandler

def ez_cisco(hostname, show_command, username="ntc", password="ntc123"):
    platform = "cisco_ios"
    # print(hostname)
    # print(username)
    # print(password)
    # print(show_command)
    device = ConnectHandler(
        ip=hostname, username=username, password=password, device_type=platform   
)
    output = device.send_command(show_command)
    device.disconnect()
    
    return output

response = ez_cisco("csr1", "show version")
print(response)

response = ez_cisco("csr2", "show ip int brief")
print(response)

response = ez_cisco("csr3", "show run | i snmp")
print(response)
    