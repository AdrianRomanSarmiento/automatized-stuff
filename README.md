# automatized-stuff
Python scripts to automate various tasks

## Automatically checking your Email - toHotmail_Firefox.py
Using Firefox, it opens the outlook web page and introduces your email and password automatically.

Notes:
- You need to have Firefox installed, as well as the selenium Module
- Modify the `example@hotmail.com` and `example_password` with your real email and password
- If changes occur in the Outlook web page Xpath's, the code may no longer be valid. Last check: March 2018 

## Useful tools to edit PDF files - pdfTools.py
Rotates, combines and reorders PDF files. Currently, the supported functions are:

#### rotation("input.pdf", pdfpage, degrees, "outputName.pdf")
Rotates 90, 180 or 270 degrees (clockwise) a specific page of a PDF. `pdfpage`and `degrees` must be integers. The output file is only the rotated page.

#### rotation2("input.pdf", pdfpage, degrees, "outputName.pdf")
Rotates 90, 180 or 270 degrees (clockwise) a specific page of a PDF. `pdfpage`and `degrees` must be integers. The output file is like the input file, but contains the rotated page in the same place as the original.

#### combination(["file_1.pdf", "file_2.pdf", "file_3.pdf"], outputName.pdf")
Merges PDF documents into a single PDF file. The order in the output file will be the same as in the list.

#### reorder("input.pdf", [list of pages you want], "outputName.pdf")
Reorders the pages of a PDF file in a desired order. The pages indicated in the list must be integers. Can also be used to extract one page of a PDF file.
