from netmiko import ConnectHandler
from getpass import getpass

def print_logger(message, hostname):
    print(f"{message} | {hostname}")
    

def connect_to_device(hostname, username, password, device_type):
    print_logger("Connecting to device", hostname)
    device = ConnectHandler(
        host=hostname,
        username=username,
        password=password,
        device_type=device_type,
    )
    
    return device

def deploy_commands(device, hostname, config_file):
    print_logger("Sending commands from file", hostname)
    device.send_config_from_file(config_file)
    
def main(device_hostname, username, password, device_type):
    config_file = "./configs/snmp.cfg"
    
    net_device = connect_to_device(
        device_hostname, username, password, device_type
    )
    
    deploy_commands(net_device, device_hostname, config_file)
    
    print_logger("Disconnecting from device", device_hostname)
    net_device.disconnect()
    
device = input("Please enter the hostname or IP: ")
username = input("Please enter the username: ")
password = getpass("Please enter the password: ")
device_type = input("Please enter the device type: ")

main(device, username, password, device_type)