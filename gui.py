from modules import functions
import PySimpleGUI as sg

# Title
label = sg.Text("Type in a to-do")

# Defining buttons in GUI
label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

# Placement of buttons
window = sg.Window("My To-Do App", layout=[[label], [input_box, add_button]])
window.read()
window.close()