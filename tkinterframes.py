#imports
#import Tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import tkinter as tk

#important stuff, sets frame etc.
root=Tk()
##root.title("Learning Tool")
##root.geometry('300x300')
##menuframe=Menu(root)
##root.config(menu=menuframe)
##
###MENUS
###file w exit
##filemenu=Menu(menuframe)
##menuframe.add_cascade(label='File', menu=filemenu)
##filemenu.add_command(label='Exit', command=root.quit)
###help w instructions?
##helpmenu=Menu(menuframe)
##menuframe.add_cascade(label='Help', menu=helpmenu)

#variables
username=StringVar()
password=StringVar()

LARGE_FONT= ("Verdana", 12)

class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        #label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        #label.pack(pady=10,padx=10)

                #to login   
        def login(*args):
            if usernameentry.get()=='' or passwordentry.get()=='':
                messagebox.showinfo(title='ERROR', message='You did not enter a username or password.')
                self.mainloop()
            else:
                file=open('quizlet_logins.txt','r')
                for line in file:
                    info=[]
                    line=line.replace('\n','').split(',')
                    if usernameentry.get() and passwordentry.get() in line:
                        controller.show_frame(PageOne)
                    else:
                        print('oops')
                        
        #page1
        #LOGIN SCREEN
        #login label
        loginlbl=tk.Label(parent, text='Please Login').grid(column=0, row=1)
        #username
        usernamelbl=tk.Label(parent, text='Username: ').grid(column=0, row=2)
        usernameentry=tk.Entry(parent, textvariable=username)
        usernameentry.grid(column=1, row=2, padx=5, pady=5)
        #password
        passwordlbl=tk.Label(parent, text='Password: ').grid(column=0, row=3)
        passwordentry=tk.Entry(parent, textvariable=password)
        passwordentry.grid(column=1, row=3, padx=5, pady=5)
        #login button
        #loginbtn=tk.Button(parent, text='Login', command=login).grid(column=0, row=4)

        button = tk.Button(parent, text="Login",
                            command=login).grid(column=0, row=4)
        #loginbtn.pack()
        #page2
        button2 = tk.Button(parent, text="Create Account",
                            command=lambda: controller.show_frame(PageTwo)).grid(column=1, row=4)
        #button2.pack()

class PageOne(tk.Frame):

    def __init__(self, parent, controller):        
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        #startpage
        button1 = tk.Button(self, text="Logout",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()
        


app = SeaofBTCapp()
app.mainloop()
