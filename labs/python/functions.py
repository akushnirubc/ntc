#! /usr/bin/env python

def get_vlans():
    return [1, 5, 10, 20]

# def vlan_exists(vlan_id):
#     return vlan_id in get_vlans()

def vlan_exists(vlan_id):
    vlans = [1, 5, 10, 20]
    is_vlan_valid = vlan_id in vlans
    return is_vlan_valid

vlans = get_vlans()
print(vlans)
print(vlan_exists(20))
print(vlan_exists(12))