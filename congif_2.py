#!/usr/bin/env python3
#!/usr/bin/env python 
import os

print("----------------------------------")
currentDirectory = os.getcwd()                      #Print current directory
print(currentDirectory)

print("----------------------------------")
os.chdir('/Users/pvolcy/Documents/Automating boring Stuff with Python')   #Change to Directory where the txt is located 
currentDirectory = os.getcwd()
print(currentDirectory)
print("----------------------------------")


vlan_config_file = open("vlan.txt","r") #Open the file
vlan_text = vlan_config_file.read()     #Read only save as String including spaces
vlan_text =vlan_text.split("\n")        #Remove space and save as list  of string   
#print(vlan_text)

vlans = [ ]             #Create a empty list
for items in vlan_text: #Run a loop and return a string per line
    if "vlan" in items: 
        temp ={}        
        id = items.strip().strip("vlan").strip()  #If "Vlan" found in strim create a empty dictionary, strip space , strip word(vlan) , strip any space left and add 1st key value into empty dictionary
        #print(id)
        temp["id"]=id
    
    elif "name" in items:
        name = items.strip().strip("name").strip() #If "name" found in strim , strip space , strip word(name) , strip any space left and add second key value into  dictionary
        #print(name)
        temp["name"]=name
        vlans.append(temp) #End od insertion of key value , Dictionary is append to list    

#print(items)
print(vlans)            #Print final list


vlan_config_file.close()  #Close File

write_config_file = open("configToFile.txt", "w")
for config in vlans:
    Id = config.get("id")
    name = config.get("name")
    write_config_file.write("Vlan "+Id+"\n")
    write_config_file.write(" Name "+name+"\n")
print("----------------------------------")

print("File Create with success")

vlan_config_file.close()
