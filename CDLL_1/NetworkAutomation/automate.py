import os
import pexpect


#session = connect(ip_address , username , password) #connect function from external pexpect library return a session using telnet




print("----------------------------------")
currentDirectory = os.getcwd()                      #Print current directory
print(currentDirectory)
print("----------------------------------")
print("----------------------------------")
os.chdir('/home/pvolcy/Documents/AutomatingBoringStuffWithPython/NetworkAutomation')   #Change to Directory where the txt is located 
currentDirectory = os.getcwd()
print(currentDirectory)
print("----------------------------------")


def get_device_list():

    device_list = []
        #file = open("devices.txt" , "r")
    with open("devices.txt" , "r") as f:
            
        for line in f:
            device_list.append(line.strip())
    f.close()   
    #print(device_list)
    return device_list


result =get_device_list()
print (result)



def connect(ip_address, username , password):
    print ("Establishing telnet session to ip address {0} with username {1} and password {2}").format(ip_address,username,password)
    #telnet_command = "telnet"+ ip_address

    #Connect to device with telnet
    session = pexpect.spawn("telnet " +ip_address, timeout=20)
    results = session.expect(["Username:",pexpect.TIMEOUT])

    if results !=0:
        print("Failed to establish Telnet connection with {0}").format(ip_address)
        exit()
    
    session.sendline(username)
    results = session.expect(["Password:",pexpect.TIMEOUT])

    if results !=0:
        print("Username {0} failed").format(username)
        exit()
    
    session.sendline(password)
    results = session.expect([">",pexpect.TIMEOUT])
    
    if results != 0:
        print '!!! Password failed: ', password
        exit()
    
    print '--- connected to: ', ip_address
    return session


def get_version(session):

    print(" Getting version of the device")
    session.sendline("en")
    results = session.expect(["Password:",pexpect.TIMEOUT])
    session.sendline("cisco")
    results = session.expect(["SWA#",pexpect.TIMEOUT])
    session.sendline("show version | inc Version")
    results = session.expect([">",pexpect.TIMEOUT])

    # Extract the 'version' part of the output
    #version = session.before.split(",")
    #version = version[1].strip()
    version = session.before.splitlines()
    version = version[1]
    version = version.split(",")
    version = version[1]
    print("The version is : "  +version)
    return version



if __name__ == "__main__":
    device_list = get_device_list()
    version_file_out = open("info.txt" ,"w")
    
    for ip_address in device_list:
        session = connect(ip_address ,"admin", "cisco!123")
        device_version= get_version(session)
        print("Creating File with information")
        version_file_out.write("IP: "+ip_address+ " and Version is : "+device_version)
    
    version_file_out.close()

       





