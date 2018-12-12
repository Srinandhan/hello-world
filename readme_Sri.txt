Automating the process of extraction and printing of keywords using Python

A python program to extract information from PDF documents that would then be input into databases or local spreadsheets was scripted. Three modules were majorly made use of in this endeavour: PyPDF2 (the first-line pdf extraction tool used in python), textract (specializes in OCR and can parse scanned images as well) and NLTK (natural Language Toolkit used in statistical natural language processing). 


Getting Started

Have Python program ready. Have sample PDF documents for testing as well.

Prerequisites

Python 3 and above preferred
Windows 7 and above preferred. Linux/iOS might have slightly different requirements

Installing

Install modules PyPDF2, textract, nltk
If any modules do not install, use package managers (pip comes with Python 3 and above)
If pip doesn't work install using Chocolatey
textract can be installed using easy-install 

Development of script (script uploaded as well)

Import the installed modules
Call required functions
Extract keywords and print to file

Testing
Break code at PyPDF2 and test if normal PDF with text is being extracted
Separate textract code and test if scanned PDF text is recognized
Test nltk functionality as well

Deployment

Using Python IDE/terminal call Python
Execute script