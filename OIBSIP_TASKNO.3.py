import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import *
from tkinter import messagebox
import string
import random
import pyperclip
pw=tk.Tk()
img_icon=PhotoImage(file="C:\\Users\\kriti\\OneDrive\\Desktop\\pw generator\\pwimg.gif")
scaled_icon=img_icon.subsample(1,1)
pw.iconphoto(True,scaled_icon)
pw.geometry("500x500")
pw.title("PASSWORD GENERATOR")
pw.config(background="Black")
def generator():
    small_alpha=string.ascii_lowercase
    cap_alpha=string.ascii_uppercase
    num=string.digits
    special_char=string.punctuation
    all=small_alpha+cap_alpha+num+special_char
    pw_length=int(num_dropdown.get())
    if(select.get()==1):
        result_label.insert(0,''.join(random.sample(small_alpha,pw_length)))
    if(select.get()==2):
        result_label.insert(0,''.join(random.sample(small_alpha+cap_alpha,pw_length)))
    if(select.get()==3):
        result_label.insert(0,''.join(random.sample(all,pw_length)))
def copy_clip():
    pw_copy=result_label.get()
    pyperclip.copy(pw_copy)
top=Label(pw,text="PASSWORD LENGTH",font=("Times new roman",20,'bold'),background="Black",foreground="White")
top.pack()
selection=tk.IntVar()
num= [str(i) for i in range(0,11)]
num_dropdown=ttk.Spinbox(pw,textvariable=selection,values=num)
num_dropdown.pack(pady=50)
select=tk.IntVar()
weak_checkbox=Radiobutton(pw,text="Weak",value=1,variable=select)
weak_checkbox.pack(fill=tk.X,padx=120,pady=1)
Medium_checkbox=Radiobutton(pw,text="Medium ",value=2,variable=select)
Medium_checkbox.pack(fill=tk.X,padx=120,pady=1)
Strong_checkbox=Radiobutton(pw,text="Strong",value=3,variable=select)
Strong_checkbox.pack(fill=tk.X,padx=120,pady=1)
gen_label=tk.Button(pw,text="GENERATE",font=("Times new roman",18,'bold'),background="Black",foreground="White",command=generator)
gen_label.pack(pady=40)
result_label=Entry(pw,font=("Times new roman",18,'bold'),background="White",foreground="Black")
result_label.pack(fill=tk.X,padx=40)
copy_button=tk.Button(pw,text="COPY",font=("Times new roman",18,'bold'),background="white",foreground="Black",command=copy_clip)
copy_button.pack(pady=10)
pw.mainloop()