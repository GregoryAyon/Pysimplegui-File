import PySimpleGUI as sg

def addFunc(num1, num2):
    return num1 + num2

sg.theme('DarkBrown')

layout = [[sg.Text('-----Add APP-----')],
        [sg.Text('Enter your 1st number:',size=(20,1)),sg.InputText(size=(20,1),key='in_1')],
        [sg.Text('Enter your 2nd number:',size=(20,1)),sg.InputText(size=(20,1), key='in_2')],
        [sg.Text('Output:')],
        [sg.Text('Output Here', key='-OUT-')],
        [sg.Button('Add'),sg.Button('Clear'), sg.Button('Exit')]]

window = sg.Window('Add Two Number', layout)

while True:
    event, values = window.read()
    if event == 'Exit' or event == sg.WIN_CLOSED:
        break
    if event == 'Add':
        num1 = int(values['in_1'])
        num2 = int(values['in_2'])
        result = addFunc(num1, num2)
        window['-OUT-'].update(result)

    if event == 'Clear':
        window['in_1'].update('')
        window['in_2'].update('')
        window['-OUT-'].update('Output Here')
        
    

window.close()