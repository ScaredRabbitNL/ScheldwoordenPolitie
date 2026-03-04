import os


def createDirectory(dir_name):
    try:
        os.mkdir(dir_name)
        print(f"Directory {dir_name} created successfully!")
    except FileExistsError:
        print(f"Directory '{dir_name}' already exists")
    except PermissionError:
        print(f"Permission denied: Unable to create '{dir_name}'.")
    except Exception as e:
        print(f"An error occurred: {e}")


def createFile(file_name : str, file_dir : str, file_contents : list[str], mode : str, encoding : str):
    if mode == None:
        mode = "w"
    if encoding == None:
        encoding = "utf-8"
    with open(file_dir + "/" + file_name, mode, encoding=encoding) as f:
        f.write(f"{file_contents}\n")

