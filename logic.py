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
    print(randomInteger)
    numberOfAttempts = 0

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break
        # Added the logic to check if the number is number
        if not values[0].isnumeric():
            sg.popup("input the number!")
            continue

        userGuess = int(values[0])

        if randomInteger == userGuess:
            sg.popup_animated(message="You won! Number of attempts: " + str(numberOfAttempts), image_source="happy-smile.gif"
                              , time_between_frames=10, title="You won!")

        if randomInteger < userGuess:
            window["guess_result"].update("Random number is smaller!")
        if randomInteger > userGuess:
            window["guess_result"].update("Random number is greater!")
        numberOfAttempts += 1


def close():
    window.close()
