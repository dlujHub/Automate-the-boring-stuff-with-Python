"""
Say your boss emails you thousands of files with American-style dates
(MM-DD-YYYY) in their names and needs them renamed to Europeanstyle
dates (DD-MM-YYYY). This boring task could take all day to do by
hand! Let’s write a program to do it instead.
Here’s what the program does:
• It searches all the filenames in the current working directory for
American-style dates.
• When one is found, it renames the file with the month and day swapped
to make it European-style.

"""

import os
import re
import shutil

# Create a regex that matches files with the American date format.
date_pattern = re.compile(r"""^(.*?)
(([01])?\d)-  # one or two digits for the month
(([0123])?\d)- # one or two digits for the day
((19|20)\d\d) # four digits for the year
(.*?)$       # all text after the date
""", re.VERBOSE)

# Loop over the files in the working directory.
os.chdir('.\\files\\c9_dates')
for amer_filename in os.listdir('.'):
    mo = date_pattern.search(amer_filename)

    # Skip files without a date.
    if mo is None:
        continue

    # Get the different parts of the filename.
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # Form the European-style filename.
    euro_filename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    # Get the full, absolute file paths.
    abs_working_dir = os.path.abspath('.')
    amer_filename = os.path.join(abs_working_dir, amer_filename)
    euro_filename = os.path.join(abs_working_dir, euro_filename)

    # Rename the files.
    shutil.move(amer_filename, euro_filename)
