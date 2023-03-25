import tkinter as tk
from tkinter import messagebox

win = tk.Tk() # Create the window interface
win.geometry('200x70')
win.title('Sum of Numbers!')

def write()->None:
    text_file = open('number.txt','r')
    nums = []
    for line in text_file:
        nums.append(float(line.rstrip('\n')))
    total = sum(nums)
    avg = total/len(nums)
    message = '\nConfirmation:  total: ' + str(total) + ', avg:' + str(avg)

    messagebox.showinfo('information', message)

def quit()->None:
    messagebox.showinfo('information','Thank you...')
    win.destroy()

# def submit()->None:
#     messagebox.showinfo('information', 'entered :' + F.get() + ',' + S.get() + ',' + T.get())


# btnSubmit = tk.Button(win, text='submit', command = submit).grid(column=0, row=6)
btnQuit = tk.Button(win, text='quit', command=quit).grid(column=1, row=0)
btnWrite = tk.Button(win, text='Display',command=write).grid(column=2, row=0)

win.mainloop()
