# RealBookParser
RealBookParser - a simple tool for managing "Real Book" pdfs

Welcome to RealBookParser v1.4! 

INTRODUCTION

As all jazz musicians know, "Real Books" are an extremely important resource. However, they can be hard work; especially if one only has them in digital form. 
Let's assume you want to play a piece which you know is contained in a Real Book and that you have said Real Book in pdf form. This is what you have to do:

 - consult the master index to find the exact edition and page number
 - open the corresponding real book pdf and find said page (which will likely not correspond to the page of the actual pdf)
 - either read the pdf as-is (and repeat the process every time you need it), or use a pdf tool to extract the single pages you need for future reference

This involves opening numerous pdfs and relying on various tools/readers to do the job, and anyone who does this regularly knows it's a tedious process. 
There must be an easier way, no? Well, now there is! 

WHAT RealBookParser DOES

RealBookParser automates the process described above. It is made up of two .txt files (data1 and data2) containing the data of the real book master index and a python script which converts said data and uses it in conjunction with the PyPDF2 package to extract single pieces/pages from a .pdf file called master.pdf, containing the sheet music pages of all the real books in the master index (apart from the Standards Real Book. This will be added at a later date) 

NOTE: Due to copyright restrictions, I cannot include any Real Book pdf's in this repository. You will need to make your own master.pdf to use RealBookParser! (This is the only tricky part. If you have questions, don't hesitate to contact francesconowell "at" gmail dot com



FIRST TIME SETUP

Step 1: make sure you have Python 2.7 or higher installed, as well as the PyPDF package (pip install PyPDF2) 
Step 2: create your own master.pdf by concatenating the Real Book pages in the following order:

        - Real Book 1 (vol.5)
        - Real Book 2 (all new, vol II.)
        - The New Real Book 1 (Sher Music)
        - The New Real Book 2 (Sher Music)
        - The New Real Book 3 (Sher Music)
        
NOTE: You should only have the SHEET MUSIC PAGES in your pdf, without the covers/indices. The pieces in the appendices will also be added at a later date. Page 1 of master.pdf should be page 1 of the Real Book 1. Page 478 should be Page 1 of the Real Book 2, etc. (Again, apologies if this is annoying but there are pdf manipulation tools which should make this relatively easy. If you run into trouble, contact me!) 

Step 3: Place your master.pdf in the same folder as the script and the data text files



HOW TO USE RealBookParser

Step 1: Open terminal/command prompt and run the python script in interactive mode (python3 -i rb_parser_v1.4.py) 

Step 2: When prompted, search for a piece using command std_search("Keyword"). Make Sure You Capitalize The Keyword Like This! 

Step 3: All of the matches will appear, together with a key number. Find the key of the standard you were looking for, and enter command get_pdf(key)

Step 4: All done! the pdf of the individual standard will now be in the same folder


FUTURE UPDATES

I plan to add the following features at a later date: 

- Support for the Standards real book, as well as the pieces in the appendices of the other real books
- A GUI 
- Conversion into an directly executable program/app



