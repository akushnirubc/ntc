#! /usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass

# CSR1 variables
# platform = 'cisco_ios'
# host = 'csr1'
# username = 'ntc'
# password = 'ntc123'
print("*" * 80)
print("Connecting to CSR1...")
csr1 = ConnectHandler(
    device_type='cisco_ios', ip='csr1', username='ntc', password=getpass()
)
# print(device.is_alive())
print("Saving CSR1 config")
save_cfg = csr1.send_command('wr mem')
print(save_cfg)

print("Backup CSR1 config")
csr1.send_command('term len 0')
csr1_conf = csr1.send_command('show run')

print("Write CSR1 backup config to /home/ntc/labs/python/configs/csr1.cfg")

with open("/home/ntc/labs/python/configs/csr1.cfg", "w") as csr1_output_file:
    csr1_output_file.write(csr1_conf)
csr1.disconnect()

print('*' * 80)

print("Connecting to CSR2...")
csr2 = ConnectHandler(
    device_type = 'cisco_ios', ip ='csr2', username = 'ntc', password = getpass()
)
print("Saving CSR2 config")
save_cfg = csr2.send_command("wr mem")
print(save_cfg)

print("Backup CSR2 config")
csr2.send_command('term len 0')
csr2_conf = csr2.send_command('show run')

print("Write CSR2 backup config to /home/ntc/labs/python/configs/csr2.cfg")

with open("/home/ntc/labs/python/configs/csr2.cfg", "w") as csr2_output_file:
    csr2_output_file.write(csr2_conf)
csr2.disconnect()
print('*' * 80)