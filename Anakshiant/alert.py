from tkinter import *
import tkinter.messagebox
root = Tk()
tkinter.messagebox.showinfo("Window Title","Hey i need an worker ?")
answer = tkinter.messagebox.askquestion("Question 1","Are you a human ?")
if answer == "yes":
    tkinter.messagebox.showinfo("Congrats","Thank god! it;s good to know another human is out there")
    if answer == "no":
        tkinter.messagebox.shhowinfo("Alien","!00% confiremed")
root.mainloop()
