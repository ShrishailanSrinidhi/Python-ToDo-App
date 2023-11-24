def get_todos():
    with open('todos.txt', 'r') as file:
        todos_local = file.readlines()
    return todos_local

while True:
    # Get choice from user whether user wants to add new item, show the list or exit the program
    user_action = input("Type add, show, edit, complete or exit: ")

    # Remove any spaces in choice i.e. to make add == add(space)
    user_action = user_action.strip()

    # Depeding on user choice add, show or exit program
    if user_action.startswith("add"):
            todo = user_action[4:]

            todos = get_todos()

            todos.append(todo + '\n')

            with open('todos.txt', 'w') as file:
                todos = file.writelines(todos)

    elif user_action.startswith("show"):
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos = get_todos()
            
            for index, items in enumerate(todos):
                items = items.strip("\n")
                row = f"{index+1}-{items}"
                print(row)
    elif user_action.startswith("edit"):
            try:
                number = int(user_action[5:])
                number = number-1

                todos = get_todos()

                new_todo = input("Enter new To-Do item: ")
                todos[number] = new_todo + '\n'

                with open('todos.txt', 'w') as file:
                    todos = file.writelines(todos)
            except ValueError:
                 print("Your command is not valid.")
                 continue

    elif user_action.startswith("complete"):
            try:
                number = int(user_action[9:])

                todos = get_todos()
                index = number - 1
                todo_to_remove = todos[index].strip('\n')
                todos.pop(index)

                with open('todos.txt', 'w') as file:
                    todos = file.writelines(todos)
                message = f"Todo {todo_to_remove} was removed from the list."
                print(message)
            except IndexError:
                 print("There is no item with that number.")
                 continue

    elif user_action.startswith("exit"):
            break
    
    else:
         print("This command is not valid !")
    
    
print("Bye!")
