import functions
import PySimpleGUI

label = PySimpleGUI.Text("Type in a to-do")
input_box = PySimpleGUI.InputText(tooltip="Enter a todo", key="todo")
add_button = PySimpleGUI.Button("Add")
edit_button = PySimpleGUI.Button("Edit")
complete_button = PySimpleGUI.Button("Complete")
exit_button = PySimpleGUI.Button("Exit")
list_box = PySimpleGUI.Listbox(values=functions.get_todos(),
                               key="todos",enable_events=True, size=[45, 10])

window = PySimpleGUI.Window("My to-Do-App",
                            layout=[[label,], [input_box, add_button]
                            , [list_box, edit_button, complete_button], [exit_button]],
                            font=("abc", 15))
while True:
    event, values = window.read()
    print(1,event)
    print(2,values)
    print(3,values["todos"])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"]

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + "\n"
            functions.write_todos(todos)
            window["todos"].update(values=todos)

        case "Complete":
            todo_to_complete = values["todos"][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)

            functions.write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value="")

        case "todos":
            window["todo"].update(value=values["todos"][0])

        case PySimpleGUI.WINDOW_CLOSED:
            break
        case "Exit":
            break


print("bye")
window.close()