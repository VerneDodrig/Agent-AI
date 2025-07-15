import os
import subprocess

def run_python_file(working_directory, file_path):
    full_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not full_path.startswith(os.path.abspath(os.path.join(".", working_directory))):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory | Directory Path: {full_path}, Prefix_Path: {os.path.abspath(os.path.join(".", working_directory))}'
    elif not os.path.exists(full_path):
        return f'File "{file_path}" not found.'
    elif file_path.split(".")[-1] != "py":
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        python_result = subprocess.run(["python3", full_path], capture_output=True, cwd=os.path.abspath(working_directory), timeout=30, check=True, text=True)

        if python_result.returncode != 0:
            return f'STDOUT: {python_result.stdout}\nSTDERR: {python_result.stderr}\nProcess exited with code {python_result.returncode}\n'
        elif python_result.stdout == None:
            return f'No output produced.'

        return f'STDOUT: {python_result.stdout}\nSTDERR: {python_result.stderr}\n'
    except Exception as e:
        return f'Error: executing Python file: {e}'