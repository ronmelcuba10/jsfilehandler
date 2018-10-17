import io
import os
import sys

def myfunction():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, 'tut.txt')

    tut_file = open(file_path,'r')
    lines = tut_file.readlines()

    # make main folder
    tut_name = lines[0].strip().replace(':', ' ').replace('#####','')
    tut_folder = os.path.join(dir_path, tut_name)
    if not os.path.exists(tut_folder):
        os.mkdir(tut_name)

    # move to the new folder
    if (os.path.isdir(tut_folder)):
        os.chdir(tut_folder)

    # if less than 100 add one or two leading zeros
    leading_zeroes = len( str( len(lines) ) )
    i = 0

    # create child folders
    for line in lines:
        s = ' --- '
        if s in line:
            i += 1
            # numbers leading with 0s to guarantee a sorted list
            os.mkdir(f'{str(i).zfill(2)} -- {line[line.index(s) + len(s) :-5]}')


if __name__ == '__main__':
    myfunction()