#imports
#import Tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import tkinter as tk

##try to make it look nicer
##try to get everything working
##think of ways to make this program different than others

#basis for frames/windows being created below
class SeaofBTCapp(object):
    def __init__(self,parent):
        self.root=parent
        self.root.title('Learning Tool')
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

#start page - create account or login - WORKING
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        
        #variables
        username=StringVar()
        password=StringVar()

        #check if username is valid
        def login(*args):
            if usernameentry.get()=='' or passwordentry.get()=='':
                messagebox.showinfo(title='ERROR', message='You did not enter a username or password.')
            else:
                x=1
                file=open('quizlet_logins.txt','r')
                for line in file:
                    info=[]
                    line=line.replace('\n','').split(',')
                    #print(line[1])
                    #print(password.get())
                    if username.get()==line[0] and (' '+password.get())==line[1]:
                        #controller.show_frame(Terms)
                        x=0 #helps keep track of whether login was valid or invalid
                        break
                    else:
                        x=1
                if x==1:
                    messagebox.showinfo(title='ERROR', message='You entered your username or password incorrectly.')
                elif x==0:
                    usernameentry.delete(0,END)
                    passwordentry.delete(0,END)
                    controller.show_frame(Terms)
                    
        #login label
        loginlbl=tk.Label(self, text='Please Login or').grid(column=0, row=1)
        #username
        usernamelbl=tk.Label(self, text='Username: ').grid(column=0, row=2)
        usernameentry=tk.Entry(self, textvariable=username)
        usernameentry.grid(column=1, row=2, padx=5, pady=5)
        #password
        passwordlbl=tk.Label(self, text='Password: ').grid(column=0, row=3)
        passwordentry=tk.Entry(self, textvariable=password, show='*')
        passwordentry.grid(column=1, row=3, padx=5, pady=5)
 
        loginbtn = tk.Button(self, text="Login", command=login).grid(column=1, row=4,padx=5,pady=5)
        createbtn=tk.Button(self, text='Create Account',command=lambda: controller.show_frame(CreateAccount)).grid(column=1, row=1, padx=5,pady=5)

#choose what they wanna study - WORKING
class Study(tk.Frame):
    def __init__(self, parent, controller):        
        tk.Frame.__init__(self, parent)
        
        logoutbtn = tk.Button(self, text="Logout", command=lambda: controller.show_frame(StartPage)).grid(column=0,row=0, padx=5, pady=5)
        backbtn=tk.Button(self, text='Back',command=lambda: controller.show_frame(Terms)).grid(column=1,row=0,padx=5,pady=5)#go back to previous pg

        studylbl=tk.Label(self, text='How would you like to study?').grid(column=2, row=1)
        flashcardbtn=tk.Button(self,text='Flashcard',command=lambda: controller.show_frame(StudyFlash)).grid(column=2,row=2,padx=5,pady=5)
        writebtn=tk.Button(self,text='Write',command=lambda: controller.show_frame(StudyWrite)).grid(column=2,row=3,padx=5,pady=5)

#create a new account - WORKING
class CreateAccount(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        backbtn=tk.Button(self, text='Back',command=lambda: controller.show_frame(StartPage)).grid(column=0,row=0,padx=5,pady=5)#go back to previous pg

        #variables
        newusername=StringVar()
        newpassword=StringVar()
        checkpassword=StringVar()

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
            unentry.delete(0,END)
            pwentry.delete(0,END)
            controller.show_frame(StartPage)
            messagebox.showinfo(title='',message='Your account has been created!')

        #check to see if username is already in use
        def test(*args):
            #print(newusername.get())
            info=[]
            file=open('quizlet_logins.txt','r')
            for line in file:
                line=line.replace('\n','').split(',')
                #print(line)
                info.append(line[0])
            if unentry.get() in info:
                messagebox.showinfo(title='ERROR', message='This username is already in use. Please choose another username.')
            elif unentry.get()=='' or pwentry.get()=='':
                messagebox.showinfo(title='ERROR', message='You did not enter a username or password.')
            else:
                if pwentry.get()==checkpwentry.get():
                    createact()
                else:
                    messagebox.showinfo(title='ERROR', message='Your passwords do not match.')
                    
            file.close()
        
        #root=Tk()
        #login label
        createlbl=tk.Label(self, text='Create an Account').grid(column=0, row=1)
        #username
        newunlbl=tk.Label(self, text='Username: ').grid(column=0, row=2)
        unentry=tk.Entry(self, textvariable=newusername)
        unentry.grid(column=1, row=2, padx=5, pady=5)
        #password
        newpwlbl=tk.Label(self, text='Password: ').grid(column=0, row=3)
        pwentry=tk.Entry(self, textvariable=newpassword, show='*')
        pwentry.grid(column=1, row=3, padx=5, pady=5) #not working yet
        #check password
        checkpwlbl=tk.Label(self, text='Verify Password: ').grid(column=0, row=4)
        checkpwentry=tk.Entry(self, textvariable=checkpassword, show='*')
        checkpwentry.grid(column=1, row=4, padx=5, pady=5) #not working yet

        #create the button
        createbtn = tk.Button(self, text="Create", command=test).grid(column=1, row=5, padx=5, pady=5)

#terms being studied - WORKING
class Terms(tk.Frame):
    def __init__(self, parent, controller):        
        tk.Frame.__init__(self, parent)
        
        logoutbtn = tk.Button(self, text="Logout", command=lambda: controller.show_frame(StartPage)).grid(column=0,row=0, padx=5, pady=5)
        #backbtn=tk.Button(self, text='Back',command=lambda: controller.show_frame(Study)).grid(column=3,row=0,padx=5,pady=5)

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

        def saveterms(*args):
            #if there are no terms entered
            if (term1.get() and term2.get() and term3.get() and term4.get() and term5.get() and defn1.get() and defn2.get() and defn3.get() and defn4.get() and defn5.get())=='':
                messagebox.showinfo(title='ERROR', message='Please enter terms before continuting.')
            else:
                #write to file
                file=open('studyterms.txt','w')
                file.write(term1.get()+','+defn1.get()+'\n')
                term1.delete(0,END)
                defn1.delete(0,END)
                file.write(term2.get()+','+defn2.get()+'\n')
                term2.delete(0,END)
                defn2.delete(0,END)
                file.write(term3.get()+','+defn3.get()+'\n')
                term3.delete(0,END)
                defn3.delete(0,END)
                file.write(term4.get()+','+defn4.get()+'\n')
                term4.delete(0,END)
                defn4.delete(0,END)
                file.write(term5.get()+','+defn5.get()+'\n')
                term5.delete(0,END)
                defn5.delete(0,END)
                file.close()
                controller.show_frame(Study) #go to next frame
        
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

        #print(terms1.get())
        savebtn=tk.Button(self, text='Save',command=saveterms).grid(column=1,row=0,padx=5,pady=5)
        #printing empty line.. fix it!
        
#write option - NEEDS WORK - figure out how to check terms (similar to flashcard?)
class StudyWrite(tk.Frame):
    def __init__(self, parent, controller):        
        tk.Frame.__init__(self, parent)

        #variables
        ask=StringVar()

        logoutbtn = tk.Button(self, text="Logout", command=lambda: controller.show_frame(StartPage)).grid(column=0,row=0, padx=5, pady=5) #logout and return to start pg
        backbtn=tk.Button(self, text='Back',command=lambda: controller.show_frame(Study)).grid(column=1,row=0,padx=5,pady=5)#go back to previous pg
        checkbtn=tk.Button(self,text='Check',command=check).grid(column=3,row=1, padx=5,pady=5)
        defnentry=tk.Entry(self, textvariable=ask)
        defentry.grid(column=2, row=2, padx=5, pady=5)

        #check if its right
        def check(*args):
            print('doing something')
            #if matches, delete text in entry box, clear label

            #if doesn't match, keep it there

        studying=[]
        file=open('studyterms.txt','r')
        for line in file:
            print(line)
            line=line.replace('\n','').split(',')
            x=random.randint(0,1)
            studying.append(line[x])
            termlbl=tk.Label(self,text=line[0])#.grid(column=2,row=1,padx=5,pady=5)
            termlbl.visible=True
            termlbl.place(x=20,y=50)
            termlbl.pi=termlbl.place_info()
        file.close()
        print(studying)
        
#flashcard option - NEEDS WORK - and next term function, start button dissapear
class StudyFlash(tk.Frame):
    def __init__(self, parent, controller):        
        tk.Frame.__init__(self, parent)

        def getTerm(*args):
            #finding term to study
            #startbtn.place_forget()
            #startbtn.visible=not startbtn.visible
            studying=[]
            file=open('studyterms.txt','r')
            for line in file:
                print(line)
                line=line.replace('\n','').split(',')
                x=random.randint(0,1)
                studying.append(line[x])
                termlbl=tk.Label(self,text=line[0])#.grid(column=2,row=1,padx=5,pady=5)
                termlbl.visible=True
                termlbl.place(x=20,y=50)
                termlbl.pi=termlbl.place_info()
                defnlbl=tk.Label(self,text=line[1])
                defnlbl.visible=True
                defnlbl.place(x=20,y=50)
                defnlbl.pi=defnlbl.place_info()
                defnlbl.place_forget()
            file.close()
            print(studying)

        def check(*args): #flips "card"
            if termlbl.visible:
                print(studying)
                file=open('studyterms.txt','r')
                for line in file:
                    line=line.replace('\n','').split(',')
                    print(line)
                    #print(studying[0])
                    if studying[0]==line[0]:
                        termlbl.place_forget()
                        defnlbl.place(defnlbl.pi)
                    elif studying[0]==line[1]:
                        pass
            else:
                defnlbl.place_forget()
                termlbl.place(termlbl.pi)                        
            termlbl.visible=not termlbl.visible
            defnlbl.visible=not defnlbl.visible
            #termlbl.visible=not termlbl.visible #not working

        def nextTerm(*args): #moves to next word
            print('next')
            
        logoutbtn = tk.Button(self, text="Logout", command=lambda: controller.show_frame(StartPage)).grid(column=0,row=0, padx=5, pady=5)
        backbtn=tk.Button(self, text='Back',command=lambda: controller.show_frame(Study)).grid(column=1,row=0,padx=5,pady=5)        
        flipbtn=tk.Button(self, text='Flip',command=check).grid(column=2, row=3, padx=5, pady=5)
        nextbtn=tk.Button(self, text='Next',command=nextTerm).grid(column=3, row=3, padx=5, pady=5)
        startbtn=tk.Button(self,text='Start',command=getTerm).grid(column=1,row=4,padx=5,pady=5)
        #startbtn.visible=True
##        startbtn.place(x=20,y=50)
##        startbtn.pi=startbtn.place_info()
##        startbtn.place_forget()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x400")
    app = SeaofBTCapp(root)
    root.mainloop()
