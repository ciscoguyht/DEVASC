import os

print("----------------------------------")
currentDirectory = os.getcwd()                      #Print current directory
print(currentDirectory)

print("----------------------------------")
os.chdir('/home/pvolcy/Documents/AutomatingBoringStuffWithPython/CDLL_1/readFile.py')   #Change to Directory where the txt is located 
currentDirectory = os.getcwd()
print(currentDirectory)
print("----------------------------------")


demofile = open("demofile.txt", "rt")

#demofile = demofile.readlines()  #Return a dictionary where each line is an item including return character

#demofile = demofile.readline() Return a string Reads the lines one at a time

#demofile = demofile.read(6) Return  a specific number of character

#for line in demofile:  #Return a The file content as a string
#    print (line.strip("\n")) 


#name = input("Input your name here: ") #Have issue with python 2.7 for certain type of Data
name = raw_input("Input your name here: ")
print(name)