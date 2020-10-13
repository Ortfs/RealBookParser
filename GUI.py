from tkinter import *
from tkinter import ttk
import sys
sys.setrecursionlimit(10**6)
from rb import std_search, get_pdf, matchtostring

def click():
    entered_text = searchbar.get()
    output_text = matchtostring(std_search(entered_text))
    output = ttk.Label(root, text = output_text)
    output.grid(row = 2, column = 3, sticky = E)

def click1():
    entered_text = searchbar.get()
    matches = std_search(entered_text)

    matchbox.delete(1,END)
    if matches == []:
        matchbox.insert(2, 'No matches!')
    for i in range(len(matches)):
        #button = ttk.Button(root, text = matches[i][0], command = click2)
        matchbox.insert(i+1, matches[i][0])
def click2():
    entered_text = searchbar.get()
    matches = std_search(entered_text)
    selected = matchbox.curselection()[0]
    get_pdf(matches[selected-1][1])

root = Tk()
root.title("RealBookParser v1.5")
root.geometry('700x500')
#root.configure(bg = "black")

top = Label(root, text = "welcome to RBParser v1.5 \n please enter a Keyword")
top.grid(row = 0, column = 1, sticky = N)



keyword = StringVar()
searchbar = ttk.Entry(root, textvariable = keyword)
searchbar.grid(row = 1, column = 1, sticky = W)

searchbutton = ttk.Button(root, text = "search!", command = click1)
searchbutton.grid(row = 2, column = 1, sticky = W)


output_label = ttk.Label(root, text = "Here's what I found:")
output_label.grid(row = 1, column = 3)

matchbox = Listbox(root, width = 40)
matchbox.insert(1, "TITLE")
matchbox.grid(row = 2, column = 3)

"""
page_no = StringVar()
pdf_bar = ttk.Entry(root, textvariable = page_no)
pdf_bar.grid(row = 3, column = 3)
"""
pdf_button = ttk.Button(root, text = "get pdf", command = click2)
pdf_button.grid(row = 4, column = 3)

root.mainloop()
