import random

au=random.randint(1,100)

guess=int(input("Guess a number  "))
count=1

while guess!=au:
    if guess>au:
        print("Guess lower ")
    else:
        print("Guess higher ")
    guess=int(input("Guess a number  "))
    count+=1

print("You are correct.")
print("You took ",count," attemps.")