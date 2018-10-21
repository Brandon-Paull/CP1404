import os
import shutil

os.chdir('FilesToSort')
print(os.getcwd())


for directory_name, directory_list, file_list in os.walk("."):
    print(directory_name)
    for file in file_list:
        print(file)
        shutil.move(file, 'FilesToSort')
