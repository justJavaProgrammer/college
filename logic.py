import PySimpleGUI as sg
import random as randomizer

sg.theme('DarkAmber')  # Add a touch of color
# All the stuff inside your window.
layout = [[sg.Text('Number guesser')],
          [sg.Text('Enter your guess'), sg.InputText()],
          [sg.Text(key="guess_result")],
          [sg.Button('Ok'), sg.Button('Cancel')]]

# Create the Window
window = sg.Window('Number Guesser by Odeyalooo', layout)


def start():
    randomInteger = randomizer.randint(0, 100)

    userProbe = None
    numberOfAttempts = 0

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break

        userGuess = int(values[0])

        if randomInteger == userGuess:
            sg.popup("You won! Number of attempts: " + str(numberOfAttempts))

        if randomInteger < userGuess:
            window["guess_result"].update("Random number is smaller!")
        if randomInteger > userGuess:
            window["guess_result"].update("Random number is greater!")
        numberOfAttempts += 1


def close():
    window.close()
