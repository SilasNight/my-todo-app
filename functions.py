def get_todos():
    with open('todo.txt', 'r') as file_local:
        todo_local = file_local.readlines()
    return todo_local
def write_todos(to_write):
    with open('todo.txt', 'w') as file_local:
        file_local.writelines(to_write)