import json #json package part form the standard library  built in  python 
import os

print("----------------------------------")
currentDirectory = os.getcwd()                      #Print current directory
print(currentDirectory)
print("----------------------------------")
print("----------------------------------")
os.chdir('/home/pvolcy/Documents/AutomatingBoringStuffWithPython/JSON')   #Change to Directory where the txt is located 
currentDirectory = os.getcwd()
print(currentDirectory)
print("----------------------------------")


with open("sw1.json", "r") as f:
    data = f.read()
   # print (data)    return the json file information

json_dict = json.loads(data) 
print(json_dict) #  json load to convert the json data structure into a dictionary
print ("The json document is loaded as a {0}\n").format(type(json_dict))
print("Now printing each item in this document and the type it contains")

for k , v in json_dict.items():
    print("The key {0} contains {1} value").format(str(k),str(v))
    if "vlans" in json_dict.keys():
        continue
    continue

print("----------------------------------\n")
print(json_dict["users"].items())
for k , v in json_dict["users"].items():
    print("The key {0} contains {1} value").format(str(k),str(v))

print("----------------------------------\n")

for k in json_dict["vlans"]:
    print ("\n"+str(k))
    for k , v in k.items():
        print("The key {0} contains {1} value").format(str(k),str(v))




    

