
import PyPDF2

pdfFileObj = open('.\\files\\encrypted.pdf', 'rb')
file = PyPDF2.PdfFileReader(pdfFileObj)

fileDict = open('.\\files\\dictionary.txt')
dictionary = fileDict.readlines()

for word in dictionary:
    word = word.strip()
    if file.decrypt(word) == 1:
        print('Password is ', word)
        break
    if file.decrypt(word.lower()) == 1:
        print('Password is ', word)
        break

pdfFileObj.close()
fileDict.close()
