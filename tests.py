from functions.get_files_info import get_files_info, get_file_content

try:
    print(f'"Result for lorem.txt directory:\n"{get_file_content("calculator", "lorem.txt")}"')
    print(f'"Result for main.py directory:\n"{get_file_content("calculator", "main.py")}"')
    print(f'"Result for pkg/calculator.py directory:\n"{get_file_content("calculator", "pkg/calculator.py")}"')
    print(f'"Result for /bin/cat directory:\n"{get_file_content("calculator", "/bin/cat")}"')
except Exception as e:
    print(f'Error: {e}')