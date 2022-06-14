from tkinter import *
root = Tk()
root.geometry("500x300")

def getvals():
    print("Accepted")
#Heading 
Label(root, text ="New Registration Form",font="ar 20 bold").grid(row=0,column=3)

#Field name
name = Label(root,text="Name")
mobile = Label(root,text="Mobile")
gender = Label(root,text="Gender")
emergency = Label(root,text="Emergency")
paymentmode = Label(root,text="Payment Mode")

#Packing of Fields
name.grid(row=1,column=2)
mobile.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)
paymentmode.grid(row=5,column=2)

#Variable for storing data
namevalue = StringVar
mobilevalue = StringVar
gendervalue = StringVar
emergencyvalue = StringVar
paymentvalue = StringVar
checkvalue = IntVar

#Creating entry field
nameentry = Entry(root, textvariable = namevalue)
mobileentry = Entry(root, textvariable = mobilevalue)
genderentry = Entry(root, textvariable = gendervalue)
emergencyentry = Entry(root, textvariable = emergencyvalue)
paymententry = Entry(root, textvariable = paymentvalue)

#Packing entry field
nameentry.grid(row=1,column=3)
mobileentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
emergencyentry.grid(row=4,column=3)
paymententry.grid(row=5,column=3)

#Creating checkbox
checkbtn = Checkbutton(text="remember me?", variable = checkvalue)
checkbtn.grid(row=6,column=3)

#Submit button
Button(text="Submit",command=getvals).grid(row=7,column=3)




root.mainloop()