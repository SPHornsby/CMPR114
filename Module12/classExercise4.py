import tkinter
import tkinter.messagebox

class MyGUI:

    def __init__(self):
        self.main_window = tkinter.Tk()
        self.my_button1 = tkinter.Button(self.main_window, text='Quote 1',command=self.display_quote1)
        self.my_button2 = tkinter.Button(self.main_window, text='Quote 2',command=self.display_quote2)
        self.my_button3 = tkinter.Button(self.main_window, text='Quote 3',command=self.display_quote3)

        self.my_button1.pack()
        self.my_button2.pack()
        self.my_button3.pack()

        tkinter.mainloop()
    def display_quote1(self):
        response = 'For small creatures such as we the vastness is bearable only through love.'
        tkinter.messagebox.showinfo('Your quote:',response)
    def display_quote2(self):
        response = 'Singing is like a celebration of oxygen.'
        tkinter.messagebox.showinfo('Your quote:',response)
    def display_quote3(self):
        response = 'Laughter is the language of the soul.'
        tkinter.messagebox.showinfo('Your quote:',response)

if __name__ == '__main__':
    my_gui = MyGUI()