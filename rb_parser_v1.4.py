import re
import PyPDF2
from PyPDF2 import PdfFileReader,PdfFileWriter

#convert the .txt files to a string
part1 = open(r"data1.txt", "r+")
part2 = open(r"data2.txt", "r+")

string1 = str(part1.read())
string2 = str(part2.read())

#split the two strings at every blank space, creating two lists
list1 = re.split("\s", string1)
list2 = re.split("\s", string2)

std_list = []

def parser(l):
    keys = ['R1' , 'R2', 'NR1' , 'NR2' , 'NR3' , 'SRB']
    title = ""
    i = 0
    while l[i] not in keys:
        title += l[i]
        title += " "
        i += 1
    std = [title[:-1], l[i], l[i+1]]
    std_list.append(std)
    l = l[i+2:]
    if len(l) > 1:
        parser(l)

#each standard in the master index is now a 3- element list of the form [title, 'real book', 'page no.'], contained in std_list
parser(list1)
parser(list2)

#converts 'page no.' to integer
for std in std_list:
    if not std[-1].isdigit():
            std_list.remove(std)
    else:
        std[-1] = int(std[-1])

#sort the stds in std_list by edition, adding to the page no. so as to get the according page no. in master.pdf
r1_stds = []
r2_stds = []
nr1_stds = []
nr2_stds = []
nr3_stds = []
#srb_stds = []
appendix = []
for std in std_list:
    if std[1] == "R1":
        std.pop(1)
        r1_stds.append(std)
    elif std[1] == "R2":
        std.pop(1)
        std[-1] += 477
        r2_stds.append(std)
    elif std[1] == "NR1":
        std.pop(1)
        std[-1] += 891
        nr1_stds.append(std)
    elif std[1] == "NR2":
        std.pop(1)
        std[-1] += 1303
        nr2_stds.append(std)
    elif std[1] == "NR3":
        std.pop(1)
        std[-1] += 1750
        nr3_stds.append(std)

    """
    elif std[1] == "SRB":
        std.pop(1)
        std[-1] += 2174
        srb_stds.append(std)
    """


#removes the stds at the end of the Real Book 1 (to be added at a later date)
for std in r1_stds:
    if int(std[1]) > 500:
        appendix.append(std)
        r1_stds.remove(std)


#sorts stds in a given edition by page no.
#assigns a "page amount" to each std (i.e the amount of pages between one standard and the next)
def pages(list):
    list.sort(key = lambda x:int(x[1]))
    for i in range(len(list)-1):
        std = list[i]
        next_std = list[i+1]
        std.append(int(next_std[1])-int(std[1]))

        if std[2] == 0:
            std[2] = 1
    list[-1].append(1)

pages(r1_stds)
pages(r2_stds)
pages(nr1_stds)
pages(nr2_stds)
pages(nr3_stds)
#pages(srb_stds)

#cleaning up: removal of appendices (to be added at a later date)
appendix2 = nr1_stds[-7:]
nr1_stds = nr1_stds[:-7]
nr1_stds[-1][-1] = 2

appendix3 = nr2_stds[-6:]
nr2_stds = nr2_stds[:-6]

#'re-merge' all stds into one list. stds are now of the form ['title', page no. in master.pdf, amount of pages]
all_stds = r1_stds + r2_stds + nr1_stds + nr2_stds + nr3_stds

#all_std += srb_stds

#create the pdf of the k_th standard in all_stds using PyPDF2
def get_pdf(k):
    pdfFileObj = open("master.pdf", 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    title = all_stds[k-1][0]
    page_num = all_stds[k-1][1]
    num_pages = all_stds[k-1][2]
    output = PyPDF2.PdfFileWriter()
    for i in range(num_pages):
            pageObj = pdfReader.getPage(page_num -1 + i)
            output.addPage(pageObj)
    output_pdf = open(title + ' .pdf', 'wb')
    output.write(output_pdf)
    output_pdf.close()


#searches all_stds for ones whose title contains the string "word"
#returns all matches together with their indices in tuple form
def std_search(word):
    matching = []
    for std in all_stds:
        if word in std[0]:
            matching.append((std[0], all_stds.index(std)+1))
    print("")
    print(  "Here's what I found:")
    print("")
    print("")
    for match in matching:
        print(match)
    print("")
    print(  'Use command get_pdf( "page number" ) to create the pdf')



print(" Welcome to the Real Book pdf parser v1.4!")
print(' Use command std_search( "Capitalized Keyword" ) to search for a standard')
print(' E.g std_search("Autumn")')
