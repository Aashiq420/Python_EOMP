from tkinter import *
from tkinter import messagebox as mb
from datetime import *
from random import *

#Button Functions
def submit():
    try:
        num = age.get()
        if int(num)>=18:
            root.destroy()
            run = lotto()
        elif int(num)<0:
            mb.showerror("Value Error","Please enter a positive number for your age")
        elif int(num)<18:
            mb.showwarning("Warning", "You are too young to enter")

    except ValueError:
        mb.showerror("Value Error", "Please only enter a number")

#Main function for all calculations
def lotto():
    import random
    #Initializing a new window
    master=Tk()
    master.title("Ithuba National Lottery")
    master.geometry("400x400")

    #generate 6 random non-repeating numbers
    win_nums = sorted(random.sample(range(1,50), 6))
    print(win_nums) 

    #tkinter stuff
    num_1 = Entry(master, width=4)
    num_2 = Entry(master, width=4)
    num_3 = Entry(master, width=4)
    num_4 = Entry(master, width=4)
    num_5 = Entry(master, width=4)
    num_6 = Entry(master, width=4)

    #tkinter placements on master
    num_1.place(x=0,y=0)
    num_2.place(x=50,y=0)
    num_3.place(x=100,y=0)
    num_4.place(x=150,y=0)
    num_5.place(x=200,y=0)
    num_6.place(x=250,y=0)

    #loop main thing
    master.mainloop()
     

#Tkinter initialization 
root = Tk()
root.title("Ithuba Lottery")
root.geometry("422x270")
root.config(bg="white")

#background 18+ image creation and placement
icon_canvas = Canvas(root, width=300, height=300, bg="white",bd=0, highlightthickness=0,)
icon_canvas.place(x=110,y=-3)
icon = PhotoImage(file="18.png")
icon_canvas.create_image(0, 0, anchor=NW, image=icon)

#Tkinter stuff
head_label = Label(root, text="Welcome to the Ithuba National Lottery program", bg="white", font="Helvetica 13 bold")
head_label.config()
age_label = Label(root, text="Enter your age: ", bg="white")
age = Entry(root, width=3)
sub_btn = Button(root, text="Submit", command=submit)

#Tkinter placements
head_label.place(x=5,y=5)
age_label.place(x=5,y=40)
age.place(x=110, y=40)
sub_btn.place(x=20,y=80)

#looping windows
root.mainloop()
