import os
from jinja2 import Environment, FileSystemLoader # 2 object imported t render template # Import Jinja2 library
import yaml# Import yaml library

ENV = Environment(loader=FileSystemLoader('/home/pvolcy/Documents/AutomatingBoringStuffWithPython/JINJA'))  #Create template Environment indicate that the template exist in the same direcoty where we started the interpreter
# Filters are added to the ENV object after declaration. Note that we're
# actually passing in our "get_interface_speed" function and not running
# it--the template engine will execute this function when we call
# template.render()
def get_interface_speed(interface_name):
    """ get_interface_speed returns the default Mbps value for a given
        network interface by looking for certain keywords in the name
    """
    if "gigabit" in interface_name.lower():
        return 1000
    if "fast" in interface_name.lower():
        return 100
ENV.filters["get_interface_speed"] = get_interface_speed
template = ENV.get_template("template.j2") # specificiate the template




    

interface_dict = {
     "name": "GigabitEthernet0/1",
     "description": "Server Port",
     "vlan": 10,
     "uplink": False #if the uplink property of interface is True, then we want to make this interface a VLAN trunk.
 }


intlist = [
    "GigabitEthernet0/1",
    "GigabitEthernet0/2",
    "GigabitEthernet0/3"
]

intdict = {
    "GigabitEthernet0/1": "Server port number one",
    "GigabitEthernet0/2": "Server port number two",
    "GigabitEthernet0/3": "Server port number three"
}

interfaces = [
    {
        "name": "GigabitEthernet0/1",
        "desc": "uplink port",
        "uplink": True
    },
    {
        "name": "GigabitEthernet0/2",
        "desc": "Server port number one",
        "vlan": 10
    },
    {
        "name": "GigabitEthernet0/3",
        "desc": "Server port number two",
        "vlan": 10
    }
]



print("----------------------------------")
currentDirectory = os.getcwd()                      #Print current directory
print(currentDirectory)
print("----------------------------------")
print("----------------------------------")
os.chdir('/home/pvolcy/Documents/AutomatingBoringStuffWithPython/JINJA')   #Change to Directory where the yml file  is located 
currentDirectory = os.getcwd()
print(currentDirectory)
print("----------------------------------")
with open("interfaces.yml") as f:
    interfaces = yaml.load(f)
    #print(template.render(interyes-http.j2))
    print(interfaces)
    #print(template.render(interface=interfaces))





#print(template.render(interface=interface_dict))
#print(template.render(interface_list=intlist))
#print(template.render(interface=intdict))
#print(template.render(interface=interfaces))

