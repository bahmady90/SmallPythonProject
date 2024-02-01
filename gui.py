import functions
import PySimpleGUI

label = PySimpleGUI.Text("Type in a to-do")
input_box = PySimpleGUI.InputText()
add_button = PySimpleGUI.Button("Add")

window = PySimpleGUI.Window("My to-Do-App", layout=[[label,],[input_box, add_button]])
window.read()
window.close()