#Aashiq Adams Class 2
#Python End of Module Project
#Novermber 2020
from tkinter import *
from tkinter import messagebox as mb
from datetime import *
from random import *
import time

#Main class containing modules to run program
class Lotto:
    #initialization function which runs age confirmation page
    def __init__(self):
        #Date and time functions
        now = datetime.now()
        date = now.strftime("%d %B %Y")
        current_time = now.strftime("%H:%M %p")
        date_label_text = date+"\n"+current_time

        #Creating Tkinter widgets (only Label, Entry, anf Button were used)
        head_label = Label(root, text="Welcome to the Ithuba National Lottery program", bg="white", font="Helvetica 13 bold")
        age_label = Label(root, text="Enter your age: ", bg="white")
        date_label = Label(root, text=date_label_text, bg="white", fg="#ef3e33", font="Arial 12 bold")
        self.age_entry = Entry(root, width=3)
        self.sub_btn = Button(root, text="Submit", command=self.submit, fg="grey", state=DISABLED)
        check_label = Label(root, text="Accept T's and C's", bg="white")
        self.var = IntVar()
        check = Checkbutton(root, bg="white", activebackground="#ef3e33", bd=0, highlightthickness=0, variable= self.var, command=self.enable)

        #Tkinter widget placements
        head_label.place(x=5,y=5)
        age_label.place(x=5,y=40)
        self.age_entry.place(x=110, y=40)
        self.sub_btn.place(x=20,y=110)
        date_label.place(x=5, y=220)
        check_label.place(x=5,y=80)
        check.place(x=130,y=80)
    
    #Function to enable button on checkbox active
    def enable(self):
        if self.var.get():
            self.sub_btn.config(state=NORMAL, bg="#ef3e33", fg="white")
        else:
            self.sub_btn.config(state=DISABLED, bg="grey", fg="grey")

    #Button Functions
    #Module for Submit button
    def submit(self):
        #try/except to catch ValueError in entry
        try:
            #Checking age
            self.age = self.age_entry.get()
            age = self.age
            if int(age)>=18:
                root.destroy()
                run = self.main()
            elif int(age)<0:
                mb.showerror("Value Error","Please enter a positive number for your age")
            elif int(age)<18:
                mb.showwarning("Warning", "You are too young to enter")

        except ValueError:
            mb.showerror("Value Error", "Please only enter a number")

    #Module for main program window
    def main(self):
        #importing random module to generate lotto numbers
        import random

        #Initializing a new window
        self.master=Tk()
        master = self.master
        master.title("Ithuba National Lottery")
        master.geometry("550x350")
        master.resizable(0, 0)
        master.config(bg="#f9db17")

        #Generate 6 random non-repeating numbers
        self.win_nums = sorted(random.sample(range(1,50), 6))
        print("for developer testing - winning numbers:",self.win_nums)

        #background 18+ image creation and placement
        icon_canvas = Canvas(master, width=500, height=130, bg="white",bd=0, highlightthickness=0)
        icon_canvas.place(x=20,y=0)
        icon = PhotoImage(file="logo.png")
        icon_canvas.create_image(0, 0, anchor=NW, image=icon)

        #Creating Tkinter widgets (only Label, Entry, and Button were used)
        user_input_label = Label(master, text="Enter your lucky numbers here:           -            -           -           -           -", bg="#f9db17", fg="#221d1f", font="Helvetica 12 bold")
        self.result_label = Label(master, bg="#f9db17", fg="#221d1f", font="Helvetica 15 bold italic")
        self.main_date_label = Label(master, bg="#f9db17", fg="#221d1f", font="Helvetica 13 bold")
        self.num_1 = Entry(master, width=3)
        self.num_2 = Entry(master, width=3)
        self.num_3 = Entry(master, width=3)
        self.num_4 = Entry(master, width=3)
        self.num_5 = Entry(master, width=3)
        self.num_6 = Entry(master, width=3)
        confirm_btn = Button(master, text="Confirm", command=self.calc, bg="#00a66a", fg="whitesmoke", font="Calibri 13")#green
        clear_btn = Button(master, text="Reset", command=self.clear, bg="#099eda", fg="whitesmoke", font="Calibri 13")#blue
        exit_btn = Button(master, text="Quit", command=master.destroy, bg="#ef2c43",fg="whitesmoke", font="Calibri 13")#red

        #Date and time functions
        now = datetime.now()
        date = now.strftime("%d %B %Y")
        current_time = now.strftime("%H:%M %p")
        date_time =  date+"\n"+current_time
        self.main_date_label['text']= date_time

        #tkinter placements on master 
        user_input_label.place(x=0, y=152)
        self.num_1.place(x=250,y=150)
        self.num_2.place(x=300,y=150)
        self.num_3.place(x=350,y=150)
        self.num_4.place(x=400,y=150)
        self.num_5.place(x=450,y=150)
        self.num_6.place(x=500,y=150)
        confirm_btn.place(x=250,y=190)
        clear_btn.place(x=450,y=190)
        self.result_label.place(x=5,y=250)
        exit_btn.place(x=10,y=300)
        self.main_date_label.place(x=90,y=303)

        #loop main window
        master.mainloop()

    #Function to do calculations
    def calc(self):
        #Doctest Testing
        '''
        >>> Lotto.calc(self)
        True
        '''

        #update current time
        now = datetime.now()
        date = now.strftime("%d %B %Y")
        current_time = now.strftime("%H:%M %p")
        date_time =  date+"\n"+current_time
        self.main_date_label['text'] = date_time

        #try/except to catch ValueError on user entry 
        try:
            #Fetching user numbers from Entry fields
            a = int(self.num_1.get())
            b = int(self.num_2.get())
            c = int(self.num_3.get())
            d = int(self.num_4.get())
            e = int(self.num_5.get())
            f = int(self.num_6.get())

            #Creating list for user entry numbers
            user_nums = sorted([a,b,c,d,e,f])
        except ValueError:
            mb.showerror("Value Error","Please only enter numbers and do not leave fields blank")
        
        #check for duplicates, restart if detected
        user_nums = list(dict.fromkeys(user_nums))
        if len(user_nums)<6:
            mb.showerror("Duplicate detected","Make sure you enter 6 DIFFERENT numbers")
            self.master.destroy()
            run = self.main()
            pass

        #Check if numbers in range
        for i in user_nums:
            if i>49 or i<1:
                mb.showerror("Range Error", "Make sure to enter only numbers between 1 and 49")

        #Counting correct lotto numbers
        counter=0
        for i in user_nums:
            if i in self.win_nums:
                counter+=1
        
        #Dictionary for storing prizes accoriding to correct numbers
        #Displaying result on label
        prizes = {0:"0",1:"0",2:"20",3:"100.50",4:"2384",5:"8584",6:"10000000"}

        if counter<=1:
            result = "You only got "+str(counter)+" number(s) correct and did not win"
            self.result_label['text'] = result

        #checking if money was won to display a gif
        if counter>1:
            #saving text to save later
            self.text = "|Date: "+date+"\n|Time: "+current_time+"\n|Age: "+str(self.age)+"\n|Winning numbers: "+str(self.win_nums)+"\n|User numbers: "+str(user_nums)+"\n|Correct numbers: "+str(counter)+"\n|Amount won: R"+str(prizes[counter])+"\n*********************************************\n"

            #gif background using Toplevel so that it stays attached to main window
            self.win = Toplevel()
            win = self.win
            win.title("WINNER!")
            win.geometry("400x302")
            win.resizable(0,0)
            win.config(bg='black')
            
            #function for sliding words 
            def shift():
                x1,y1,x2,y2 = canvas.bbox("marquee")
                if(x2<0 or y1<0):
                    x1 = canvas.winfo_width()
                    y1 = canvas.winfo_height()//2
                    canvas.coords("marquee",x1,y1)
                else:
                    canvas.move("marquee", -2, 0)
                canvas.after(1000//fps,shift)

            #Creating canvas for horizontal slide of words
            canvas=Canvas(win,bg='black')
            canvas.place(x=-1,y=-1)
            text_var="YOU WIN!!! You have won R"+str(prizes[counter])+"!"
            text=canvas.create_text(0,-75,text=text_var,font=('Times New Roman',20,'bold'),fill='#f9db17',tags=("marquee",),anchor='w')
            canvas['width']=400
            canvas['height']=40
            fps=70
            shift()
            
            #Creating and placing claim button 
            btn = Button(win, text="Claim", bg="#f9db17", command=self.claim_win)
            btn.place(x=180, y=270)

            #Creating frames from gif file 
            frame_count = 17
            frames = [PhotoImage(file='moola.gif',format = 'gif -index %i' %(i)) for i in range(frame_count)]
            
            #function to animate gif frames
            def win_img(ind):
                frame = frames[ind]
                ind += 1
                if ind == frame_count:
                    ind = 0
                gif_label.configure(image=frame)
                win.after(100, win_img, ind)

            #label for gif background
            gif_label = Label(win, bg='black')
            gif_label.place(x=-1,y=40)
            win.after(0, win_img, 0)

        else:
            mb.showinfo("Unlucky","Unfortunately you haven't won anything, but you can try again by clicking reset")
            #File handling
            f = open('results_file.txt','a+')
            self.text = "|Date: "+date+"\n|Time: "+current_time+"\n|Age: "+str(self.age)+"\n|Winning numbers: "+str(self.win_nums)+"\n|User numbers: "+str(user_nums)+"\n|Correct numbers: "+str(counter)+"\n|Amount won: R"+str(prizes[counter])+"\n*********************************************\n"
            f.write(self.text)
            f.close()
        return True

    #Module to clear displays
    def clear(self):
        #generate new set of winning numbers
        import random
        self.win_nums = sorted(random.sample(range(1,50), 6))
        print("for developer testing - winning numbers:",self.win_nums)

        #update current time
        now = datetime.now()
        date = now.strftime("%d %B %Y")
        current_time = now.strftime("%H:%M %p")
        date_time =  date+"\n"+current_time
        self.main_date_label['text']= date_time

        #Clearing various widgets
        self.num_1.delete(0, 'end')
        self.num_2.delete(0, 'end')
        self.num_3.delete(0, 'end')
        self.num_4.delete(0, 'end')
        self.num_5.delete(0, 'end')
        self.num_6.delete(0, 'end')
        self.result_label['text'] = ""

    #Function to run claiming window
    def claim_win(self):
        #Closing gif window and opening claim window
        self.win.destroy()
        self.claim = Toplevel()
        claim = self.claim
        claim.title("Claim Winnings")
        claim.geometry("300x250")
        claim.config(bg="#00a66a")
        claim.resizable(0, 0)

        #creating labels and entries
        instruction_label = Label(claim, text="Enter your details below", font="Helvetica 18 bold", bg="#00a66a")
        name_label = Label (claim, text="Name:", bg="#00a66a")
        surname_label = Label (claim, text="Surname:", bg="#00a66a")
        tel_label = Label(claim, text="Telephone:", bg="#00a66a")
        email_label = Label(claim, text="E-mail:", bg="#00a66a")
        self.name = Entry(claim)
        self.surname = Entry(claim)
        self.tel = Entry(claim)
        self.email = Entry(claim)
        submit_btn = Button(claim, text="Submit", command=self.save_info)

        #placing widgets on claim window
        instruction_label.place(x=5,y=5)
        name_label.place(x=5,y=40)
        surname_label.place(x=5,y=70)
        tel_label.place(x=5,y=100)
        email_label.place(x=5,y=130)
        self.name.place(x=100,y=40)
        self.surname.place(x=100,y=70)
        self.tel.place(x=100,y=100)
        self.email.place(x=100,y=130)
        submit_btn.place(x=120,y=180)

    #Function to append winners' data to txt file
    def save_info(self):
        #fetching data from entry widgets
        name = self.name.get()
        surname = self.surname.get()
        tel = self.tel.get()
        email = self.email.get()

        #Checking if fields blank
        if tel != "" and name != "" and surname != "" and email != "":
            #error handling on numeric entries
            try:
                tel = int(tel)
                #File handling
                f = open('results_file.txt','a+')
                user_data = "|Name: "+name+"\n|Surname: "+surname+"\n|Telephone: "+str(tel)+"\n|E-mail: "+email+"\n"
                combined = user_data + self.text
                f.write(combined)
                f.close()

                #closing message
                mb.showinfo("Claim Request Submitted","Thank you for playing")
                self.clear()
                self.claim.destroy()
            except ValueError:
                mb.showerror("Value Error","Only use numbers for telephone")
                self.claim.destroy()
                self.claim_win()  
        else:
            mb.showerror("Error","Do not leave any fields blank")
            self.claim.destroy()
            self.claim_win() 


#Tkinter initialization 
root = Tk()
root.title("Ithuba National Lottery - Confirm Age")
root.geometry("422x272")
root.resizable(0, 0) 
root.config(bg="white")

#background 18+ image creation and placement
icon_canvas = Canvas(root, width=300, height=300, bg="white",bd=0, highlightthickness=0)
icon_canvas.place(x=120,y=-3)
icon = PhotoImage(file="18.png")
icon_canvas.create_image(0, 0, anchor=NW, image=icon)

#looping root and running main class
program = Lotto()
root.mainloop()