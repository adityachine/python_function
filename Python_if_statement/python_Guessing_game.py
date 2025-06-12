import random

jackpot = random.randint(1,100)
userinput = int(input("Chal Guess kar:- "))
counter = 1
while userinput != jackpot:
    if userinput < jackpot:
        print("Guess Higher number")
    else:
        print("Guess lower Number")    
    userinput = int(input("Chaal Guess Kar"))
    counter+=1    
print("sahi Guess")
print("you took ", counter,"attempts to guess the number")