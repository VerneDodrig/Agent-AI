import os
from .config import MAX_CHARACTERS

def get_files_info(working_directory, directory=None):
    full_path = os.path.abspath(os.path.join(working_directory, directory))

    if not full_path.startswith(os.path.abspath(os.path.join(".", working_directory))):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory | Directory Path: {full_path}, Prefix_Path: {os.path.abspath(os.path.join(".", working_directory))}'
    elif not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'
    
    path_contents = os.listdir(full_path)
    path_contents_list = []

    for file in path_contents:
        file_path = os.path.abspath(os.path.join(full_path, file))
        path_contents_list.append(f'- {file}: file_size={os.path.getsize(file_path)}, is_dir={os.path.isdir(file_path)}')

    path_content_string = "\n".join(path_contents_list)
    
    return path_content_string


def get_file_content(working_directory, file_path=None):
    full_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not full_path.startswith(os.path.abspath(os.path.join(".", working_directory))):
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory | Directory Path: {full_path}, Prefix_Path: {os.path.abspath(os.path.join(".", working_directory))}'
    elif not os.path.isfile(full_path):
        return f'Error: "{file_path}" is not a directory'
    
    with open(full_path, "r") as file_contents:
        file_content_string = file_contents.read(MAX_CHARACTERS)

        if len(file_content_string) == MAX_CHARACTERS:
            return f'{file_content_string}[...File "{file_path}" truncated at {MAX_CHARACTERS} characters]'

        return f'{file_content_string}'