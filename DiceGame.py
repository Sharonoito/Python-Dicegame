import random

def roll_dice(min,max):
    while True:
        number=random.randint(min,max)
        print("Your number :{}".format(number))
        print("Rolling dice...")
        option=input("Do you want to roll the dice again? (y/n)") 
        if option.lower()=='n':
            break


roll_dice(1,6)




