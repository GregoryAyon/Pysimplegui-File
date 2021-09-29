import PySimpleGUI as sg

def addFunc(num1, num2):
    return num1 + num2

sg.theme('DarkBrown')

layout = [[sg.Text('-----Add APP-----')],
        [sg.Text('Enter your 1st number:'),sg.InputText()],
        [sg.Text('Enter your 2nd number:'),sg.InputText()],
        [sg.Text('Output:')],
        [sg.Text('Output Here', key='-OUT-')],
        [sg.Button('Add'), sg.Button('Exit')]]

window = sg.Window('Add Two Number', layout)

while True:
    event, values = window.read()
    if event == 'Exit' or event == sg.WIN_CLOSED:
        break
    if event == 'Add':
        num1 = int(values[0])
        num2 = int(values[1])
        result = addFunc(num1, num2)
        window['-OUT-'].update(result)
    

window.close()