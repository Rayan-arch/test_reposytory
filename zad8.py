#rock, papier, scissors game with computer
import random as r

invalid_input = False

print("Rock, paper, scissors game with computer.\n  If You want to end type 'quit'.")
print("-"*60)


while True:
    while invalid_input == False:
        usr_1 = input("Enter Scissors,Rock or Paper player 1: ").lower()
        if usr_1 == "r" or usr_1 == "s" or usr_1 == "p" or usr_1 == "quit":
            invalid_input = True
        else:
            print("Invalid input!")
    p2 =r.randint(0,2)
    usr = {0:"r",1:"p",2:"s"}
#Quit program
    if usr_1 == "quit":
        break
#print computer answer    
    if usr[p2] =="r":
        print("Rock")
    elif usr[p2] =="p":
        print("Paper")
    elif usr[p2] =="s":
        print("Scissors")
#Check who win by checing every single solution
    if usr_1 == usr[p2]:
        print("It's a tie!")
    if usr_1 == "p" and usr[p2] == "r":
        print(" You win the game!")
        print("#"*60)
    elif usr_1 == "r" and usr[p2] == "p":
        print("You lose the game!")
        print("#"*60)
    elif usr_1 == "s" and usr[p2] == "p":
        print("You win the game!")
        print("#"*60)
    elif usr_1 == "p" and usr[p2] == "s":
        print("You lose the game!")
        print("#"*60)
    elif usr_1 == "s" and usr[p2] == "r":
        print("You lose the game!")
        print("#"*60)
    elif usr_1 == "r" and usr[p2] == "s":
        print("You win the game!")
        print("#"*60)
    invalid_input = False
