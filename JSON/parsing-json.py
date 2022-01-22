import json

"""
Created by Nick Miles
nicksnetworklab.com

JSON Functions

load()  - Import native JSON from a file and convert to it to a python object
loads() - Load string. Import JSON data from a string for parsing and manipulating within program
dump()  - Write JSON formatted data from Python object into a file
dumps() - Dump string. Take JSON dictionary data and convert to a serialized string for parsing and manipulating

"""


def main():

    # Load in JSON data using load
    with open("interfaces.json") as data:
        interface_data = json.load(data)

    #  Load in JSON formatted string
    with open("interfaces.json") as data:
        interface_data_string = data.read()

    print("Type of interface_data_string:", type(interface_data_string))
    print("Type of interface_data_string:", type(interface_data))

    # Convert a JSON formatted string to a python object
    interfaces_string_object = json.loads(
        interface_data_string
    )  # uses loads because interfacedata is a string
    print(
        "Type of interface_data_string after using loads function:",
        type(interfaces_string_object),
    )

    """
    We can manipulate this JSON data by navigating down the JSON structured and changing the values of the keys. 
    In this examintple, I changed the descriptions of the two GigabitEthernet interfaces, and the IP address 
    information of GigabitEthernet0/0.
    """
    # Editing Descriptions
    print("\nBefore Editing Descriptions")
    print(interface_data["interfaces"][0]["description"])
    print(interface_data["interfaces"][1]["description"])
    interface_data["interfaces"][0]["description"] = "Primary Uplink"
    interface_data["interfaces"][1]["description"] = "Secondary Uplink"
    print("After Editing Descriptions")
    print(interface_data["interfaces"][0]["description"])
    print(interface_data["interfaces"][1]["description"])

    # Editing IP Addresses
    print("\nBefore Editing IPv4 Info")
    print(interface_data["interfaces"][0]["ipv4"]["address"])
    print(interface_data["interfaces"][0]["ipv4"]["mask"])
    interface_data["interfaces"][0]["ipv4"]["address"] = "10.10.1.50"
    interface_data["interfaces"][0]["ipv4"]["mask"] = "255.255.255.252"
    print("\nAfter Editing IPv4 Info")
    print(interface_data["interfaces"][0]["ipv4"]["address"])
    print(interface_data["interfaces"][0]["ipv4"]["mask"])

    # Saving modified JSON data back to a file using dump
    with open("interfaces_dump.json", "w") as fh:
        json.dump(
            interface_data, fh, indent=4
        )  # indent is optional, but helps with improving readability

    # Loop through and print interfaces
    for interface in interface_data["interfaces"]:
        print(interface)


if __name__ == "__main__":
    main()
