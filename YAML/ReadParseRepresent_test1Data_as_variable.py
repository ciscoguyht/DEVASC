import yaml
from yaml import load_all, load_all
import os

print("----------------------------------")
currentDirectory = os.getcwd()                      #Print current directory
print(currentDirectory)

print("----------------------------------")
os.chdir('/Users/pvolcy/Documents/Automating boring Stuff with Python/YAML')   #Change to Directory where the txt is located 
currentDirectory = os.getcwd()
print(currentDirectory)
print("----------------------------------")

#with open("test1.yml") as f:
    #result = yaml.load(f)
    #print(result)
    #type(result)

with open("test1.yml") as stream:
    documents = load_all(stream,Loader=yaml.FullLoader)
    print(type(documents))

    for doc in documents:
        print(type(doc))
        print(doc)
        print("------------------------------------------------------------------------------------------------------------------------------------------------------")
        print(doc["people"])
        print("------------------------------------------------------------------------------------------------------------------------------------------------------")
        print(doc["people"][2])
        print("------------------------------------------------------------------------------------------------------------------------------------------------------")
        print(doc["people"][2]["Lab"])