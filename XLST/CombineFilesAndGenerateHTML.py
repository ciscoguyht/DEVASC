from lxml import etree
#!/usr/bin/env python3
#!/usr/bin/env python 
import os

print("----------------------------------")
currentDirectory = os.getcwd()                      #Print current directory
print(currentDirectory)

print("----------------------------------")
os.chdir('/home/pvolcy/Documents/AutomatingBoringStuffWithPython/XLST')   #Change to Directory where the txt is located 
currentDirectory = os.getcwd()
print(currentDirectory)
print("----------------------------------")

stream = open("template.xsl","rb").read()
xslRoot = etree.fromstring(stream)
transform = etree.XSLT( xslRoot)
stream2 = open("xmldata.xml","rb").read()
xmlRoot = etree.fromstring(stream2)
transRoot = transform(xmlRoot)
print(transRoot)
print(etree.tostring(transRoot))


write_config_file = open("result.html", "w")
write_config_file.write(etree.tostring(transRoot))

print("----------------------------------")

print("File Create with success")