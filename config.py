#!/usr/bin/env python3
#!/usr/bin/env python 

devices = ['switch1', 'switch2', 'switch3']    #Dictionary of switch
vlans = [{'id': '10', 'name': 'USERS'}, {'id': '20', 'name': 'VOICE'},{'id': '30', 'name': 'WLAN'}] # List of dictionary

def extractId():  #1-The Vlan´s ID variable extracted from the List of Dictionary
    for items in vlans:
        id = items.get("id")
        return id

def extractName(): #2-The Vlan´s Name variable extracted from the List of Dictionary  
    for items in vlans:    
        name = items.get("name")
        return name

def CreateCommand(vlan , name):        #3.-Create proper command to configure Vlan by receiving 2 variables
    command = []
    command.append("Vlan "+vlan)
    command.append("Name "+name)
    return command

def  printSymbol(sym="*"):
    return sym *50

def Printspace(): #4.-Print Space between each Vlan configured
    print("\n")

def ExtractDevice():  #Extract Device in  Switch´s Dictionary
    for each in devices:
        return each
            


def pushCommandS(each, command):    #6.-Push Command to correct Device
    print("Connecting to device " + each)
    for commands in command:
        print("Sending command: "+commands)


def ConfiguringVlanForProperDevice(id,each,command): #Configure Vlan For Each device listed in Switch´s Dictionary
        print("C0NFIGURING VLAN"+id)
        pushCommandS(each,command)

def main():
    for items in vlans:
        VlanID=extractId()
        VlanNAme = extractName()
        command = CreateCommand(VlanID,VlanNAme)
        print(printSymbol())
        each =ExtractDevice()
        ConfiguringVlanForProperDevice(VlanID,each,command)
        Printspace()

if __name__ == "__main__":
    main()

        



       





