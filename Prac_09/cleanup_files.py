"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import os


def demo_walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        for filename in filenames:
            current_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, get_fixed_filename(filename))
            os.rename(current_name, new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    temp_name = ""
    for i, character in enumerate(filename):

        if i == 0:
            if character.islower():
                temp_name += character.upper()
            else:
                temp_name += character
        elif character.isupper():
            temp_name += "_"
            temp_name += character
        else:
            temp_name += character
    print(temp_name)
    temp_name.replace(" ", "_").replace(".TXT", ".txt")
    return temp_name


demo_walk()
