def introduction(nombre):
   
    print("Nice to Meet you, "+nombre)
    print("It is really simple to do scripting with me .. But i can do a lot of things...\nLet me show you\nI can add two numbers and give you the result")


def addition(n1 , n2):
    result = n1 + n2
    print("{} + {} = {}".format(n1,n2,result))

def introductionMultiplication():
    print("Also , i can multiply 2 numbers and give you the results")
    print("Give me a number")

def multiplication(n1 , n2):
    result = n1 * n2

    print("{} * {} = {}".format(n1,n2,result))


def introductionMultiplication():
    print("Also , i can do bolean operation as well")
    print("Give me one string")

def compareStrings(w1,w2):
    print("{} is equal to {} ?".format(w1,w2))
    if w1 == w2:
        print("True")
    else:
        print("False")

def prediction(edad):
    result = edad + 5
    print("In 5 years you will be {} OMG! You are really old\nC you next time :D with more python".format(result))
    for n in range(0,8):
        ntimes = "*" * n
        print(ntimes)
    

if __name__ == "__main__":
    print("Hello World, I`m python.. What's your name ?")
    name=input()
    introduction(name)
    print("Give me a number")
    number1=float(input("Number: " ))
    print("Give me another number:")
    number2=float(input("Another number " ))
    addition(number1,number2)
    introductionMultiplication()
    number1=float(input("Number: " ))
    print("Give me another number:")
    number2=float(input("Another number " ))
    multiplication(number1 , number2)
    introductionMultiplication()
    word1= input("String: ")
    print("Give me another string: ")
    word2=input("Another String: ")
    compareStrings(word1,word2)
    print("How old are you ?")
    age=int(input())
    prediction(age)






   
    



