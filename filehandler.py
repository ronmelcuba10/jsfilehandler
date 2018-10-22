import io
import os
import sys
import shutil


FILE_NAME = 'tut.txt'
TITLE_DESIGNATOR = '#####'
NOTHING = ''
SPACE = ' '
COLON = ':'
INTERROGATION = '?'
SLASH = '/'
THREE_DASHES = ' --- '
FOLDER_INDEX_SEPARATOR = '%%%'
EXTENSION = '.txt'

def clearName(name):
    return name.replace(COLON, SPACE).replace(INTERROGATION, NOTHING).replace(SLASH, NOTHING)

def unordered_file(f):
    return f.strip()[:-1] != ')'

def files_need_order(list):
    # return true if any of the files names is followed by a number
    return any( unordered_file(f) for f in list) 

def reorder_files(list):
    index = 1
    #for f in list:
    #    if unordered_file(f):
    list.sort()
    new_list = []
    for f in list:
        #print(f)
        if f == 'tut.txt':
            continue
         
        new_name = 'new (' + str(index) + ')' + EXTENSION
        try:
            os.rename(f, new_name)
            index += 1
        except:
            return None
        new_list.append(new_name)
        #print(new_name)
    return new_list
        
            

def make_new_folder(dir_path, tut_name):
    tut_folder = os.path.join(dir_path, tut_name)
    if not os.path.exists(tut_folder):
        os.mkdir(tut_name)
    return tut_folder


def myfunction():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, FILE_NAME)

    tut_file = open(file_path,'r')
    lines = tut_file.readlines()

    # make main folder
    tut_name = clearName(lines[0].strip()).replace( TITLE_DESIGNATOR, NOTHING)
    tut_folder = make_new_folder(dir_path, tut_name)
    
    # move to the new folder
    if (os.path.isdir(tut_folder)):
        os.chdir(tut_folder)

    # if less than 100 add one or two leading zeros
    leading_zeroes = len( str( len(lines) ) )
    i = 0
    files_in_folder = {}

    # create child folders
    for line in lines:
        if THREE_DASHES in line:
            # numbers leading with 0s to guarantee a sorted list
            i += 1
            folder_name = f'{str(i).zfill(leading_zeroes)} -- {line[line.index(THREE_DASHES) + len(THREE_DASHES) :-5]}'
            if not os.path.exists(folder_name):
                os.mkdir(folder_name)
        else:
            if line.strip() and FOLDER_INDEX_SEPARATOR in line:
                files_in_folder[line.split(SPACE)[1]] = [clearName(folder_name), clearName(line.strip()).split(' ', 1)[1].split(FOLDER_INDEX_SEPARATOR)[0].split(' ',1)[1]]

    
    #for k,v in files_in_folder.items():
    #    print(f' key {k} value {v}')

    #move the files to their folder
    files_list = [each for each in os.listdir(dir_path) if each.endswith(EXTENSION)]
    
    # change back to upper folder
    os.chdir('..')

    #print(files_list)

    #print(files_need_order(files_list))
    if files_need_order(files_list):
        files_list = reorder_files(files_list)
        if not files_list:
            print('Error renaming files')
            return 
    
    # moving files to their subfolders by its names
    for f in files_list:
        key = f.split('.')[0]
        idx = f[f.find('(') + 1 : f.find(')')]
        if idx in files_in_folder:
    #        print(files_in_folder[idx][1].strip() + EXTENSION)
            new_file_name = os.path.join(tut_folder.strip(), files_in_folder[idx][0].strip(), files_in_folder[idx][1].strip() + EXTENSION)
    #        print(new_file_name)
            shutil.move(f, new_file_name)
    

if __name__ == '__main__':
    myfunction()
