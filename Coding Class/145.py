#Importing Tkinter
from ast import If
from tkinter import *
#Defining root variable
root = Tk()
#Adding the title
root.title("ID Verification")
#Sizing The Window
root.geometry("400x500")

label1 = Label(root)
label2 = Label(root)
label3 = Label(root)

def showDetails():
    name = "Divyam Yadav"
    print(type(name))
    grade = 6
    print(type(grade))   
    subject = ["Math", "SST", "German"]
    print(type(subject))
    label1['text'] = name
    label2['text'] = grade
    label3['text'] = subject

buttonStart = Button(root, text="Show My Details", command=showDetails)
buttonStart.pack()
label1.pack()
label2.pack()
label3.pack()
#Running The Program 
root.mainloop()