from jinja2 import Environment, FileSystemLoader

ENV = Environment(loader=FileSystemLoader('/home/pvolcy/Documents/AutomatingBoringStuffWithPython/JINJA'))

template = ENV.get_template("template.j2")


class NetworkInterface():

    def __init__(self, name, description, vlan, uplink=False):  #Constructor
        self.name = name
        self.description = description
        self.vlan = vlan
        self.uplink = uplink

interface_obj = NetworkInterface("GigabitEthernet0/1", "Server Port", 10) #Intance of OBject

print(template.render(interface=interface_obj))


