import re
message= "The ip address of the 1st Router is : 192.168.10.1 and the 2st is 172.169.10.1"
IPRegx = re.compile(r"\d\d\d.\d\d\d.\d\d.\d")
result=IPRegx.search(message)
#print(result.group())

#print(IPRegx.findall(message)) 

Message2  = " The ip address of the 1st Router is : 192.168.10.1"
IPRegx2 = re.compile(r"(\d\d\d).(\d\d\d).(\d\d).(\d)")
result=IPRegx2.search(Message2)
#print(result.group(1))
#print(result.group(2))
#print(result.group(3))
#print(result.group(4))

text3 = " The batmovile and batman got lost"
textRegx3 = re.compile(r"bat(man|movile|girl#)")
#print(textRegx3.findall(text3))
result3=textRegx3.search(text3)
#print(result3.group(0))
#print(result3.group(1))

message4 = " You can call me at +52 981-141-3405 tonight at 9 PM"
phoneRx4 = re.compile(r"(\+\d\d\s)?(\d\d\d-\d\d\d-\d\d\d\d)")
#print(phoneRx4.findall(message4))


text5 = " The batmovile and batwoman got lost"
textRegx5 = re.compile(r"bat(wo)*man") #0+
textRegx5 = re.compile(r"bat(wo)+man") #1+
result5 = textRegx5.search(text5)
#print(result5.group(0))
#print(result5.group(1))
#print(textRegx5.findall(text5))



text6 = "My numbers are 454-242-2442,424-242-2554,232-242-5532"
textRegx6 = re.compile(r"((\d\d\s)?\d\d\d-\d\d\d-\d\d\d\d(,)?){3}")
result6 = textRegx6.search(text6)
#print(result6.group())



text7 = ' "HaHaHaHaHaHa"  i said '
textRegx7 = re.compile(r"(Ha){3,5}")
#textRegx7 = re.compile(r"(Ha){3,5}?")
result7 = textRegx7.search(text7)
#print(result7.group())


text8 = "My numbers are 454-242-2444 , i never saw him calling me using the number 232-242-5532"
textRegx8 = re.compile(r"((\d\d\d)-(\d\d\d)-(\d\d\d\d))")
#print(textRegx8.findall(text8))



text9= " 12 Towels ksksksk 144 fuse_sa 14 pencil-red asaa"
textRegx9= re.compile(r"\d+\s\w+")
#print(textRegx9.findall(text9))


text9= " 12 Towels ksksksk 144 fuse_sa 14 pencil-red asaa"
textRegx9 = re.compile(r"[aeiouAEIOU]")
#print(textRegx9.findall(text9))

text9= " 12 Towels ksksksk 144 fuse_sa 14 pencil-red asaa"
textRegx9 = re.compile(r"[aeiouAEIOU]{2}")
#print(textRegx9.findall(text9))

text9= " 12 Towels ksksksk 144 fuse_sa 14 pencil-red asaa"
textRegx9 = re.compile(r"[^aeiouAEIOU]")  #Making your won regx
#print(textRegx9.findall(text9))


text10 = "The batmovile and batwoman got lost"
textRegx10 = re.compile(r"^The")
#print(textRegx10.findall(text10))
result10 = textRegx10.search(text10)
#print(result10.group(0))


text11 = "The batmovile and batwoman got lost"
textRegx11 = re.compile(r"lost$")
#print(textRegx11.findall(text11))

text12 = "lost"
textRegx12 = re.compile(r"^lost$")
#print(textRegx12.findall(text12))

text13 = "1212342154515345533432ff323"
textRex13=re.compile(r"^\d+")
#print(textRex13.findall(text13))


text14 = "1212342154515345533432fad1d1323"
textRex14=re.compile(r"\d+")
#print(textRex14.findall(text14))

text15 = "1212342154515345533432fad1d1323"
textRex15=re.compile(r"^\d+$")
#print(textRex15.findall(text15))

text16 = " The cat in the hat sat on the hlat mat"
textRegx16 = re.compile(r".at")   #MAtch anything except a new line
#print(textRegx16.findall(text16))

text17 = " The cat in the hat sat on the hlat mat"
textRegx17 = re.compile(r".{1,2}at")
#print(textRegx17.findall(text17))


text18 = " My First Name is : Philippe, My last name is: Volcy "
#print(text18.find(":"))
#print(text18[20:])


text20= " My First Name is : Philippe, My last name is: Volcy "
textRegx20 = re.compile(r"My First Name is : (.*)My last name is: (.*)")
#print(textRegx20.findall(text20))

text25= " My First Name is : Philippe, My last Name is : Volcy "
textRegx25 = re.compile(r" (My First Name|My last Name) is : (\w+)")
#print(textRegx25.findall(text25))

text21 = "<To serve a lot of dogs.> Make it fly>"
textRegx21 = re.compile(r"<.*?>")  # a non greedy match
#print(textRegx21.findall(text21))

text22 = "<To serve a lot of dogs.> Make it fly>"
textRegx22 = re.compile(r"<.*>")  # a greedy match
#print(textRegx22.findall(text22))

text23 = "Serve the pilot \n trust the plane \n and flyyyyy"
textRegx23 = re.compile(r".*",re.DOTALL)  #MAtch anything including a new line
#print(textRegx23.findall(text23))


text24 = "tHe batmovile and batwoman got lost"
textRegx24 = re.compile(r"^The",re.IGNORECASE)  # MAtch lower case/ upper case
#print(textRegx24.findall(text24))
result24 = textRegx24.search(text24)
#print(result24.group(0))


text26= " Agent is : Philippe, matter of fact Agent is : Volcy "
textRegx26 = re.compile(r"Agent is : \w+")
#print(textRegx26.findall(text26))
#print(textRegx26.sub("Andre",text26))

text27= " Agent is : Philippe, matter of fact Agent is : Volcy "
textRegx27 = re.compile(r"Agent is : (\w{1,2})\w*")
#print(textRegx27.findall(text27))
print(textRegx27.sub(r"Agent \1",text27))
