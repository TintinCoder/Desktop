from tkinter import *
root= Tk()
root.title("Driving License")
root.geometry("1000x1000")

label_title = Label(root, text="Your Driving License", width="1000", height="2")
label_title.config(bg="red")
label_title.pack()

label_id = Label(root, text="ID: ")
label_id.place(relx="0", rely="0.05")

label_name = Label(root, text="Name: ")
label_name.place(relx="0", rely="0.10")

label_dob = Label(root, text="Date Of Birth: ")
label_dob.place(relx="0", rely="0.13")

label_pin = Label(root, text="Pin No: ")
label_pin.place(relx="0", rely="0.15")

label_address = Label(root, text="Address: ")
label_address.place(relx="0", rely="0.17")

label_auth = Label(root, text="Authorisation to drive the following vehicles: ")
label_auth.place(relx="0", rely="0.19")

label1 = Label(root)

label2 = Label(root)

label3 = Label(root)

label4 = Label(root)

label5 = Label(root)

label6 = Label(root)


def showDetails():
    textID = 2375557274
    print(type(textID))
    name = "Divyam Yadav"
    print(type(name))
    dob = "21st August 2010"
    print(type(dob))
    pin = 532252
    print(type(pin))
    address = "House No. 1755, Gurugram, Haryana, India, Asia, Earth, Milky Way, Universe"
    print(type(address))
    auth = "Two Wheeler"
    print(type(auth))
    
    label1['text'] = textID
    label2['text'] = name
    label3['text'] = dob
    label4['text'] = pin
    label5['text'] = address
    label6['text'] = auth
    
    label1.place(relx="0.1", rely="0.05")
    label2.place(relx="0.1", rely="0.10")
    label3.place(relx="0.1", rely="0.13")
    label4.place(relx="0.1", rely="0.15")
    label5.place(relx="0.1", rely="0.17")
    label6.place(relx="0.3", rely="0.19")
    
start = Button(root, text="Get Details", command=showDetails)
start.pack()
root.mainloop()