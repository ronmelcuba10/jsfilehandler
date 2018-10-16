import io
import os
import sys

def myfunction():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, 'tut.txt')

    tut_file = open(file_path,'r')
    lines = tut_file.readlines()

    # make main folder
    tut_name = lines[0].strip().replace(':', ' ')
    tut_folder = os.path.join(dir_path, tut_name)
    if not os.path.exists(tut_folder):
        os.mkdir(tut_name)

    # movr to the new folder
    if (os.path.isdir(tut_folder)):
        os.chdir(tut_folder)

    # create child folders
    for line in lines:
        if '---' in line:
            os.mkdir(line[5:-5])


if __name__ == '__main__':
    myfunction()