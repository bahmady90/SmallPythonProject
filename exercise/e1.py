import PySimpleGUI as sg
import converters

sg.theme("Black")
enter_feet = sg.Text("Enter feet:")
input_feet = sg.Input(key="feet")

enter_inches = sg.Text("Enter Inches:")
input_inches = sg.Input(key="inches")

convert_button = sg.Button("Convert")
exit_button = sg.Button("Exit")
output_label = sg.Text("",
                               key="output")

window = sg.Window("Convertor",
                            layout=[[enter_feet, input_feet],
                                                 [enter_inches, input_inches],
                                                 [convert_button, exit_button, output_label]])


while True:

    event, values = window.read()

    match event:
        case "Convert":
            value_feet = float(values["feet"])
            value_inches = float(values["inches"])
            value_meters = converters.convert(value_feet, value_inches)
            print(value_meters)
            window["output"].update(value=f"{value_meters} m", text_color="white")
        case sg.WINDOW_CLOSED:
            break
        case "Exit":
            break


window.close()
