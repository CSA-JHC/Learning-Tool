#imports
#import Tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import tkinter as tk

root=Tk()
#LARGE_FONT= ("Verdana", 12)

#basis for frames/windows being created below
class SeaofBTCapp(object):
    def __init__(self,parent):
        self.root=parent
        self.root.title('Main Frame')
        self.container = tk.Frame(parent)
        self.container.pack(side="top", fill="both", expand = True)

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Study, CreateAccount, StudyWrite, StudyFlash, Terms):

            frame = F(self.container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

#start page - create account or login
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        #label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        #label.pack(pady=10,padx=10)
        
        #variables
        username=StringVar()
        password=StringVar()

        #check if username is valid
        #MAKE SURE TO CHECK IF USERNAME AND PASSWORD ARE IN FILE
        def login(*args):
            if usernameentry.get()=='' or passwordentry.get()=='':
                messagebox.showinfo(title='ERROR', message='You did not enter a username or password.')
            else:
                controller.show_frame(Terms)
                    
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

#choose what they wanna study
class Study(tk.Frame):
    def __init__(self, parent, controller):        
        tk.Frame.__init__(self, parent)
##        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
##        label.pack(pady=10,padx=10)
        
        logoutbtn = tk.Button(self, text="Logout", command=lambda: controller.show_frame(StartPage)).grid(column=0,row=0, padx=5, pady=5)

        studylbl=tk.Label(self, text='How would you like to study?').grid(column=2, row=1)
        flashcardbtn=tk.Button(self,text='Flashcard',command=lambda: controller.show_frame(StudyFlash)).grid(column=2,row=2,padx=5,pady=5)
        writebtn=tk.Button(self,text='Write',command=lambda: controller.show_frame(StudyWrite)).grid(column=2,row=3,padx=5,pady=5)

#create a new account
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
            controller.show_frame(StartPage)
            messagebox.showinfo(title='',message='Your account has been created!')

        #check to see if username is already in use
        def test(*args):
            print(newusername.get())
            info=[]
            file=open('quizlet_logins.txt','r')
            for line in file:
                line=line.replace('\n','').split(',')
                #print(line)
                info.append(line[0])
            if unentry.get() in info:
                messagebox.showinfo(title='ERROR', message='This username is already in use. Please choose another username.')
            else:
                createact()
                #figure out a way to stop this loop

        #root=Tk()
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
        createbtn = tk.Button(self, text="Create", command=test).grid(column=1, row=4, padx=5, pady=5)

#terms being studied
class Terms(tk.Frame):
    def __init__(self, parent, controller):        
        tk.Frame.__init__(self, parent)
##        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
##        label.pack(pady=10,padx=10)
        
        logoutbtn = tk.Button(self, text="Logout", command=lambda: controller.show_frame(StartPage)).grid(column=0,row=0, padx=5, pady=5)
        #backbtn=tk.Button(self, text='Back',command=lambda: controller.show_frame(Study)).grid(column=3,row=0,padx=5,pady=5)
        savebtn=tk.Button(self, text='Save',command=lambda: controller.show_frame(Study)).grid(column=1,row=0,padx=5,pady=5)

        #variables
        terms1=StringVar()
        terms2=StringVar()
        terms3=StringVar()
        terms4=StringVar()
        terms5=StringVar()
        defns1=StringVar()
        defns2=StringVar()
        defns3=StringVar()
        defns4=StringVar()
        defns5=StringVar()
        
        #5 terms
        term1lbl=tk.Label(self,text='Term').grid(column=2,row=0)
        term1=tk.Entry(self, textvariable=terms1)
        term1.grid(column=2, row=1, padx=5, pady=5)
        term2=tk.Entry(self, textvariable=terms2)
        term2.grid(column=2, row=2, padx=5, pady=5)
        term3=tk.Entry(self, textvariable=terms3)
        term3.grid(column=2, row=3, padx=5, pady=5)
        term4=tk.Entry(self, textvariable=terms4)
        term4.grid(column=2, row=4, padx=5, pady=5)
        term5=tk.Entry(self, textvariable=terms5)
        term5.grid(column=2, row=5, padx=5, pady=5)

        #5 definitions
        defnlbl=tk.Label(self,text='Definition').grid(column=3,row=0)
        defn1=tk.Entry(self, textvariable=defns1)
        defn1.grid(column=3, row=1, padx=5, pady=5)
        defn2=tk.Entry(self, textvariable=defns2)
        defn2.grid(column=3, row=2, padx=5, pady=5)
        defn3=tk.Entry(self, textvariable=defns3)
        defn3.grid(column=3, row=3, padx=5, pady=5)
        defn4=tk.Entry(self, textvariable=defns4)
        defn4.grid(column=3, row=4, padx=5, pady=5)
        defn5=tk.Entry(self, textvariable=defns5)
        defn5.grid(column=3, row=5, padx=5, pady=5)

        #printing empty line.. fix it!
        print(term1.get())

##        #write to file
##        file=open('studyterms.txt','w')
##        file.write(term1.get()+','+defn1.get()+'\n')
##        file.write(term2.get()+','+defn2.get()+'\n')
##        file.write(term3.get()+','+defn3.get()+'\n')
##        file.write(term4.get()+','+defn4.get()+'\n')
##        file.write(term5.get()+','+defn5.get()+'\n')
##        file.close()
        
#write option
class StudyWrite(tk.Frame):
    def __init__(self, parent, controller):        
        tk.Frame.__init__(self, parent)
##        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
##        label.pack(pady=10,padx=10)

        logoutbtn = tk.Button(self, text="Logout", command=lambda: controller.show_frame(StartPage)).grid(column=0,row=0, padx=5, pady=5)
        backbtn=tk.Button(self, text='Back',command=lambda: controller.show_frame(Study)).grid(column=3,row=0,padx=5,pady=5)

        #ask to start with term or definition
        
#flashcard option
class StudyFlash(tk.Frame):
    def __init__(self, parent, controller):        
        tk.Frame.__init__(self, parent)
##        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
##        label.pack(pady=10,padx=10)

        logoutbtn = tk.Button(self, text="Logout", command=lambda: controller.show_frame(StartPage)).grid(column=0,row=0, padx=5, pady=5)
        backbtn=tk.Button(self, text='Back',command=lambda: controller.show_frame(Study)).grid(column=3,row=0,padx=5,pady=5)        

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x400")
    app = SeaofBTCapp(root)
    root.mainloop()
