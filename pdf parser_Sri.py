#!usr/bin/env python
import PyPDF2
import textract

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

filename = 'filetobeparsed.pdf'
pdfFileObj = open(filename,'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
#The pdfReader variable is a readable object that will be parsed
#discerning the number of pages will allow parsing through all 
#the pages
num_pages = pdfReader.numPages
count = 0
text = ""
while count < num_pages:
	pageObj = pdfReader.getPage(count)
	count += 1
	text += pageObj.extractText()

#This if statement exists to check if the above library returned #words. It's done because PyPDF2 cannot read scanned files.

if text != "":
   text = text

#If the above returns as False, we run the textract to #convert scanned/image based PDF files into text (Optical Character Recognition)

else:
	text = textract.process(fileurl, method='tesseract', language='eng')
 
tokens = word_tokenize(text)

#creating a new list that contains punctuations, to be cleaned
punctuations = ['(',')',';',':','[',']',',']

#Initializing the stopwords variable which is a list of words like #"The", "I", "and", etc. that don't hold much value as keywords

stop_words = stopwords.words('english')

#keywords list that returns only a list of words NOT IN stop_words and NOT IN punctuations.

keywords = [word for word in tokens if not word in stop_words and not word in punctuations]
print(keywords, file=open('newparse.xls','w'))
