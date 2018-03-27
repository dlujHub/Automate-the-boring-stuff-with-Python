"""
If no other arguments are passed other than the string to
strip, then whitespace characters will be removed from the beginning and
end of the string.
Otherwise, the characters specified in the second argument
to the function will be removed from the string.

"""

import re


def remove_spaces(string):
    start = re.compile(r'^\s*')
    end = re.compile(r'\s*$')
    string = start.sub('', string)
    string = end.sub('', string)
    return string


s = "    this is a string     "

print("This is what I have for you:")
print(remove_spaces(s))
