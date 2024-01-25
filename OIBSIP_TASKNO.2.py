import tkinter as tk
from tkinter import *
from tkinter import messagebox
cal=tk.Tk()
cal.geometry("400x500")
cal.title("BMI CALCULATOR")
cal.config(bg="Light blue")
img_icon=PhotoImage(file="C:\\Users\\kriti\\OneDrive\\Desktop\\BMI Calculator\\BMIPIC.gif")
cal.iconphoto(False,img_icon)
def bmi():
    try:
        w=weight.get()
        h=height.get()
        m=h/100
        bmi=float(format(w/(m**2),".2f"))
        bmi_label.config(text="BMI: "+" "+str(bmi),font=("times new roman",18,'bold'))
        messages(bmi)
    except ZeroDivisionError:
        messagebox.showerror(title="Error",message="Height or Weight can't be Zero")
def messages(bmi):
    if(bmi<=18.5):
        msg_label.config(text="you are are underweight",bg="yellow",fg="Black",font=("Times new roman",18,"bold"))
    elif(bmi>18.5 and bmi<=24.9):
        msg_label.config(text="you are are Normal",bg="Green",fg="Black",font=("Times new roman",18,"bold"))
    elif(bmi>24.9 and bmi<=30):
        msg_label.config(text="you are are overweight",bg="pink",fg="Black",font=("Times new roman",18,"bold"))
    else:
        msg_label.config(text="you are suffering from obesity",bg="Red",fg="Black",font=("Times new roman",18,"bold"))  
    
      
top=Label(cal,text="BMI CALCULATOR",font=("Times New Roman",18,'bold'),fg="Red",bg="Black",width=28,height=4)
top.pack()
height=DoubleVar
weight=DoubleVar
height=tk.Scale(cal,variable=height,length=500,from_=0,to=3000,orient=HORIZONTAL, font=("Times New Roman", 18, 'bold'),troughcolor="magenta", label="HEIGHT(in cm)")
height.pack(padx=20, pady=20)
weight=tk.Scale(cal,variable=weight,length=500,from_=0,to=500,resolution=0.1,orient=HORIZONTAL, font=("Times New Roman", 18, 'bold'),troughcolor="blue", label="WEIGHT(in kg)")
weight.pack(padx=20, pady=4)
button1=tk.Button(cal,text="CALCULATE BMI",bg="black",fg="White",font=("Times new roman",18,'bold'),command=bmi)
button1.pack(padx=10,pady=4)
bmi_label=Label(cal,font=("times new roman",18,'bold'))
bmi_label.pack(padx=10,pady=4)
msg_label=Label(cal,font=("Times new roman",18,'bold'))
msg_label.pack(padx=10,pady=4)
cal.mainloop()