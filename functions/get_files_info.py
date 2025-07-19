import os
from .config import MAX_CHARACTERS
from google.genai import types

def get_files_info(working_directory, directory=None):
    full_path = os.path.abspath(os.path.join(working_directory, directory))

    if not full_path.startswith(os.path.abspath(os.path.join(".", working_directory))):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
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
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
    elif not os.path.isfile(full_path):
        return f'Error: "{file_path}" is not a file'
    
    try:
        with open(full_path, "r") as file_contents:
            file_content_string = file_contents.read(MAX_CHARACTERS)

            if len(file_content_string) == MAX_CHARACTERS:
                return f'{file_content_string}[...File "{file_path}" truncated at {MAX_CHARACTERS} characters]'

            return f'{file_content_string}'
    except:
        return f'Error: Unable to open file {file_path} at {full_path}'


def write_file(working_directory, file_path, content):
    full_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not full_path.startswith(os.path.abspath(os.path.join(".", working_directory))):
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'

    directory_path = os.path.dirname(full_path)

    try:
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
    except:
        return f'Error: Unable to create directory {directory_path}'
    
    try:
        with open(full_path, "w") as file_to_write:
            file_to_write.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: Unable to write to {content} to {file_path}.'


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads the contents of a file up to 10000 characters",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to read from, relative to the working directory.",
            ),
        },
    ),
)


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes or overwrites a file with a given string of content.  If a file does not exist, this will create that file and write to that file with the given content string.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to write to, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write into the chosen file.",
            ),
        },
    ),
)