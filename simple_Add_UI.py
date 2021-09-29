import PySimpleGUI as sg

def addFunc(num1, num2):
    return num1 + num2

def subFunc(num1, num2):
    return num1 - num2

def mulFunc(num1, num2):
    return num1 * num2

def devFunc(num1, num2):
    return num1 / num2

sg.theme('DarkTeal11')

layout = [[sg.Text('--------------------------------------------Basic Calulator APP-----')],
        [sg.Text('Enter your 1st number:',size=(20,1)),sg.InputText(size=(20,1),key='in_1')],
        [sg.Text('Enter your 2nd number:',size=(20,1)),sg.InputText(size=(20,1), key='in_2')],
        [sg.Text('Answer:')],
        [sg.Text('Answer Here', key='-OUT-')],
        [sg.Button('Sum'), sg.Button('Sub'), sg.Button('Mul'), sg.Button('Dev'),sg.Button('Clear'), sg.Button('Exit')]]

window = sg.Window('Basic App', layout)

while True:
    event, values = window.read()
    if event == 'Exit' or event == sg.WIN_CLOSED:
        break
    if event == 'Sum':
        num1 = int(values['in_1'])
        num2 = int(values['in_2'])
        result = addFunc(num1, num2)
        window['-OUT-'].update(result)

    if event == 'Sub':
        num1 = int(values['in_1'])
        num2 = int(values['in_2'])
        result = subFunc(num1, num2)
        window['-OUT-'].update(result)

    if event == 'Mul':
        num1 = int(values['in_1'])
        num2 = int(values['in_2'])
        result = mulFunc(num1, num2)
        window['-OUT-'].update(result)
    
    if event == 'Dev':
        num1 = int(values['in_1'])
        num2 = int(values['in_2'])
        result = devFunc(num1, num2)
        window['-OUT-'].update(result)

    if event == 'Clear':
        window['in_1'].update('')
        window['in_2'].update('')
        window['-OUT-'].update('Answer Here')
        
    

window.close()