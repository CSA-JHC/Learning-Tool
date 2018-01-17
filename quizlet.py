#imports
#import Tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

#class for page screens
##class Page(tk.Frame):
##    def __init__(self,*args,**kwargs):
##        tk.Frame.__init__(self,*args,**kwargs)
##    def show(self):
##        self.lift()
##class Page1(Page):
##   def __init__(self, *args, **kwargs):
##       Page.__init__(self, *args, **kwargs)
##       label = tk.Label(self, text="This is page 1")
##       label.pack(side="top", fill="both", expand=True)

#to create a new account
##def createaccount(*args):
##    firstname=input('What is your name? ')
##    lastname=input('What is your name?' )
##    un=input('Create a Username: ')
##    pw=input('Create a Password: ')

#to login   
def login(*args):
    if usernameentry.get()=='' or passwordentry.get()=='':
        messagebox.showinfo(title='ERROR', message='You did not enter a username or password.')
        root.mainloop()
    else:
        file=open('quizlet_logins.txt','r')
        for line in file:
            info=[]
            line=line.replace('\n','').split(',')
            if usernameentry.get() and passwordentry.get() in line:
                        loginlbl.destroy()
                        usernamelbl.destroy()
                        usernameentry.destroy()
                        psswordlbl.destroy()
                        passwordentry.destroy()
                        button.destroy()
                        button2.destroy()

            else:
                print('oops')
        
#important stuff, sets frame etc.
root=Tk()
root.title("Learning Tool")
root.geometry('300x300')
menuframe=Menu(root)
root.config(menu=menuframe)

#MENUS
#file w exit
filemenu=Menu(menuframe)
menuframe.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Exit', command=root.quit)
#help w instructions?
helpmenu=Menu(menuframe)
menuframe.add_cascade(label='Help', menu=helpmenu)

#variables
username=StringVar()
password=StringVar()

#LOGIN SCREEN
#login label
loginlbl=ttk.Label(root, text='Please Login').grid(column=1, row=1)
#username
usernamelbl=ttk.Label(root, text='Username: ').grid(column=1, row=2)
usernameentry=ttk.Entry(root, textvariable=username)
usernameentry.grid(column=2, row=2, padx=5, pady=5)
#password
passwordlbl=ttk.Label(root, text='Password: ').grid(column=1, row=3)
passwordentry=ttk.Entry(root, textvariable=password)
passwordentry.grid(column=2, row=3, padx=5, pady=5)
#login button (DONT FORGET TO ADD CHECK FUNCTION)
loginbtn=ttk.Button(root, text='Login', command=login).grid(column=1, row=4)

#SWITCH PAGES
