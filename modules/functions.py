def get_todos(filepath="todos.txt"):
    """Read a text file and return the list of 
    to-do items.
    """
    with open('todos.txt', 'r') as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(todos_arg, filepath="todos.txt"):
    """Write the to-do items in the text file.
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)