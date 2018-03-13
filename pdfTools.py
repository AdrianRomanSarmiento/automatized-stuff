#! python3
# pdfTools.py - Rotates, combines and reorders PDF files
# Functions: rotation - Rotates 90, 180 or 270 degrees (clockwise) a specific page of a PDF. The output file is only the rotated page.
#            rotation2 - Clockwise rotates a specific page of a PDF. The output file is the original file but with the rotated page in the same position.
#            combination - Merges specific pages of PDF documents into a single PDF file
#            reorder - Reorders the pages of a PDF file in a desired order. Can be used to extract one page of a PDF file.


import PyPDF2

def rotation(filename, pdfpage, degrees, outputname):
    originalFile = open(filename, "rb")             #Opens the file, it must be in the working directory
    pdfReader = PyPDF2.PdfFileReader(originalFile)  #Reads the file
    page = pdfReader.getPage(pdfpage-1)             #Page you want to rotate. Starts with 0, so we substract one to the input.
    page.rotateClockwise(degrees)                   #Degrees you want to rotate
    #Save and close the documents
    pdfWriter = PyPDF2.PdfFileWriter()
    pdfWriter.addPage(page)
    resultFile = open(outputname, "wb")             #Creates a new PDF
    pdfWriter.write(resultFile)                     #Writes the content (only the rotated page)
    resultFile.close()                              #Closes the output file
    originalFile.close()                            #Closes the original file
    print("Done, the page number %s was rotated and saved as %s" % (pdfpage, outputname))
    
def rotation2(filename, pdfpage, degrees, outputname): 
    originalFile = open(filename, "rb")             #Opens the file, it must be in the working directory
    pdfReader = PyPDF2.PdfFileReader(originalFile)  #Reads the file
    pdfWriter = PyPDF2.PdfFileWriter()
    for pageNum in range(0, pdfReader.numPages):    #Loops through the pages and saves them. Rotates the page specified by the user
        if pageNum == pdfpage-1:
            page = pdfReader.getPage(pdfpage-1)
            page.rotateClockwise(degrees)
            pdfWriter.addPage(page)
        else:
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)
    resultFile = open(outputname, "wb")             #Creates a new PDF
    pdfWriter.write(resultFile)                     #Writes the content
    resultFile.close()                              #Closes the output file
    originalFile.close()                            #Closes the original file
    print("Done, the page number %s was rotated and %s was created" % (pdfpage, outputname))
    
def combination(pdflist, outputname):
    pdfWriter = PyPDF2.PdfFileWriter()
    #Opens the files, they must be in the working directory
    for filename in pdflist:
        pdfFileObj = open(filename, "rb")           
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        #Loop through the pages you want to add
        for pageNum in range(pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)
    #Save and close the resulting PDF
    pdfOutput = open(outputname,"wb")
    pdfWriter.write(pdfOutput)
    pdfOutput.close()
    print("Done, %s was created" % (outputname))

def reorder(filename, pagelist, outputname):
    #Opens and reads the file. It must be in the working directory
    originalFile = open(filename, "rb")
    pdfReader = PyPDF2.PdfFileReader(originalFile)
    #Loops through the file selecting the desired pages
    pdfWriter = PyPDF2.PdfFileWriter()
    for page in pagelist:
        pageObj = pdfReader.getPage(page-1)
        pdfWriter.addPage(pageObj)
    #Saves the pages in a new PDF and closes it
    resultFile = open(outputname,"wb")
    pdfWriter.write(resultFile)
    resultFile.close()
    originalFile.close()
    print("Done, %s was created" % (outputname))
    
#Examples of usage of each function.        
rotation("example.pdf", 1, 90, "output.pdf")
rotation2("example.pdf", 1, 90, "output.pdf")
combination(["example_1.pdf", "example_2.pdf","example_3.pdf"],"output.pdf")
reorder("example.pdf",[3, 6, 27], "output.pdf")
