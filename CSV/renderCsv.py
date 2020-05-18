import os
import csv
from jinja2 import Template, FileSystemLoader , Environment

ENV = Environment(loader=FileSystemLoader(('/home/pvolcy/Documents/AutomatingBoringStuffWithPython/CSV')))
template = ENV.get_template("configfromCSV.j2")

print("----------------------------------")
currentDirectory = os.getcwd()                      #Print current directory
print(currentDirectory)
print("----------------------------------")
print("----------------------------------")
os.chdir('/home/pvolcy/Documents/AutomatingBoringStuffWithPython/CSV')   #Change to Directory where the yml file  is located 
currentDirectory = os.getcwd()
print(currentDirectory)
print("----------------------------------")

with open("switch-ports.csv") as f:
    output = csv.DictReader(f)
    #print (output)
    print(template.render(interface_list=output))
    