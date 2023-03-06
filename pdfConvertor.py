from PyPDF2 import PdfReader
 
# creating a pdf reader object
reader = PdfReader('Phillip_K._Dick_-_Do_Androids_Dream_of_Electric_Sheep.pdf')
 
# printing number of pages in pdf file
print(len(reader.pages))
 
# getting a specific page from the pdf file
page = reader.pages[2]
 
# extracting text from page
text = page.extract_text()
print(text)