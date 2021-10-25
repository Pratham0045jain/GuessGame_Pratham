from random import random

randNum = random()*10
num = round(random()*10)

chances = 1

""" print(num) """

   
while (chances <= 5):

    enteredNum = int(input("Type your number between 1 to 10 --- " )) 
    """ I forgot to use the int function, but will surly remember it next time. """
    print(enteredNum)

    if (num == enteredNum) :
        print("Congrats! You win!")
        break
    else:
        print("You lose, try again!")
        chances += 1
    

if not chances < 5:
    print("chances over")
