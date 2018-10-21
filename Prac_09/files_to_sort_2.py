import os
import shutil

file_types = set()
custom_names = {}
os.chdir('FilesToSort')

for directory_name, directory_list, file_list in os.walk("."):
    for file in file_list:
        file_type = os.path.splitext(file)[1].strip(".")

        if file_type in file_types:
            shutil.move(file, custom_names[file_type])
        else:
            custom_name = input("What category would you like to sort {} files into? ".format(file_type))
            try:
                os.mkdir(custom_name)
            except FileExistsError:
                pass

            file_types.add(file_type)
            shutil.move(file, custom_name)
            custom_names["{}".format(file_type)] = custom_name
