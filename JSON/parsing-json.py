import json

# JSON
print("#--------------- Working with JSON ---------------#")
print()

'''
JSON Functions

load()  - Import native JSON and convert to python dictionary from a file
loads() - Load string. Import JSON data from a string for parsing and manipulating within program
dump()  - Write JSON data from Python object to a file
dumps() - Dump string. Take JSON dictionary data and convert to a serialized string for parsing and manipulating

'''

with open("interfaces.json") as data:
    interfacedata = data.read()

with open("interfaces.json") as data:
    interfacedata2 = json.load(data) #load in json data straight into a dict

#Print raw JSON data string
print(interfacedata)
print('type of interfacedata json:', type(interfacedata))
print(interfacedata2)
print('type of interfacedata2 json:', type(interfacedata2))

#Convert JSON data into a dictionary
interfaces_dict = json.loads(interfacedata) #uses loads because interfacedata is a string
print('type of interface_dict after using loads function:', type(interfaces_dict))
print()

#Print interfaces dictionary
print(interfaces_dict)

#Modifying Data
interfaces_dict["interfaces"]["interface1"]["description"] = "Main uplink"
interfaces_dict["interfaces"]["interface2"]["description"] = "Backup uplink"
print()

#Print dictionary after updating data
print(interfaces_dict)
print()

#Print Individual peices of JSON
print(interfaces_dict["interfaces"]["interface1"]["ipv4"]["address"])

#Saving JSON data back to file
with open("interfaces.json", "w") as fh:
    json.dump(interfaces_dict, fh, indent=4) #indent is optional but helps with improving readability

print()