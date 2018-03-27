"""
Write a program that opens all .txt files in a folder and searches for any
line that matches a user-supplied regular expression. The results should
be printed to the screen.

"""
import os
import re

dir_files = os.listdir('.\\files\\c8_dir')
print('What text do you want to search for?')
user_regex = re.compile(str(input()))
file_regex = re.compile(r'\w+\.txt$')

for i in range(len(dir_files)):
    if file_regex.match(dir_files[i]):
        file = open('.\\files\\c8_dir\\' + dir_files[i])
        content = file.readlines()
        for line in range(len(content)):

            if user_regex.search(content[line]):
                print(content[line])
        file.close()
