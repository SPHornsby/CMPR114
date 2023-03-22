import tkinter as tk
from tkinter import messagebox

win = tk.Tk() # Create the window interface
win.geometry('300x100')
win.title('Fun with Numbers!')

tk.Label(win, text= 'enter the first number').grid(column  =0, row = 0)
tk.Label(win, text= 'enter the second number').grid(column = 0, row = 1)
tk.Label(win, text= 'enter the third number').grid(column = 0, row = 2)

def write()->None:
    text_file = open('FunWithNumbers.txt','a')
    nums = [float(F.get()),float(S.get()),float(T.get())]
    total = sum(nums)
    avg = total/3
    text_file.write('\nConfirmation: ' + str(F.get()) + ', ' + str(S.get()) + ', ' + str(T.get())+', total:' + str(total) + ', avg:' + str(avg))
    text_file.close()
    messagebox.showinfo('information', 'Data Recorded')

def quit()->None:
    messagebox.showinfo('inromation','Thank you...')
    win.destroy()

def submit()->None:
    messagebox.showinfo('information', 'entered :' + F.get() + ',' + S.get() + ',' + T.get())

F = tk.StringVar()
tk.Entry(win, width = 10, textvariable= F).grid(column = 1, row = 0)
S = tk.StringVar()
tk.Entry(win, width=10, textvariable=S).grid(column = 1, row =1)
T = tk.StringVar()
tk.Entry(win, width=10, textvariable=T).grid(column = 1, row =2)

btnSubmit = tk.Button(win, text='submit', command = submit).grid(column=0, row=6)
btnQuit = tk.Button(win, text='quit', command=quit).grid(column=1, row=6)
btnWrite = tk.Button(win, text='transfer',command=write).grid(column=2, row=6)

win.mainloop()
submit()