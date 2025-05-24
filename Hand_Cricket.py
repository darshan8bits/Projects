import random
import math

print("Welcome to the Hand Cricket Game developed by Darshan")
print("Beware of spelling mistakes, else error will be generated.")
print("############################___LETS PLAY!___##############################")

def st(a):
    return a.strip().lower()

def genRan(r, d):
    return random.randrange(r, d)
def compDesc(a):
    if a == 0:
        return "bat"
    else:
        return "bowl"

def battfirst():
    print("You are about to start Batting, Good Luck!!!")
    user_score = 0
    comp_score = 0
    running = True
    while running:
        inp2 = int(input("Enter from 1 - 6: "))
        if inp2 not in range(1, 7):
            print("Invalid Input.")
            continue
        compinp2 = genRan(1, 7)
        print("Computer entered ", compinp2)
        if compinp2 == inp2:
            print("You are out! Your score:", user_score)
            print("Computer is going to Bat Next!")
            print("Computer needs ",user_score + 1, "runs to win!")
            running = False
        elif compinp2 != inp2:
            user_score += inp2
            print("Your score:", user_score)

        else:
            print("Invalid input somewhere, please restart again!!! ")
            
    running = True
    target = user_score + 1
    while running:
        if comp_score >= target:
            print("Computer has chased the score, You lose!")
            running = False
        
        else:    
            inp2 = int(input("Enter from 1 - 6: "))
            if inp2 not in range(1, 7):
                print("Invalid Input.")
                continue
            compinp2 = genRan(1, 7)
            print("Computer entered", compinp2)
            if inp2 == compinp2:
                if comp_score == user_score:
                    print("Draw match! Well plaid.")
                    running = False
                else:
                    print("Computer was out! You won the game by",user_score - comp_score, "runs.")
                    running = False
            elif compinp2 != inp2:
                comp_score += compinp2
                print("Computer's score:", comp_score)

            else:
                print("Invalid input somewhere, please restart again!!! ")
            
            

def ballfirst():
    print("You are about to start balling, Good Luck!!!")
    user_score = 0
    comp_score = 0
    running = True
    while running:
        inp2 = int(input("Enter from 1 - 6: "))
        if inp2 not in range(1, 7):
            print("Invalid Input.")
            continue
        compinp2 = genRan(1, 7)
        print("Computer entered ", compinp2)
        if compinp2 == inp2:
            print("The computer is out! Computer's score :",comp_score)
            print("You need", comp_score + 1, " runs to win!")
            running = False
        elif compinp2 != inp2:
            comp_score += inp2
            print("Computer score: ", comp_score)
        else:
            print("Invalid input somewhere, please restart again!")
    running = True
    target = comp_score + 1
    while running:
        if user_score >= target:
            print("You have chased the score! You won!")
            running = False
        
        else:    
            inp2 = int(input("Enter from 1 - 6: "))
            if inp2 not in range(1, 7):
                print("Invalid Input.")
                continue
            compinp2 = genRan(1, 7)
            print("Computer entered", compinp2)
            if inp2 == compinp2:
                if comp_score == user_score:
                    print("Draw match! Well plaid.")
                    running = False
                else:
                    print("You are out! Computer won the game by ",comp_score - user_score, "runs.")
                    running = False
            elif compinp2 != inp2:
                user_score += inp2
                print("Your score:", user_score)

            else:
                print("Invalid input somewhere, please restart again!!! ")

#Toss Module

inp = (st(input("Odd or Even? ")))
inp1 = int(st(input("Enter a number(1 - 6): ")))
compinp1 = genRan(1, 7)
print("Computer entered ",compinp1)
if inp == "odd":
    if (compinp1 + inp1) % 2 == 0:
        a =  compDesc(genRan(0, 2))
        print("You have lost the Toss.")
        print("The computer has decided to ",a, "first.")
    else:
        a = st(input("You have won the Toss. (Bat or Bowl)? "))

elif inp == "even":
    if(compinp1 + inp1) % 2 == 0:
        a = st(input("You have won the Toss. (Bat or Bowl)? "))
    else:
        a =  compDesc(genRan(0, 2))
        print("You have lost the Toss.")
        print("The computer has decided to ",a, "first.")

else:
    print("Invalid input somewhere, please restart again!!! ")


#Main Game

if a == 0 or a == "bowl":
    ballfirst()

elif a == 1 or a == "bat":
    battfirst()

else:
    print("Invalid input somewhere, please restart again!!! ")









    

