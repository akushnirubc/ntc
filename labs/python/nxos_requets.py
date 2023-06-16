import requests
import json
from requests.auth import HTTPBasicAuth

requests.packages.urllib3.disable_warnings()


def nxapi_request(device, command):
    auth = HTTPBasicAuth("ntc", "ntc123")
    headers = {"Content-Type": "application/json"}

    url = f"https://{device}/ins"

    payload = {
        "ins_api": {
            "version": "1.0",
            "type": "cli_show",
            "chunk": "0",
            "sid": "1",
            "input": command,
            "output_format": "json",
        }
    }

    response = requests.post(
        url, data=json.dumps(payload), headers=headers, auth=auth, verify=False
    )
    return response


def get_nxos_neighbors(response):

    data = json.loads(response.text)

    device_neighbors = data["ins_api"]["outputs"]["output"]["body"][
        "TABLE_cdp_neighbor_brief_info"
    ]["ROW_cdp_neighbor_brief_info"]
    if isinstance(device_neighbors, dict):
        device_neighbors = [device_neighbors]

    neighbors_list = []
    for neighbor in device_neighbors:
        neighbor = {
            "neighbor_interface": neighbor["port_id"],
            "local_interface": neighbor["intf_id"],
            "neighbor": neighbor["device_id"],
        }
        neighbors_list.append(neighbor)

    return neighbors_list


def main():

    neighbors = {}

    devices = ["nxos-spine1", "nxos-spine2"]
    command = "show cdp neighbors"
    for dev in devices:
        response = nxapi_request(dev, command)
        neighbors[dev] = get_nxos_neighbors(response)

    print(json.dumps(neighbors, indent=4))


if __name__ == "__main__":
    main()