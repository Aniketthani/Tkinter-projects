from tkinter import *
from tkinter import ttk

#please install the library for using wikipedia api using command  :  pip install wikipedia
import wikipedia as wiki

root=Tk()
root.title("WikiPedia Search Tool")
root.geometry("700x675")
root.minsize(700,675)
root.maxsize(700,675)
root.config(bg="#00bdaa")

def clear():
    my_entry.delete(0,END)
    my_text.delete(0.0,END)

def search():
    data = wiki.page(my_entry.get())
    #clear screen
    clear()

    #output wikipedia results to textbox

    my_text.insert(0.0,data.content) 


lf=LabelFrame(root,text="Search Wikipedia",bg="#00bdaa")
lf.pack(pady=20)
#create entry box

my_entry=Entry(lf,font=("Helvetica",20),width=47)
my_entry.pack(pady=20,padx=20)

#create Text box frame
myframe=Frame(root,bg="#00bdaa")
myframe.pack(pady=5)

#create a vertical scrollbar

text_scroll=ttk.Scrollbar(myframe)
text_scroll.pack(side=RIGHT,fill=Y)

#create horizontal scroll bar
hor_scroll=ttk.Scrollbar(myframe,orient="horizontal")
hor_scroll.pack(side=BOTTOM,fill=X)

#create Text box
my_text=Text(myframe,yscrollcommand=text_scroll.set,wrap="none",xscrollcommand=hor_scroll.set)
my_text.pack(pady=5)



#configure scrollbars
text_scroll.config(command=my_text.yview)
hor_scroll.config(command=my_text.xview)

#button frame
button_frame=Frame(root,bg="#00bdaa")
button_frame.pack(pady=10)

search_button=Button(button_frame,text="Lookup",font=("Arial",32),bg="#a80a2f",fg="white",command=search)
search_button.grid(row=0,column=0,padx=20)

clear_button=Button(button_frame,text="Clear",font=("Arial",32),bg="#a80a2f",fg="white",command=clear)
clear_button.grid(row=0,column=1,padx=20)





root.mainloop()