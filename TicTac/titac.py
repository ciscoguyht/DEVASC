#! /usr/bin/env  python3
import pprint
import random



def createTicTacBoard():
    tictac = {"Top-L":" ","Top-M":" ","Top-R":" ","Mid-L":" ","Mid-M":" ","Mid-R":" ","Low-L":" ", "Low-M": " ","Low-R":" "}
    return tictac

def RandomTicTacBoardPop():
    newBoard = {"Top-L":" ","Top-M":" ","Top-R":" ","Mid-L":" ","Mid-M":" ","Mid-R":" ","Low-L":" ", "Low-M": " ","Low-R":" "}
    return newBoard

def printboard(titac):
    
    print(titac["Top-L"] + "|" + titac["Top-M"] + "|" + titac["Top-R"]  )
    print("-----")
    print(titac["Mid-L"] + "|" + titac["Mid-M"] + "|" + titac["Mid-R"]  )
    print("-----")
    print(titac["Low-L"] + "|" + titac["Low-M"] + "|" + titac["Low-R"]  )


def ComputerPlay(titac,newTiTacBoard):
    choosenValue = random.choice(titac.keys())
    print("ChoosenValue is :"+choosenValue)
    for key , value  in titac.items():
        if key == choosenValue:
            titac[key] = "X"
            
            

    for key , value  in newTiTacBoard.items():
        
        if key == choosenValue:
            choosenKey = key

    newTiTacBoard.pop(choosenKey)

    
def UserPlay(titac,newTiTacBoard):
    choosenValue = raw_input("Do your play:")
    titac[choosenValue] = "0"
            

    for key , value  in newTiTacBoard.items():
        if key == choosenValue:
            choosenKey = key
    newTiTacBoard.pop(choosenKey)



def WinConditionComputer(titac):
    for key , value in titac.items():
        if   ( titac["Top-L"]== "X" and titac["Top-M"]== "X" and titac["Top-R"]== "X") or ( titac["Mid-L"] == "X" and titac["Mid-M"]== "X" and titac["Mid-R"]== "X" ) or ( titac["Low-L"]== "X" and titac["Low-M"]== "X"  and titac["Low-R"]== "X" ) :
            print ("Computer Won")
            Again == False 
            return Again

def WinConditionUser(titac):
    for key , value in titac.items():
        if   ( titac["Top-L"]== "0" and titac["Top-M"]== "0" and titac["Top-R"]== "0") or ( titac["Mid-L"] == "0" and titac["Mid-M"]== "0" and titac["Mid-R"]== "0" ) or ( titac["Low-L"]== "0" and titac["Low-M"]== "0"  and titac["Low-R"]== "0" ) :
            print ("User Won")
            Again == False 
            return Again
            




if __name__ == "__main__":
    print("Initial board will be Created")
    print("Board created")

    tictac = createTicTacBoard()
    newTicTacBoard = RandomTicTacBoardPop()
    print("Initial board will be printed:")
    printboard(tictac)
    
    Again = True

    while Again == True: 
        print("Philippe it's your  turn to play")
        UserPlay(tictac,newTicTacBoard)
        printboard(tictac)
        print(newTicTacBoard)
        WinConditionUser(tictac)
        print(Again)

        print("Computer turn to play")
        ComputerPlay(tictac,newTicTacBoard)
        printboard(tictac)
        print(newTicTacBoard)
        WinConditionComputer(tictac)
        print(Again)
        
        
    
    print("Game over")

    
    
