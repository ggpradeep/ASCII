import random
import math
print("Random Fun Calculator!!")

lucky_number = random.randint(1, 10)
print("Your lucky number is:", lucky_number)
fun_choices = ["Run for 5 minutes", "Say a tounge twister", "Create a game", "Be nice to someone"]
random_activity = random.choice(fun_choices)
print("Random activity for today:", random_activity)
print("\nGuess the secret number from 1 to 5!")
secret_number = random.randint(1, 5)

while True:
    guess = int(input("Enter your guess: "))
    if guess == secret_number:
        print("Correct! You guessed the number.")
        break
    else:
        print("Wrong guess. Try again!")

decimal_number = float(input("\nEnter a decimal number: "))
print("Ceiling value:", math.ceil(decimal_number))
print("Floor value:", math.floor(decimal_number))

print("x = 10 and y = -5")
x = 10
y = -5
print("Copy sign result:", math.copysign(x, y))
negative_number = int(input("Enter a negative number: "))

print("Absolute value:", math.fabs(negative_number))

number1 = int(input("Enter first number for the greatest common factor: "))
number2 = int(input("Enter second number for the greatest common factor: "))

print("The GCF is:", math.gcd(number1, number2))
print("\nVery fun calculator summary!")
print("Lucky Number:", lucky_number)
print("Random Activity:", random_activity)
print("Secret Number:", secret_number)
