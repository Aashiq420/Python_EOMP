#Aashiq Adams
#Python End of Module Project
#Novermber 2020
from tkinter import *
from tkinter import messagebox as mb
from datetime import *
from random import *

class Lotto:
    #initialization function which runs age confirmation page
    def __init__(self):
        #Date and time functions
        now = datetime.now()
        date = now.strftime("%d %B %Y")
        current_time = now.strftime("%H:%M %p")
        date_label_text = date+"\n"+current_time

        #Tkinter stuff
        head_label = Label(root, text="Welcome to the Ithuba National Lottery program", bg="white", font="Helvetica 13 bold")
        age_label = Label(root, text="Enter your age: ", bg="white")
        date_label = Label(root, text=date_label_text, bg="white", fg="#ef3e33", font="Arial 12 bold")
        self.age = Entry(root, width=3)
        sub_btn = Button(root, text="Submit", command=self.submit, bg="#ef3e33", fg="white")

        #Tkinter placements
        head_label.place(x=5,y=5)
        age_label.place(x=5,y=40)
        self.age.place(x=110, y=40)
        sub_btn.place(x=20,y=80)
        date_label.place(x=5, y=220)
    #Button Functions
    def submit(self):
        try:
            self.num = self.age.get()
            num = self.num
            if int(num)>=18:
                root.destroy()
                run = self.main()
            elif int(num)<0:
                mb.showerror("Value Error","Please enter a positive number for your age")
            elif int(num)<18:
                mb.showwarning("Warning", "You are too young to enter")

        except ValueError:
            mb.showerror("Value Error", "Please only enter a number")

    #Main function for all calculations
    def main(self):
        import random
        #Initializing a new window
        master=Tk()
        master.title("Ithuba National Lottery")
        master.geometry("510x400")
        master.config(bg="#f9db17")

        #background 18+ image creation and placement
        icon_canvas = Canvas(master, width=500, height=130, bg="white",bd=0, highlightthickness=0)
        icon_canvas.place(x=0,y=0)
        icon = PhotoImage(file="logo.png")
        icon_canvas.create_image(0, 0, anchor=NW, image=icon)

        #generate 6 random non-repeating numbers
        win_nums = sorted(random.sample(range(1,50), 6))
        print(win_nums) 

        #tkinter stuff
        user_input_label = Label(master, text="Enter your lucky numbers here:             -           -           -           -           -", bg="#f9db17")
        num_1 = Entry(master, width=3)
        num_2 = Entry(master, width=3)
        num_3 = Entry(master, width=3)
        num_4 = Entry(master, width=3)
        num_5 = Entry(master, width=3)
        num_6 = Entry(master, width=3)
        x = Label(master, text=self.num)
        x.place(x=5,y=200)

        #tkinter placements on master
        user_input_label.place(x=0, y=152)
        num_1.place(x=220,y=150)
        num_2.place(x=270,y=150)
        num_3.place(x=320,y=150)
        num_4.place(x=370,y=150)
        num_5.place(x=420,y=150)
        num_6.place(x=470,y=150)

        #loop main thing
        master.mainloop()
     

#Tkinter initialization 
root = Tk()
root.title("Ithuba National Lottery - Confirm Age")
root.geometry("422x272")
root.resizable(0, 0) 
root.config(bg="white")

#background 18+ image creation and placement
icon_canvas = Canvas(root, width=300, height=300, bg="white",bd=0, highlightthickness=0,)
icon_canvas.place(x=110,y=-3)
icon = PhotoImage(file="18.png")
icon_canvas.create_image(0, 0, anchor=NW, image=icon)

#looping root and running main class
program = Lotto()
root.mainloop()
