import os,sys
from tkinter import *
from tkinter import messagebox
root= Tk()
def return_entry(en):
	winMessage = 0
	counter = 0
	typeOne = entry_1.get()
	typeTwo = entry_2.get()
	currentFolder = os.getcwd()
	for oneFile in os.listdir(currentFolder):
		startName = os.path.join(currentFolder, oneFile)
		if not os.path.isfile(startName): continue
		oldbase = os.path.splitext(startName)
		endName = startName.replace(typeOne, typeTwo)
		output = os.rename(startName, endName)
		if startName != endName:
			counter += 1
	winMessage = str(counter) + " filenames changed."
	messagebox.showinfo("Operation Complete", winMessage)
title = Label(root, text="Change All File Extensions in Current Directory", fg="white", bg="black")
one = Label(root, text="Take this extension")
two = Label(root, text="... And change it to this")

entry_1 = Entry(root)
entry_2 = Entry(root)

title.grid(row=0, sticky=N, columnspan=2)
one.grid(row=1, sticky=E)
two.grid(row=2, sticky=E)

entry_1.grid(row=1, column=1)
entry_2.grid(row=2, column=1)


c = Button(root, text="Change file type")
c.grid(columnspan=2)
c.bind('<Button-1>', return_entry)

root.mainloop()
