import io
import os
import sys
import shutil

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
    files_in_folder = {}

    # create child folders
    for line in lines:
        s = ' --- '
        if s in line:
            # numbers leading with 0s to guarantee a sorted list
            i += 1
            folder_name = f"{str(i).zfill(leading_zeroes)} -- {line[line.index(s) + len(s) :-5]}"
            if not os.path.exists(folder_name):
                os.mkdir(folder_name)
        else:
            if line.strip() and '%%%' in line:
                files_in_folder[line.split(' ')[1]] = str(i).zfill(leading_zeroes)

    files_list = [each for each in os.listdir(dir_path) if each.endswith('.mp4')]
    print(files_list)
    print(files_in_folder)

    """
    #move the files to their folder
    try:
        for f in files_list:
            new_file_name = os.path.join()
            shutil.move(f, new_file_name)
    except:
        msg = msgs.MSG_550
    return msg
    """


if __name__ == '__main__':
    myfunction()