import PySimpleGUI as sg

# Read feet from user
feet_label = sg.Text("Enter feet: ")
feet_input = sg.Input()

# Read inches from user
inches_label = sg.Text("Enter inches: ")
inches_input = sg.Input()

# Define convert button
button = sg.Button("Convert")

# Window placement
window = sg.Window("Convertor",
                   layout=[[feet_label, feet_input],
                           [inches_label, inches_input],
                           [button]])

window.read()
window.close()