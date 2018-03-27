"""
Remove the zeros from files such as spam0042.txt

"""

import os
import re

zeros_regex = re.compile(r'0')
os.chdir(".\\files\\c9_remove_zeros\\")

for folderName, subfolders, filenames in os.walk('.'):

    for filename in filenames:
        if zeros_regex.search(filename):
            filename_new = zeros_regex.sub('', filename)
            abs_path = os.path.abspath(folderName)
            os.rename(os.path.join(abs_path, filename), os.path.join(abs_path, filename_new))

