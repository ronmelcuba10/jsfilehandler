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
                files_in_folder[line.split(' ')[1]] = [folder_name, line.split(' ', 1)[1].split('%%%')[0]]

    for k,v in files_in_folder.items():
        print(f' key {k} value {v}')

    #move the files to their folder
    files_list = [each for each in os.listdir(dir_path) if each.endswith('.mp4')]
    
    # change back to upper folder
    os.chdir('..')


    for f in files_list:
        key = f.split('.')[0]
        if key in files_in_folder:
            new_file_name = os.path.join(tut_folder, files_in_folder[key][0], files_in_folder[key][1] + '.mp4')
            print(new_file_name)
            shutil.move(f, new_file_name)


if __name__ == '__main__':
    myfunction()