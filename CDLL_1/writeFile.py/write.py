import os

print("----------------------------------")
currentDirectory = os.getcwd()                      #Print current directory
print(currentDirectory)

print("----------------------------------")
os.chdir('/home/pvolcy/Documents/AutomatingBoringStuffWithPython/CDLL_1/writeFile.py')   #Change to Directory where the txt is located 
currentDirectory = os.getcwd()
print(currentDirectory)
print("----------------------------------")


file = open("device_info.txt")

name = file.readline().strip()
ip_address = file.readline().strip()
os_type = file.readline().strip()
username = file.readline().strip()
password = file.readline().strip()


print '--- Device info nicely formatted ----------------------------------'
print 'Name     IP addr         OS       Username   Password'
print '-----    --------------- -----    --------   --------'
print '{0:8} {1:15} {2:8} {3:12} {4:10}'.format(name, ip_address, os_type ,username, password)
