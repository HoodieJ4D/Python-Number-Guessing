import random
import time

def guessing():
    b = int(input("What is your first guess?"))
    if b == x:
        time.sleep(1)
        print("Congratulations! You got the number!")
    elif b < x:
        time.sleep(1)
        print("The number is higher than your guess, try again")
    elif b > x:
        time.sleep(1)
        print("Your number is lower than your guess, try again")


print("Hello there")
time.sleep(3)
print("Today we're going to play a game")
time.sleep(3)
print("The game is this, I'll choose a random number between 0 and 100, and you'll have to guess the number")
time.sleep(3)
x = random.randint(0,100)
print("The number is chosen, you can begin guessing.")
guessing();