from functions.get_files_info import get_files_info, get_file_content, write_file


print(f'"Result for lorem.txt directory:\n"{write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")}"')
print(f'"Result for pkg/morelorem.txt directory:\n"{write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")}"')
print(f'"Result for /bin/cat directory:\n"{write_file("calculator", "/tmp/temp.txt", "this should not be allowed")}"')