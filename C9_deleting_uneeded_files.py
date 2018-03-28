"""
Program that walks through a folder tree and searches for exceptionally
large files or folders—say, ones that have a file size of more than
100MB.

"""

import os


def delete_files(folder):
    folder = os.path.abspath(folder)

    for folder, subfolders, files in os.walk(folder):
        for filename in files:
            file_size = os.path.getsize(os.path.join(folder, filename))
            if file_size < 10000000:
                continue
            # os.unlink(filename)
            print("Deleting " + filename + "... with size " + str(file_size))


delete_files(".\\files")
