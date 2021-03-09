from tkinter import *

root=Tk()
root.title("Simple Calculator")
root.config(bg="black")




# input box 

e=Entry(root,width="40",borderwidth="8",font=("Arial",15,"bold"))
e.insert(0,"")
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

#function
def button_click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))
def button_clear():
    e.delete(0,END)
def button_add():
    first_num=e.get()
    e.delete(0,END)
    e.insert(0,str(first_num)+ " + ")
    global f_num
    global math
    math="add"
    f_num=int(first_num)
def button_equal():
    if(math=="add"):
        second_number=e.get().split(" + ")[1]
        e.delete(0,END)
        e.insert(0,int(f_num)+int(second_number))
    elif(math=="subtract"):
        second_number=e.get().split(" - ")[1]
        e.delete(0,END)
        e.insert(0,int(f_num)-int(second_number))
    elif(math=="divide"):
        second_number=e.get().split(" / ")[1]
        e.delete(0,END)
        e.insert(0,int(f_num)/int(second_number))
    elif(math=="multiply"):
        second_number=e.get().split(" x ")[1]
        e.delete(0,END)
        e.insert(0,int(f_num)*int(second_number))
    
def button_subtract():
    first_num=e.get()
    e.delete(0,END)
    e.insert(0,str(first_num)+ " - ")
    global f_num
    global math
    math="subtract"
    f_num=int(first_num)
def button_divide():
    first_num=e.get()
    e.delete(0,END)
    e.insert(0,str(first_num)+ " / ")
    global f_num
    global math
    math="divide"
    f_num=int(first_num)
def button_multiply():
    first_num=e.get()
    e.delete(0,END)
    e.insert(0,str(first_num)+ " x ")
    global f_num
    global math
    math="multiply"
    f_num=int(first_num)    
#Creating  Buttons
button_1=Button(root,text="1",padx=60,pady=20,command=lambda: button_click(1),bg="#403232",font=("Arial",15,"bold"),fg="white",bd=0,width="5",height="2")
button_2=Button(root,text="2",padx=60,pady=20,command=lambda: button_click(2),bg="#403232",font=("Arial",15,"bold"),fg="white",bd=0,width="5",height="2")
button_3=Button(root,text="3",padx=60,pady=20,command=lambda: button_click(3),bg="#403232",font=("Arial",15,"bold"),fg="white",bd=0,width="5",height="2")
button_4=Button(root,text="4",padx=60,pady=20,command=lambda: button_click(4),bg="#403232",font=("Arial",15,"bold"),fg="white",bd=0,width="5",height="2")
button_5=Button(root,text="5",padx=60,pady=20,command=lambda: button_click(5),bg="#403232",font=("Arial",15,"bold"),fg="white",bd=0,width="5",height="2")
button_6=Button(root,text="6",padx=60,pady=20,command=lambda: button_click(6),bg="#403232",font=("Arial",15,"bold"),fg="white",bd=0,width="5",height="2")
button_7=Button(root,text="7",padx=60,pady=20,command=lambda: button_click(7),bg="#403232",font=("Arial",15,"bold"),fg="white",bd=0,width="5",height="2")
button_8=Button(root,text="8",padx=60,pady=20,command=lambda: button_click(8),bg="#403232",font=("Arial",15,"bold"),fg="white",bd=0,width="5",height="2")
button_9=Button(root,text="9",padx=60,pady=20,command=lambda: button_click(9),bg="#403232",font=("Arial",15,"bold"),fg="white",bd=0,width="5",height="2")
button_0=Button(root,text="0",padx=60,pady=20,command=lambda: button_click(0),bg="#403232",font=("Arial",15,"bold"),fg="white",bd=0,width="5",height="2")

button_add=Button(root,text="+",padx=60,pady=20,command=button_add,bg="#db7900",font=("Arial",15,"bold"),width="5",height="2")
button_equal=Button(root,text="=",padx=140,pady=20,command=button_equal,bg="#db7900",font=("Arial",15,"bold"),width="7",height="2")
button_clear=Button(root,text="clear",padx=125,pady=20,command= button_clear,bg="#c2006e",font=("Arial",15,"bold"),width="10",height="2")

button_subtract=Button(root,text="-",padx=61,pady=20,command=button_subtract,bg="#db7900",font=("Arial",15,"bold"),width="5",height="2")
button_divide=Button(root,text="/",padx=63,pady=20,command=button_divide,bg="#db7900",font=("Arial",15,"bold"),width="4",height="2")
button_multiply=Button(root,text="x",padx=63,pady=20,command=button_multiply,bg="#db7900",font=("Arial",15,"bold"),width="5",height="2")


# put the buttons on the screen
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_0.grid(row=4,column=0)

button_add.grid(row=5,column=0)
button_equal.grid(row=5,column=1,columnspan=2)
button_clear.grid(row=4,column=1,columnspan=2)

button_subtract.grid(row=6,column=0)
button_divide.grid(row=6,column=1)
button_multiply.grid(row=6,column=2)


root.mainloop()