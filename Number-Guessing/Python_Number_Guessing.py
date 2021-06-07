import random
import time

def guessing():
    time.sleep(2)
    b = int(input("What is your first guess? "))
    if b == x:
        time.sleep(1)
        print("Congratulations! You got the number!")
        time.sleep(3)
        quit()
    elif b < x:
        time.sleep(1)
        print("The number is higher than your guess, try again")
    elif b > x:
        time.sleep(1)
        print("Your number is lower than your guess, try again")
    time.sleep(1)
    b = int(input("What is your second guess? "))
    if b == x:
        time.sleep(1)
        print("Congratulations! You got the number!")
        time.sleep(3)
        quit()
    else:
        time.sleep(1)
        print("The number chosen is an " + c + " number")
        time.sleep(1)
        print("You have one more guess!")
    b = int(input("What is your final guess? "))
    if b == x:
        time.sleep(1)
        print("Congratulations! You got the number!")
        time.sleep(3)
        quit()
    else:
        time.sleep(1)
        print("Sorry, you couldn't guess the number.")
        time.sleep(1)
        print("The number was " + str(x))
        time.sleep(2)
        print("Thanks for playing!")
        time.sleep(3)
        quit()

print("Hello there")
time.sleep(3)
print("Today we're going to play a game")
time.sleep(3)
print("The game is this, I'll choose a random number between 0 and 20, and you'll have to guess the number")
time.sleep(3)
x = random.randint(0,20)
c = x % 2
if c == 0:
    c = "even"
else:
    c = "odd"
print("The number is chosen, you can begin guessing.")
guessing();