#import xml.etree.ElementTree as ET
from lxml import etree as ET
#!/usr/bin/env python3
import xmltodict
#!/usr/bin/env python 
import os

print("----------------------------------")
currentDirectory = os.getcwd()                      #Print current directory
print(currentDirectory)

print("----------------------------------")
os.chdir('/home/pvolcy/Documents/AutomatingBoringStuffWithPython/XML_CBT')   #Change to Directory where the txt is located 
currentDirectory = os.getcwd()
print(currentDirectory)
print("----------------------------------")

#Get XML file  data  
stream = open("sample.xml","r")

#xml2 = xmltodict.parse(stream.read())

#for e in xml2["authors"]["author"]:
    #print(e)



#PArse the data into a ElementTreeObject
xml = ET.parse(stream)



#Get the root Element object  from the ElementTreeObject
root = xml.getroot()

#Iterate  through each child of the root Element
       
for e in root:    
    #Print id attribute of the elements object
    print(e.get("id"))
    for ee in e:
     #PRint the stringified version of the element
        print (ET.tostring(ee))
        print("---------------- ")

    
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------


