import schema
import pyxb


dev = schema.device()
dev.vendor = "Cisco"
dev.model = "Nexus"
dev.osver = "6.1"
dev.toxml("utf-8")
print(dev)



