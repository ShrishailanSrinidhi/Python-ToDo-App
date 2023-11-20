while True:
    # Get choice from user whether user wants to add new item, show the list or exit the program
    user_action = input("Type add, show, edit, complete or exit: ")

    # Remove any spaces in choice i.e. to make add == add(space)
    user_action = user_action.strip()

    # Depeding on user choice add, show or exit program
    if 'add' in user_action or 'new' in user_action:
            todo = user_action[4:]

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('todos.txt', 'w') as file:
                todos = file.writelines(todos)

    elif 'show' in user_action:
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            
            for index, items in enumerate(todos):
                items = items.strip("\n")
                row = f"{index+1}-{items}"
                print(row)
    elif 'edit' in user_action:
            number = int(user_action[5:])
            number = number-1

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter new To-Do item: ")
            todos[number] = new_todo + '\n'

            with open('todos.txt', 'w') as file:
                todos = file.writelines(todos)

    elif 'complete' in user_action:
            number = int(user_action[9:])

            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('todos.txt', 'w') as file:
                todos = file.writelines(todos)
            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)

    elif 'exit' in user_action:
            break
    
    else:
         print("This command is not valid !")
    
    
print("Bye!")
