import tkinter as tk
from tkinter import messagebox

win = tk.Tk() # Create the window interface
win.geometry('400x150')
win.title('Customer Information')

lblLastname = tk.Label(win, text= 'enter the lastname').grid(column  =0, row = 0)
lblFirstname = tk.Label(win, text= 'enter the firstname').grid(column = 0, row = 1)

lblAddress = tk.Label(win, text= 'enter the address').grid(column = 0, row = 2)
lblCity = tk.Label(win, text= 'enter the city').grid(column = 0, row = 3)
lblState = tk.Label(win, text= 'enter the state').grid(column = 0, row = 4)
lblZip = tk.Label(win, text= 'enter the zip code').grid(column = 0, row = 5)


def write()->None:
    text_file = open('Customers.txt','a')
    content = text_file.write('\nConfirmation: ' + str(LN.get()) + ', ' + str(FN.get()) + ', ' + str(ADD.get()) + ', ' + str(CTY.get()) + ', ' + str(ST.get()) + ', ' + str(ZIP.get()))
    text_file.close()
    messagebox.showinfo('information', 'Data Recorded')

def quit():
    messagebox.showinfo('inromation','Thank you...')
    win.destroy()

def submit():
    messagebox.showinfo('information', 'entered :' + LN.get() + ',' + FN.get() + ',' + ADD.get() + ',' + CTY.get() + ',' + ST.get() + ',' + ZIP.get())

LN = tk.StringVar()
txtLastname = tk.Entry(win, width = 30, textvariable= LN).grid(column = 1, row = 0)
FN = tk.StringVar()
txtFirstname = tk.Entry(win, width=30, textvariable=FN).grid(column = 1, row =1)

ADD = tk.StringVar()
txtAddress = tk.Entry(win, width=30, textvariable=ADD).grid(column = 1, row =2)
CTY = tk.StringVar()
txtCity = tk.Entry(win, width=30, textvariable=CTY).grid(column = 1, row =3)
ST = tk.StringVar()
txtState = tk.Entry(win, width=30, textvariable=ST).grid(column = 1, row =4)
ZIP = tk.StringVar()
txtZip = tk.Entry(win, width=30, textvariable=ZIP).grid(column = 1, row =5)

btnSubmit = tk.Button(win, text='submit', command = submit).grid(column=0, row=6)
btnQuit = tk.Button(win, text='quit', command=quit).grid(column=1, row=6)
btnWrite = tk.Button(win, text='transfer',command=write).grid(column=2, row=6)

win.mainloop()
submit()