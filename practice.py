import random as randomizer

print('Hello, you need to guess the number between 0 and 100')

randomInteger = randomizer.randint(0, 100)
userProbe = None
numberOfAttempts = 0

while randomInteger != userProbe:
    userProbe = int(input("Input your guess: "))

    if randomInteger < userProbe:
        print("Random number is smaller!")
    if randomInteger > userProbe:
        print("Random number is greater!")
    numberOfAttempts += 1

print("You won! Number of attempts: " + str(numberOfAttempts))