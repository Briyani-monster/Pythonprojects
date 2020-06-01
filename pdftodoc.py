#converts text pdf file into docx file 

import webbrowser
import sys
import pyperclip
import PyPDF2
import docx
if len(sys.argv)>1:
    #Get address from command line
    address=''.join(sys.argv[1:])
else:
    #Get address from clipbord
    address=pyperclip.paste()
pdffileobj=open(address,'rb')
pdfReader=PyPDF2.PdfFileReader(pdffileobj)
num_of_pages=pdfReader.numPages
print('creating your file...........')
doc=docx.Document()
print('converting your file...........')
for i in range(num_of_pages):
    pageObj=pdfReader.getPage(i)
    text=pageObj.extractText()
    doc.add_paragraph(text)
print('saving your file as convertedfile.docx......')    
doc.save('C:/Users/G S ASHISH\Desktop/convertedfile.docx')
print('all done!!!\nyour file is converted!!')


