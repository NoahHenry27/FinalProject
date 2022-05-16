###Order Organizer -- This program takes user inputs and generates a table of customer orders###

#Import tkinter library
from tkinter import *

from tkinter import messagebox

response = messagebox.askokcancel("Enter a customer's information?", "OK or Cancel?")

#Create an instance of tkinter window or frame
while response == True:
    fname=Tk()
    fname.geometry("700x300")
    fname.title("Enter the customer's first name")

    #Functions to take input from and automatically close input boxes
    def fun1():
       first=my_text_box.get("1.0","end-1c")
       print(first)
    def fun2 (Enter1): 
       fname.destroy()
    def fun3 (Enter2):
       lname.destroy()
    def fun4 (Enter3):
       num.destroy()
    def fun5 (Enter4):
       date.destroy()
    def fun6 (Enter5):
       time.destroy()
    def fun7 (Enter6):
       order.destroy()
    
    #Creating a text box widget
    my_text_box=Text(fname, height=5, width=40)
    my_text_box.pack()
    my_text_box.focus()

    #Create a button for fname
    Enter1= Button(fname, height=5, width=10, text="Enter", command=lambda: [fun1(), fun2(Enter1)])

    #command=get_input() will wait for the key to press and displays the entered text
    Enter1.pack()

    fname.mainloop()

    lname=Tk()
    lname.geometry("700x300")
    lname.title("Enter the customer's last name")

    def fun1():
       last=my_text_box.get("1.0","end-1c")
       print(last)

    #Creating a text box widget
    my_text_box=Text(lname, height=5, width=40)
    my_text_box.pack()
    my_text_box.focus()

    #Create a button for lname
    Enter2= Button(lname, height=5, width=10, text="Enter", command=lambda: [fun1(), fun3(Enter2)])

    #command=get_input() will wait for the key to press and displays the entered text
    Enter2.pack()

    lname.mainloop()

    num=Tk()
    num.geometry("700x300")
    num.title("Enter the customer's phone number (***-***-**** format)")

    def fun1():
       number=my_text_box.get("1.0","end-1c")
       print(number)

    #Creating a text box widget
    my_text_box=Text(num, height=5, width=40)
    my_text_box.pack()
    my_text_box.focus()

    #Create a button for num
    Enter3= Button(num, height=5, width=10, text="Enter", command=lambda: [fun1(), fun4(Enter3)])
 
    #command=get_input() will wait for the key to press and displays the entered text
    Enter3.pack()

    num.mainloop()

    date=Tk()
    date.geometry("700x300")
    date.title("Enter the pickup date (MM/DD/YYYY format)")

    def fun1():
       pickupdate=my_text_box.get("1.0","end-1c")
       print(pickupdate)

    #Creating a text box widget
    my_text_box=Text(date, height=5, width=40)
    my_text_box.pack()
    my_text_box.focus()

    #Create a button for date
    Enter4= Button(date, height=5, width=10, text="Enter", command=lambda: [fun1(), fun5(Enter4)])

    #command=get_input() will wait for the key to press and displays the entered text
    Enter4.pack()

    date.mainloop()

    time=Tk()
    time.geometry("700x300")
    time.title("Enter the pickup time (XX:XX AM/PM format)")

    def fun1():
       pickuptime=my_text_box.get("1.0","end-1c")
       print(pickuptime)

    #Creating a text box widget
    my_text_box=Text(time, height=5, width=40)
    my_text_box.pack()
    my_text_box.focus()

    #Create a button for time
    Enter5= Button(time, height=5, width=10, text="Enter", command=lambda: [fun1(), fun6(Enter5)])

    #command=get_input() will wait for the key to press and displays the entered text
    Enter5.pack()

    time.mainloop()

    order=Tk()
    order.geometry("700x300")
    order.title("Enter the customer's order details")

    def fun1():
       orderdetails=my_text_box.get("1.0","end-1c")
       print(orderdetails)

    #Creating a text box widget
    my_text_box=Text(order, height=5, width=40)
    my_text_box.pack()
    my_text_box.focus()

    #Create a button for order
    Enter6= Button(order, height=5, width=10, text="Enter", command=lambda: [fun1(), fun7(Enter6)])

    #command=get_input() will wait for the key to press and displays the entered text
    Enter6.pack()

    order.mainloop()

    print("------------------------------------------------")

    response = messagebox.askokcancel("Enter another customer's information?", "OK or Cancel?")

if response == False:
   print("End order list")




