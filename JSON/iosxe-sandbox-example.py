import json
import requests

'''
Created by Nick Miles
nicksnetworklab.com

This demo is using the Cisco DevNet always-on IOS-XE sandbox with RESTCONF to retreive interface data and create new loopbacks.

Note: The credentials to this sandbox can change at anytime and I cannot guaratenee this script will remain updated with the latest credentials.
If the credntials are not working for you, you may need to check the sandbox at developer.cisco.com and update them accordinly.
'''

def main():

    # IOS-XE Sandbox Credentials
    HOST = "sandbox-iosxe-latest-1.cisco.com"
    PORT = 443
    USER = "developer"
    PASS = "C1sco12345"

    #Allow self signed certificates
    requests.packages.urllib3.disable_warnings()


    '''
    Retrieving interfaces
    '''
    url = f"https://{HOST}:{PORT}/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces/"
    headers = {
        'Content-Type': 'application/yang-data+json',
        'Accept': 'application/yang-data+json',
    }
    response = requests.get(url, headers=headers, verify=False, auth=(USER, PASS))

    if response.ok:
        print(response.text)
        response_json = response.json()

        # Write the retrieved interface data to a file
        with open("iosxe_interfaces.json", "w") as fh:
            json.dump(response_json, fh, indent=4)

    else:
        print(f"Error occurred with status code {response.status_code}")
    

    '''
    Creating a Loopback
    '''
    post_url = f"https://{HOST}:{PORT}/restconf/data/ietf-interfaces:interfaces"
    post_headers = {
    'Accept': 'application/yang-data+json',
    'Content-Type': 'application/yang-data+json',
    'Authorization': 'Basic ZGV2ZWxvcGVyOkMxc2NvMTIzNDU='
    }

    payload = json.dumps(
        {
            "ietf-interfaces:interface": {
                "name": "Loopback510",
                "description": "Added using RESTCONF and Python - nicksnetworklab.com",
                "type": "iana-if-type:softwareLoopback",
                "enabled": True,
                "ietf-ip:ipv4": {
                    "address": [
                        {
                            "ip": "50.10.10.10",
                            "netmask": "255.255.255.255"
                        }
                    ]
                }
            }
        }
    )
    post_response = requests.post(post_url, headers=post_headers, data=payload)
    print(post_response.text)

   # To veift the loopback was created, you can re-run this script. You should get an error saying it has already been created.
   # You will be able to see the newly created loopback interface in the iosxe_interfaces.json file once you re-run it.

if __name__ == "__main__":
    main()
