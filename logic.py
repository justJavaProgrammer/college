import PySimpleGUI as sg

from NumberGuesser import NumberGuesser

sg.theme('DarkAmber')  # Add a touch of color
# All the stuff inside your window.
layout = [[sg.Text('Number guesser')],
          [sg.Text('Enter your guess'), sg.InputText()],
          [sg.Text(key="guess_result")],
          [sg.Button('Ok'), sg.Button('Cancel')]]

# Create the Window
window = sg.Window('Number Guesser by Odeyalooo', layout)

guesser = NumberGuesser()

guesser.generateRandomNumber()


def start():
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

        result, message = guesser.checkNumber(userGuess)
        if result:
            sg.popup_animated(message=message,
                              image_source="happy-smile.gif", time_between_frames=10, title="You won!")

        else:
            window["guess_result"].update(message)


def close():
    window.close()
