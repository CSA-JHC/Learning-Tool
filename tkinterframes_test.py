from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import tkinter as tk

#flashcard window


#write window

#choose what you want to learn
class OtherFrame(tk.Toplevel):
    def __init__(self,original):
        """Constructor"""
        self.original_frame=original
        tk.Toplevel.__init__(self)
        self.geometry("400x300")
        self.title("otherFrame")
 
        # create the button
        logoutbtn = tk.Button(self, text="Logout", command=self.onClose).grid(column=0,row=0, padx=5, pady=5)

        studylbl=tk.Label(self, text='How would you like to study?').grid(column=2, row=1)
        flashcardbtn=tk.Button(self,text='Flashcard').grid(column=2,row=2,padx=5,pady=5)
        writebtn=tk.Button(self,text='Write').grid(column=2,row=3,padx=5,pady=5)

    def onClose(self): #closes frame, opens start page
        self.destroy()
        self.original_frame.show()

#not working yet
class NewAccount(tk.Toplevel):
    def __init__(self,original):
        """Constructor"""
        self.original_frame=original
        tk.Toplevel.__init__(self)
        self.geometry("400x300")
        self.title("newAccount")

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
        createbtn = tk.Button(self, text="Create", command=self.onClose).grid(column=1, row=4, padx=5, pady=5)
        
    def onClose(self): #closes frame, opens start page
        self.destroy()
        self.original_frame.show()
        
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

##        #check if username is valid
##        def login(*args):
##            if usernameentry.get()=='' or passwordentry.get()=='':
##                messagebox.showinfo(title='ERROR', message='You did not enter a username or password.')
##            else:
##                file=open('quizlet_logins.txt','r')
##                for line in file:
##                    line=line.replace('\n','').split(',')
##                    print(line)
##                    if usernameentry.get()==line[0] and passwordentry.get()==line[1]:
##                        self.openOtherFrame()
##                        break
                    
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
 
        loginbtn = tk.Button(self.frame, text="Login", command=self.openOtherFrame).grid(column=1, row=4)
        createbtn=tk.Button(self.frame, text='Create Account',command=self.openNewAccount).grid(column=1, row=1, padx=5,pady=5)
 
    def hide(self): #hides main frame
        self.root.withdraw()
 
    def openOtherFrame(self): #opens other frame
        self.hide()
        subFrame=OtherFrame(self)

    def openNewAccount(self): #opens new account frame
        self.hide()
        subFrame=NewAccount(self)
 
    def show(self): #shows main frame
        self.root.update()
        self.root.deiconify()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x400")
    start = StartPage(root) 
    root.mainloop()
