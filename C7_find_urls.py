"""
Find website URLs that begin with http:// or https://.

"""

import pyperclip
import re

url_regex = re.compile('''(
(http:|https:)//
[a-zA-z0-9-/.#_]{4,}
)''', re.VERBOSE)

text = pyperclip.paste()
urls = url_regex.findall(text)
for groups in url_regex.findall(text):
    print(groups[0])
