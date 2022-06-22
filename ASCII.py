# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 11:26:33 2022

@author: KarthikaYashu
"""

from tkinter import *

root=Tk()
root.title("Ascii")

root.geometry("400x400")
root.configure(background = 'light blue')

enter_word = Entry(root)
enter_word.place(relx=0.5, rely=0.4, anchor=CENTER)

label = Label(root, text = "Name in Ascii : ", bg="light yellow", fg="black")
label2 = Label(root, text = "Encrypted Name : ", bg="light yellow", fg="black")
label.place(relx=0.5, rely=0.6, anchor=CENTER)
label2.place(relx=0.5, rely=0.8, anchor=CENTER)

def asciiConverter():
    input_word = enter_word.get()
    
    for letter in input_word :
        label["text"] += str(ord(letter)) + " "
        ascii = int(ord(letter))
        encrypted = ascii - 1
        label2["text"] += str(chr(encrypted))
        
btn = Button(root, text ="Display the Ascii and Encrypted value", command= asciiConverter)
btn.place(relx=0.5, rely=0.6, anchor=CENTER)

label.place(relx=0.5, rely=0.7, anchor=CENTER)

root.mainloop()