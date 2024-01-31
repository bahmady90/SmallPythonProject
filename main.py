import functions
import time
time = f"{time.strftime("%c")}"
print(time)
while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + "\n")

        functions.write_todos(todos)

    elif user_action.startswith("show"):

        todos = functions.get_todos()

        new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(new_todos):
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("exit"):
        break

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter the new todo: ")
            todos[number] = new_todo + "\n"

            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):

        try:
            number = int(user_action[9:])
            todos = functions.get_todos()
            completed_todo = todos[number - 1].strip('\n')
            todos.pop(number - 1)
            functions.write_todos(todos)
            message = f"Todo {completed_todo} was removed from the list."
            print(message)
        except IndexError:
            print("The number of item doesn't exist.")
            continue

    else:
        print("The Input is wrong.")

print("bye!")
