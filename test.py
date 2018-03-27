import os
import zipfile

os.chdir('.\\files')
zip = zipfile.ZipFile('new.zip', 'w')
zip.write('file.txt', compress_type=zipfile.ZIP_DEFLATED)


zip.close()
