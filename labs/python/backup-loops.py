#! /usr/bin/env python

from netmiko import ConnectHandler

devices = ["csr1", "csr2", "csr3"]

for device in devices:
    print(f"Connecting to device | {device}")

    net_device = ConnectHandler(
        host=device, username="ntc", password="ntc123", device_type="cisco_ios"
    )

    print(f"Saving configuration | {device}")

    net_device.send_command("wr mem")

    print(f"Backing up configuration | {device}")

    net_device.send_command("term len 0")
    net_config = net_device.send_command("show run")

    print(f"Writing config to file | {device}\n")

    with open(f"/home/ntc/labs/python/configs/{device}.cfg", "w") as config_file:
        config_file.write(net_config)