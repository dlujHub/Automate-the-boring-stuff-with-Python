"""
Program that walks through a folder tree and searches for files with
a certain file extension (.txt). Copy these files from whatever
location they are in to a new folder.

"""

import os
import shutil


def selective_copy(folder, ext):
    """
    Perform selective copy of all files in folder tree, that has specified extension.

    :param folder: Folder tree to be copied
    :param ext: File extension that will be copied
    """
    os.chdir(folder)
    if not os.path.exists('..\\new_dir'):
        os.makedirs('..\\new_dir')

    for folder_name, subfolders, filenames in os.walk('.'):
        for filename in filenames:
            if not filename.endswith(ext):
                continue
            file_path = os.path.join(os.path.abspath(folder_name), filename)
            shutil.copy(file_path, '..\\new_dir\\')


selective_copy('.\\files\\', '.txt')
