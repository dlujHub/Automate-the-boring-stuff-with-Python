# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

import os
import zipfile


def backup_to_zip(folder):
    # Backup the entire contents of "folder" into a ZIP file.
    folder = os.path.abspath(folder)

    # Figure out the filename this code should use based on
    # what files already exist.
    number = 1
    while True:
        zip_file_name = os.path.basename(folder) + "_" + str(number) + ".zip"
        if not os.path.exists(zip_file_name):
            break
        number += 1

    # Create the ZIP file.
    print("Creating %s..." % zip_file_name)
    backup_zip = zipfile.ZipFile(zip_file_name, 'w')

    # Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print("Adding files in %s..." % foldername)
        # Add the current folder to the ZIP file.
        backup_zip.write(foldername)

        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backup_zip.write(os.path.join(foldername, filename))
    backup_zip.close()
    print('Done!')


backup_to_zip(".\\files\\C9_backup")
