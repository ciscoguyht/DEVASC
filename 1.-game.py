import random

print("Helo, What is your name ?")
name = input()
print("Hello, "+name+" I am thing about a number between 1 and 20\nTake a guess")
number = random.randint(1,20)
print("For admin , Secret number is: "+str(number))
guessTaken = 0

for guessTaken in range(0,6):
    try:

        guess = input()
        if ( (int(guess) < number) & ( guessTaken < 5)) :
                print("Your guess is to loww, Please try again")
        elif ( (int(guess) > number) & (guessTaken < 5) ):
                print("Your guess is to high, Please try again")
        elif ( (int(guess) ==number) & (guessTaken < 5) ):
                print("Yes, you got it")
                break
        else:
                break
    except ValueError:
        print("You must insert a number not a string")
            

guessTaken = guessTaken +1
       

if int(guess) == number:
    print("You have guessed "+str(guessTaken)+" times")
else:
    print("Sorry , you try to maany times . GAME OVER")
