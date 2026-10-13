#Develop a game where the program randomly selects a number, and the user has
#to guess it. Provide feedback if the guess is too high or too low. This project helps
#you understand loops and conditional statements. 

import random

randomnum = random.randint(0,100)
num = 0

while num != randomnum:
    num = int(input("Guess the number: "))
    if num > randomnum:
        print("Too big!")
        continue
    else:
        print("Too small!")
        continue

if num == randomnum:
    print("Correct!")