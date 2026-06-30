import random
playing = True
number = str(random.randint(0,9))
print("This is a guessing game. You have to guess a number between 0 and 9. The goal is to guess the right number.")
while playing == True:
    guess = (input("Guess a number"))
    if number == guess:
        print("YOU WIN!,The secret number was", number)
        break
    else:
        print("Wrong try again.")