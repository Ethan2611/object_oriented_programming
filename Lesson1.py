from tkinter import *#it is the graphical library of python
window=Tk()#This will create the window of the app
window.geometry("600x600")#It is defining the width and height of the window
window.title("My First Tkinter App")
window.config(background="cyan")

heading=Label(window,text="Enfield Community College",bg="cyan",fg="black",font=("Ariel",30))
heading.place(x=15,y=15)
Name=Label(window,text="Enter the Child's Name",bg="cyan",fg="black",font=("Ariel",20))
Name.place(x=15,y=175)
name_entry=Entry(window,width=30,font=("Ariel"))
name_entry.place(x=300,y=185)
window.mainloop()#To make the output window stay on the screen
