from tkinter import *
from tkinter import messagebox
from user_data import UserData

class Gui:
    def __init__(self):
        self.ud = UserData()
        self.BACKGROUND_COLOR = "#9DD6DF"
        self.f_name = ""
        self.l_name = ""
        self.number = ''
        self.email = ''
        self.re_enter = ''
        self.userdata()

    def userdata(self):
        windows = Tk()
        windows.config(padx=20, pady=20, bg=self.BACKGROUND_COLOR)
        windows.title("Trip Planner")

        label = Label(text="First Name: ", font=("Ariel", 16, "bold"), bg=self.BACKGROUND_COLOR)
        self.f_name = Entry(width=20)

        label2 = Label(text="Last Name", font=("Ariel", 16, "bold"), bg=self.BACKGROUND_COLOR)
        self.l_name = Entry(width=20)

        label3 = Label(text="Phone No.", font=("Ariel", 16, "bold"), bg=self.BACKGROUND_COLOR)
        self.number = Entry(width=20)
        label4 = Label(text="Email", font=("Ariel", 16, "bold"), bg=self.BACKGROUND_COLOR)
        self.email = Entry(width=20)
        label5 = Label(text="Confirm Email:", font=("Ariel", 16, "bold"), bg=self.BACKGROUND_COLOR)
        self.re_enter = Entry(width=20)

        submit = Button(text="Submit", width=30,command = self.data_exchange)

        label.grid(row=0, column=0, sticky=W)
        label2.grid(row=1, column=0,sticky=W)
        label3.grid(row=2, column=0, sticky=W)
        label4.grid(row=3, column=0,sticky=W)
        label5.grid(row=4, column=0, sticky=W)
        self.f_name.grid(row=0, column=1)
        self.l_name.grid(row=1, column=1)
        self.number.grid(row=2, column=1)
        self.email.grid(row=3,column=1)
        self.re_enter.grid(row=4, column=1)
        submit.grid(row=5,column=0,columnspan=2)
        windows.mainloop()

    def data_exchange(self):
        if self.email.get() == self.re_enter.get():
            is_ok = messagebox.askokcancel(title='User Data',
                                           message=f"First Name: {self.f_name.get()}\nLast Name: {self.l_name.get()}"
                                                   f"\nEmail: {self.email.get()}\nContact no.: {self.number.get()}\n\nProceed to save?")
            if is_ok:
                self.ud.input(self.f_name.get(),self.l_name.get(),self.email.get(),self.number.get())
                messagebox.showinfo(title="Success", message="Congrats!! You are added to Club")
        else:
            messagebox.showinfo(title="OOps", message="Email could not be confirmed!!")


g =Gui()
