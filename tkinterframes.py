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

        for F in (StartPage, Study, CreateAccount, StudyWrite):

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
        
        #variables
        username=StringVar()
        password=StringVar()

        #check if username is valid
        def login(*args):
            if usernameentry.get()=='' or passwordentry.get()=='':
                messagebox.showinfo(title='ERROR', message='You did not enter a username or password.')
            else:
                controller.show_frame(Study)
                    
        #login label
        loginlbl=tk.Label(self, text='Please Login or').grid(column=0, row=1)
        #username
        usernamelbl=tk.Label(self, text='Username: ').grid(column=0, row=2)
        usernameentry=tk.Entry(self, textvariable=username)
        usernameentry.grid(column=1, row=2, padx=5, pady=5)
        #password
        passwordlbl=tk.Label(self, text='Password: ').grid(column=0, row=3)
        passwordentry=tk.Entry(self, textvariable=password)
        passwordentry.grid(column=1, row=3, padx=5, pady=5)
 
        loginbtn = tk.Button(self, text="Login", command=login).grid(column=1, row=4,padx=5,pady=5)
        createbtn=tk.Button(self, text='Create Account',command=lambda: controller.show_frame(CreateAccount)).grid(column=1, row=1, padx=5,pady=5)


class Study(tk.Frame):
    def __init__(self, parent, controller):        
        tk.Frame.__init__(self, parent)
##        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
##        label.pack(pady=10,padx=10)
        
        #startpage
        logoutbtn = tk.Button(self, text="Logout", command=lambda: controller.show_frame(StartPage)).grid(column=0,row=0, padx=5, pady=5)

        studylbl=tk.Label(self, text='How would you like to study?').grid(column=2, row=1)
        flashcardbtn=tk.Button(self,text='Flashcard').grid(column=2,row=2,padx=5,pady=5)
        writebtn=tk.Button(self,text='Write',command=lambda: controller.show_frame(StudyWrite)).grid(column=2,row=3,padx=5,pady=5)


class CreateAccount(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
##        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
##        label.pack(pady=10,padx=10)

        #variables
        newusername=StringVar()
        newpassword=StringVar()

        #add the new account to the file
        def createact(*args):
            newact=[]
            newun=unentry.get()
            newpw=pwentry.get()
            newact.append(newun)
            newact.append(newpw)
            file=open('quizlet_logins.txt','a')
            newact=str(newact).replace('[','')
            newact=str(newact).replace(']','')
            newact=str(newact).replace("'",'')
            file.write(newact+'\n')
            self.onClose()  

        #check to see if username is already in use
        def test(*args):
            print(newusername.get())
            file=open('quizlet_logins.txt','r')
            for line in file:
                line=line.replace('\n','').split(',')
                print(line)
                if unentry==line[0]:
                    messagebox.showinfo(title='ERROR',message='Your username is already being used, please choose another username.')
                    break
                #figure out a way to stop this loop

        root=Tk()
        #login label
        createlbl=tk.Label(self, text='Create an Account').grid(column=0, row=1)
        #username
        newunlbl=tk.Label(self, text='Username: ').grid(column=0, row=2)
        unentry=tk.Entry(self, textvariable=newusername)
        unentry.grid(column=1, row=2, padx=5, pady=5)
        #password
        newpwlbl=tk.Label(self, text='Password: ').grid(column=0, row=3)
        pwentry=tk.Entry(self, textvariable=newpassword)
        pwentry.grid(column=1, row=3) #not working yet

        # create the button
        createbtn = tk.Button(self, text="Create", command=lambda: controller.show_frame(StartPage)).grid(column=1, row=4, padx=5, pady=5)

#write option
class StudyWrite(tk.Frame):
    def __init__(self, parent, controller):        
        tk.Frame.__init__(self, parent)
##        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
##        label.pack(pady=10,padx=10)


app = SeaofBTCapp()
app.mainloop()
