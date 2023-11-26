import random as randomizer


class NumberGuesser:
    numberOfAttempts = 0
    expectedNumber = -1

    def generateRandomNumber(self):
        self.expectedNumber = randomizer.randint(0, 100)

    def checkNumber(self, userGuess):
        self.numberOfAttempts += 1

        if self.expectedNumber == userGuess:
            return True, "Correct! Number of attempts: " + str(self.numberOfAttempts)

        if self.expectedNumber < userGuess:
            return False, "Random number is smaller!"
        if self.expectedNumber > userGuess:
            return False, "Random number is greater!"

    def getNumberOfAttempts(self):
        return self.numberOfAttempts