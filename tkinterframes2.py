from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import tkinter as tk

#soon to be learning page
#try to go back to start page
class OtherFrame(tk.Toplevel):
    def __init__(self):
        """Constructor"""
        tk.Toplevel.__init__(self)
        self.geometry("400x300")
        self.title("otherFrame")
 
        # create the button
        logoutbtn = tk.Button(self, text="Logout", command=self.onClose)
        logoutbtn.pack()
        
    def hide(self): #hides frame
        self.withdraw()
        
    def onClose(self): #closes frame, opens start page
        self.hide()
        subFrame=StartPage(self)

    def show(self): #shows main frame
        self.update()
        self.deiconify()

#not working yet
class NewAccount(tk.Toplevel):
    def __init__(self):
        """Constructor"""
        tk.Toplevel.__init__(self)
        self.geometry("400x300")
        self.title("newAccount")

##        #variables
##        newusername=StringVar()
##        newpassword=StringVar()
##
##        def test(*args):
##            print('hi')
##            self.onClose()
##            
##        root=Tk()
##        #login label
##        createlbl=tk.Label(self, text='Create an Account').grid(column=0, row=1)
##        #username
##        newunlbl=tk.Label(self, text='Username: ').grid(column=0, row=2)
##        unentry=tk.Entry(self, textvariable=newusername)
##        unentry.grid(column=1, row=2, padx=5, pady=5)
##        #password
##        pwlbl=tk.Label(self, text='Password: ').grid(column=0, row=3)
##        pwentry=tk.Entry(self, textvariable=newpassword)
##        pwentry.grid(column=1#not working yet

class NewAccount(tk.Toplevel):
    def __init__(self):
        """Constructor"""
        tk.Toplevel.__init__(self)
        self.geometry("400x300")
        self.title("newAccount")

##        #variables
##        newusername=StringVar()
##        newpassword=StringVar()
##
##        def test(*args):
##            print('hi')
##            self.onClose(), row=3, padx=5, pady=5) 
##
##        # create the button
##        createbtn = tk.Button(self, text="Create", command=test).grid(column=1, row=4)

    def hide(self): #hides main frame
        self.withdraw()
 
    def onClose(self): #closes frame, opens start page
        self.hide()
        subFrame=StartPage(self)
        print('im here')
        
#LOGIN SCREEN
class StartPage(object):
    def __init__(self, parent):
        """Constructor"""
        self.root = parent
        self.root.title("Main frame")
        self.frame = tk.Frame(parent)
        self.frame.pack()

        #variables
        username=StringVar()
        password=StringVar()

        #check if username is valid
        def login(*args):
            if usernameentry.get()=='' or passwordentry.get()=='':
                messagebox.showinfo(title='ERROR', message='You did not enter a username or password.')
            else:
                file=open('quizlet_logins.txt','r')
                for line in file:
                    info=[]
                    line=line.replace('\n','').split(',')
                    if usernameentry.get()==line[0] and passwordentry.get()==line[1]:
                        self.openOtherFrame()
                        break
                    else:
                        messagebox.showinfo(title='ERROR', message='You entered a username or password incorrectly.')
                    
        #login label
        loginlbl=tk.Label(self.frame, text='Please Login or').grid(column=0, row=1)
        #username
        usernamelbl=tk.Label(self.frame, text='Username: ').grid(column=0, row=2)
        usernameentry=tk.Entry(self.frame, textvariable=username)
        usernameentry.grid(column=1, row=2, padx=5, pady=5)
        #password
        passwordlbl=tk.Label(self.frame, text='Password: ').grid(column=0, row=3)
        passwordentry=tk.Entry(self.frame, textvariable=password)
        passwordentry.grid(column=1, row=3, padx=5, pady=5)
 
        loginbtn = tk.Button(self.frame, text="Login", command=login).grid(column=1, row=4)
        createbtn=tk.Button(self.frame, text='Create Account',command=self.openNewAccount).grid(column=1, row=1, padx=5,pady=5)

    def listener(self,arg1,arg2=None): #opens frame when other frame is closed
        self.show()
 
    def hide(self): #hides main frame
        self.root.withdraw()
 
    def openOtherFrame(self): #opens other frame
        self.hide()
        subFrame=OtherFrame()

    def openNewAccount(self): #opens new account frame
        self.hide()
        subFrame=NewAccount()
 
    def show(self): #shows main frame
        self.root.update()
        self.root.deiconify()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x400")
    start = StartPage(root) 
    root.mainloop()
