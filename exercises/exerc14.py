import PySimpleGUI as sg
from converters8 import convert

feet_label = sg.Text("Enter feet:")
feet_input = sg.Input(key="feets")

inches_label = sg.Text("Enter inches:")
inches_input = sg.Input(key="inches")

button = sg.Button("Convert")
result_label = sg.Text(key="result")

window = sg.Window("Converter",
                   layout=[[feet_label, feet_input],
                           [inches_label, inches_input],
                           [button, result_label]])

while True:
    event, values = window.read()
    feets = float(values["feets"])
    inches = float(values["inches"])
    meters = convert(feets, inches)
    window["result"].update(value=f"{meters:.3f} m")

window.close()
