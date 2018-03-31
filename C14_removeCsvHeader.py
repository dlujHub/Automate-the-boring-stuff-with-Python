#! python3
# removeCsvHeader.py - Removes the header from all CSV files in the current
# working directory.

import os
import csv

os.makedirs('headerRemoved', exist_ok=True)

# Loop through every file in the current working directory.
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue  #skip

    print('Removing header from ' + csvFilename + '...')

    # Read the CSV file in (skipping first row).
    csvRows = []
    csvFIleObj = open(csvFilename)
    readerObj = csv.reader(csvFIleObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue
        csvRows.append(row)
    csvFIleObj.close()

    # Write out the CSV file.
    csvFIleObj = open(os.path.join('headerRemoved', csvFilename), 'w', newline='')
    csvWriter = csv.writer(csvFIleObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFIleObj.close()
