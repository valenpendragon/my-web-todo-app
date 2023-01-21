import os
FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Reads a text file and returns a list of to-so items
    (strings). It creates an empty file if it is not present.
    """
    if not os.path.exists(FILEPATH):
        with open(FILEPATH, 'w') as file_local:
            pass
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Writes a list of to-do items (strings) to a text file on disk.
    It will overwrite the destination file.
    """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)
    return


if __name__ == "__main__":
    print("Function testing")
    print(get_todos())