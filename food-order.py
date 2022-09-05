import random
from tkinter import *
import tkinter as tk
import datetime as dt
date=dt.datetime.now()
window=tk.Tk()
window.geometry("1500x800")
window.title("Restaurant Management System")
window.configure(background="#42032C")
dlab=Label(window,text=f"{date:%A, %B %d, %Y}",font=("Calibri",25,"bold"),bg="#42032C",fg="#F1EFDC",height=2,width=50)
dlab.pack(padx=80,pady=100)
lbl1=tk.Label(window,text="WELCOME TO WOW FOODS",bg="#D36B00",fg="#F1EFDC",font=("times",30,"bold"),width=100,height=2)
lbl1.place(x=-470,y=5)

def data(order,price):
    count=random.randint(11111,99999)
   
    file=open("order-details.txt","a")
    file.write("\n---------------------------------------------------------------------------------------------------------------------")
    file.write("\n ORDER NO: \t"+str(count))
    file.write("\n ORDER: \t"+order)
    file.write("\n PRICE: \t"+price)
    file.write("\n---------------------------------------------------------------------------------------------------------------------")
    lblbn=tk.Label(window,text="ORDER NO #"+str(count),bg="#42032C",fg="#F1EFDC",font=("times",30,"bold"),width=50,height=2)
    lblbn.place(x=100,y=200)
    
    

def breakfast():
    lbl1.destroy()
    dlab.destroy()
    lbl3.destroy()
    lbl4.destroy()
    lbl2.destroy()
    lblbk=tk.Label(window,text="ORDER BREAKFAST",bg="#D36B00",fg="#F1EFDC",font=("times",30,"bold"),width=100,height=2)
    lblbk.place(x=-470,y=5)
    lblbn=tk.Label(window,text="",bg="#42032C",fg="#F1EFDC",font=("times",30,"bold"),width=50,height=2)
    lblbn.place(x=100,y=300)
    lblbn=tk.Label(window,text="",bg="#42032C",fg="#F1EFDC",font=("times",30,"bold"),width=50,height=2)
    lblbn.place(x=100,y=200)
    
    
    
    
    #order function
    def idly():
        order="idly"
        price="50"
        lbli.destroy()
        lbld.destroy()
        lblp.destroy()
        lblbt=tk.Label(window,text="THANKS FOR ORDERING ;)",bg="#D36B00",fg="#F1EFDC",font=("times",30,"bold"),width=100,height=2)
        lblbt.place(x=-470,y=5)
        lblbn=tk.Label(window,text="Your order for"" "+order+" is confirmed... \n & Please pay Rs:"+price+" , when you recieve the order.",bg="#42032C",fg="#F1EFDC",font=("times",30,"bold"),width=50,height=2)
        lblbn.place(x=100,y=300)
        lblh=tk.Button(window,text="RETURN",bg="#D36B00",fg="#F1EFDC",font=("times",30,"bold"),command=breakfast)
        lblh.place(x=500,y=650)
        lble=tk.Button(window,text="EXIT",bg="#D36B00",fg="#F1EFDC",font=("times",30,"bold"),command=exit)
        lble.place(x=800,y=650)
        data(order,price)
        

    def dosa():
        order="dosa"
        price="70"
        lbli.destroy()
        lbld.destroy()
        lblp.destroy()
        lblbt=tk.Label(window,text="THANKS FOR ORDERING ;)",bg="#D36B00",fg="#F1EFDC",font=("times",30,"bold"),width=100,height=2)
        lblbt.place(x=-470,y=5)
        lblbn=tk.Label(window,text="Your order for"" "+order+" is confirmed... \n & Please pay Rs:"+price+" , when you recieve the order.",bg="#42032C",fg="#F1EFDC",font=("times",30,"bold"),width=50,height=2)
        lblbn.place(x=100,y=300)
        lblh=tk.Button(window,text="RETURN",bg="#D36B00",fg="#F1EFDC",font=("times",30,"bold"),command=breakfast)
        lblh.place(x=500,y=650)
        lble=tk.Button(window,text="EXIT",bg="#D36B00",fg="#F1EFDC",font=("times",30,"bold"),command=exit)
        lble.place(x=800,y=650)
        data(order,price) 

    def poori():
        order="poori"
        price="60"
        lbli.destroy()
        lbld.destroy()
        lblp.destroy()
        lblbt=tk.Label(window,text="THANKS FOR ORDERING ;)",bg="#D36B00",fg="#F1EFDC",font=("times",30,"bold"),width=100,height=2)
        lblbt.place(x=-470,y=5)
        lblbn=tk.Label(window,text="Your order for"" "+order+" is confirmed... \n & Please pay Rs:"+price+" , when you recieve the order.",bg="#42032C",fg="#F1EFDC",font=("times",30,"bold"),width=50,height=2)
        lblbn.place(x=100,y=300)
        lblh=tk.Button(window,text="RETURN",bg="#D36B00",fg="#F1EFDC",font=("times",30,"bold"),command=breakfast)
        lblh.place(x=500,y=650)
        lble=tk.Button(window,text="EXIT",bg="#D36B00",fg="#F1EFDC",font=("times",30,"bold"),command=exit)
        lble.place(x=800,y=650)
        data(order,price)



    #menu
    lbli=tk.Button(window,text="IDLY & VADA",bg="#D36B00",fg="#F1EFDC",font=("times",30,"bold"),command=idly)
    lbli.place(x=100,y=350)
    lbld=tk.Button(window,text="DOSA",bg="#D36B00",fg="#F1EFDC",font=("times",30,"bold"),command=dosa)
    lbld.place(x=650,y=350)
    lblp=tk.Button(window,text="POORI",bg="#D36B00",fg="#F1EFDC",font=("times",30,"bold"),command=poori)
    lblp.place(x=1100,y=350)

def lunch():
    lbl1.destroy()
    dlab.destroy()
    lbl3.destroy()
    lbl4.destroy()
    lbl2.destroy()
    lblbk=tk.Label(window,text="ORDER LUNCH",bg="#D36B00",fg="#F1EFDC",font=("times",30,"bold"),width=100,height=2)
    lblbk.place(x=-470,y=5)
    lblbn=tk.Label(window,text="",bg="#42032C",fg="#F1EFDC",font=("times",30,"bold"),width=50,height=2)
    lblbn.place(x=100,y=300)
    lblbn=tk.Label(window,text="",bg="#42032C",fg="#F1EFDC",font=("times",30,"bold"),width=50,height=2)
    lblbn.place(x=100,y=200)
    
    #order function
    def anna():
        order="anna sambar"
        price="50"
        lbli.destroy()
        lbld.destroy()
        lblp.destroy()
        lblbt=tk.Label(window,text="THANKS FOR ORDERING ;)",bg="#D36B00",fg="#F1EFDC",font=("times",30,"bold"),width=100,height=2)
        lblbt.place(x=-470,y=5)
        lblbn=tk.Label(window,text="Your order for"" "+order+" is confirmed... \n & Please pay Rs:"+price+" , when you recieve the order.",bg="#42032C",fg="#F1EFDC",font=("times",30,"bold"),width=50,height=2)
        lblbn.place(x=100,y=300)
        lblh=tk.Button(window,text="RETURN",bg="#D36B00",fg="#F1EFDC",font=("times",30,"bold"),command=lunch)
        lblh.place(x=500,y=650)
        lble=tk.Button(window,text="EXIT",bg="#D36B00",fg="#F1EFDC",font=("times",30,"bold"),command=exit)
        lble.place(x=800,y=650)
        data(order,price)

    def ragi():
        order="ragi ball"
        price="40"
        lbli.destroy()
        lbld.destroy()
        lblp.destroy()
        lblbt=tk.Label(window,text="THANKS FOR ORDERING ;)",bg="#D36B00",fg="#F1EFDC",font=("times",30,"bold"),width=100,height=2)
        lblbt.place(x=-470,y=5)
        lblbn=tk.Label(window,text="Your order for"" "+order+" is confirmed... \n & Please pay Rs:"+price+" , when you recieve the order.",bg="#42032C",fg="#F1EFDC",font=("times",30,"bold"),width=50,height=2)
        lblbn.place(x=100,y=300)
        lblh=tk.Button(window,text="RETURN",bg="#D36B00",fg="#F1EFDC",font=("times",30,"bold"),command=lunch)
        lblh.place(x=500,y=650)
        lble=tk.Button(window,text="EXIT",bg="#D36B00",fg="#F1EFDC",font=("times",30,"bold"),command=exit)
        lble.place(x=800,y=650)
        data(order,price)

    def curd():
        order="curd rice"
        price="30"
        lbli.destroy()
        lbld.destroy()
        lblp.destroy()
        lblbt=tk.Label(window,text="THANKS FOR ORDERING ;)",bg="#D36B00",fg="#F1EFDC",font=("times",30,"bold"),width=100,height=2)
        lblbt.place(x=-470,y=5)
        lblbn=tk.Label(window,text="Your order for"" "+order+" is confirmed... \n & Please pay Rs:"+price+" , when you recieve the order.",bg="#42032C",fg="#F1EFDC",font=("times",30,"bold"),width=50,height=2)
        lblbn.place(x=100,y=300)
        lblh=tk.Button(window,text="RETURN",bg="#D36B00",fg="#F1EFDC",font=("times",30,"bold"),command=lunch)
        lblh.place(x=500,y=650)
        lble=tk.Button(window,text="EXIT",bg="#D36B00",fg="#F1EFDC",font=("times",30,"bold"),command=exit)
        lble.place(x=800,y=650)
        data(order,price)



    #menu
    lbli=tk.Button(window,text="ANNA SAMBAR",bg="#D36B00",fg="#F1EFDC",font=("times",30,"bold"),command=anna)
    lbli.place(x=100,y=350)
    lbld=tk.Button(window,text="RAGI BALL",bg="#D36B00",fg="#F1EFDC",font=("times",30,"bold"),command=ragi)
    lbld.place(x=650,y=350)
    lblp=tk.Button(window,text="CURD RICE",bg="#D36B00",fg="#F1EFDC",font=("times",30,"bold"),command=curd)
    lblp.place(x=1100,y=350)


def dinner():
    lbl1.destroy()
    dlab.destroy()
    lbl3.destroy()
    lbl4.destroy()
    lbl2.destroy()
    lblbk=tk.Label(window,text="ORDER DINNER",bg="#D36B00",fg="#F1EFDC",font=("times",30,"bold"),width=100,height=2)
    lblbk.place(x=-470,y=5)
    lblbn=tk.Label(window,text="",bg="#42032C",fg="#F1EFDC",font=("times",30,"bold"),width=50,height=2)
    lblbn.place(x=100,y=300)
    lblbn=tk.Label(window,text="",bg="#42032C",fg="#F1EFDC",font=("times",30,"bold"),width=50,height=2)
    lblbn.place(x=100,y=200)
    
    #order function
    def roti():
        order="roti curry"
        price="70"
        lbli.destroy()
        lbld.destroy()
        lblp.destroy()
        lblbt=tk.Label(window,text="THANKS FOR ORDERING ;)",bg="#D36B00",fg="#F1EFDC",font=("times",30,"bold"),width=100,height=2)
        lblbt.place(x=-470,y=5)
        lblbn=tk.Label(window,text="Your order for"" "+order+" is confirmed... \n & Please pay Rs:"+price+" , when you recieve the order.",bg="#42032C",fg="#F1EFDC",font=("times",30,"bold"),width=50,height=2)
        lblbn.place(x=100,y=300)
        lblh=tk.Button(window,text="RETURN",bg="#D36B00",fg="#F1EFDC",font=("times",30,"bold"),command=dinner)
        lblh.place(x=500,y=650)
        lble=tk.Button(window,text="EXIT",bg="#D36B00",fg="#F1EFDC",font=("times",30,"bold"),command=exit)
        lble.place(x=800,y=650)
        data(order,price)

    def friedrice():
        order="fried rice"
        price="70"
        lbli.destroy()
        lbld.destroy()
        lblp.destroy()
        lblbt=tk.Label(window,text="THANKS FOR ORDERING ;)",bg="#D36B00",fg="#F1EFDC",font=("times",30,"bold"),width=100,height=2)
        lblbt.place(x=-470,y=5)
        lblbn=tk.Label(window,text="Your order for"" "+order+" is confirmed... \n & Please pay Rs:"+price+" , when you recieve the order.",bg="#42032C",fg="#F1EFDC",font=("times",30,"bold"),width=50,height=2)
        lblbn.place(x=100,y=300)
        lblh=tk.Button(window,text="RETURN",bg="#D36B00",fg="#F1EFDC",font=("times",30,"bold"),command=dinner)
        lblh.place(x=500,y=650)
        lble=tk.Button(window,text="EXIT",bg="#D36B00",fg="#F1EFDC",font=("times",30,"bold"),command=exit)
        lble.place(x=800,y=650)
        data(order,price)

    def noodles():
        order="noodles"
        price="60"
        lbli.destroy()
        lbld.destroy()
        lblp.destroy()
        lblbt=tk.Label(window,text="THANKS FOR ORDERING ;)",bg="#D36B00",fg="#F1EFDC",font=("times",30,"bold"),width=100,height=2)
        lblbt.place(x=-470,y=5)
        lblbn=tk.Label(window,text="Your order for"" "+order+" is confirmed... \n & Please pay Rs:"+price+" , when you recieve the order.",bg="#42032C",fg="#F1EFDC",font=("times",30,"bold"),width=50,height=2)
        lblbn.place(x=100,y=300)
        lblh=tk.Button(window,text="RETURN",bg="#D36B00",fg="#F1EFDC",font=("times",30,"bold"),command=dinner)
        lblh.place(x=500,y=650)
        lble=tk.Button(window,text="EXIT",bg="#D36B00",fg="#F1EFDC",font=("times",30,"bold"),command=exit)
        lble.place(x=800,y=650)
        data(order,price)



    #menu
    lbli=tk.Button(window,text="ROTI CURRY",bg="#D36B00",fg="#F1EFDC",font=("times",30,"bold"),command=roti)
    lbli.place(x=100,y=350)
    lbld=tk.Button(window,text="FRIED RICE",bg="#D36B00",fg="#F1EFDC",font=("times",30,"bold"),command=friedrice)
    lbld.place(x=600,y=350)
    lblp=tk.Button(window,text="NOODLES",bg="#D36B00",fg="#F1EFDC",font=("times",30,"bold"),command=noodles)
    lblp.place(x=1100,y=350)

    
    

















lbl2=tk.Button(window,text="BREAKFAST",bg="#D36B00",fg="#F1EFDC",font=("times",30,"bold"),command=breakfast)
lbl2.place(x=100,y=350)
lbl3=tk.Button(window,text="LUNCH",bg="#D36B00",fg="#F1EFDC",font=("times",30,"bold"),command=lunch)
lbl3.place(x=650,y=350)
lbl4=tk.Button(window,text="DINNER",bg="#D36B00",fg="#F1EFDC",font=("times",30,"bold"),command=dinner)
lbl4.place(x=1100,y=350)
lbl1=tk.Label(window,text="DELICOUS FOOD ON THE GO..",bg="#D36B00",fg="#F1EFDC",font=("times",30,"bold"),width=100,height=2)
lbl1.place(x=-450,y=700)
mainloop()

