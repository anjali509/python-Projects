import random
def guess():
    n=random.randrange(1,10)
    while True:
        num = int(input("Enter a number between range (0-10) :"))
        if num==n:
            print("Congrats!! guesses correctly...")
            break
        elif num>n:
            print("Guessed too high!! Try again...")
        elif num<n:
            print("Guessed too low!! Try again...")

guess()