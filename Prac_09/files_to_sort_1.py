import os
import shutil

file_types = set()
os.chdir('FilesToSort')

for directory_name, directory_list, file_list in os.walk("."):

    for file in file_list:
        file_type = os.path.splitext(file)[1].strip(".")

        if file_type in file_types:
            shutil.move(file, file_type)
        else:
            try:
                os.mkdir(file_type)
            except FileExistsError:
                pass

            file_types.add(file_type)
            shutil.move(file, file_type)
