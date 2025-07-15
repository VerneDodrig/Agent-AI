from functions.get_files_info import get_files_info, get_file_content, write_file
from functions.run_python import run_python_file


#print(f'"Result for lorem.txt directory:\n"{write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")}"')
#print(f'"Result for pkg/morelorem.txt directory:\n"{write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")}"')
#print(f'"Result for /bin/cat directory:\n"{write_file("calculator", "/tmp/temp.txt", "this should not be allowed")}"')

print(f'"Result for main.py file:\n"{run_python_file("calculator", "main.py")}')
print(f'"Result for tests.py file:\n"{run_python_file("calculator", "tests.py")}')
print(f'"Result for tests.py file:\n"{run_python_file("calculator", "../main.py")}')
print(f'"Result for tests.py file:\n"{run_python_file("calculator", "nonexistent.py")}')