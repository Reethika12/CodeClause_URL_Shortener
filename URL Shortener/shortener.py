from tkinter import *
from PIL import Image,ImageTk
import clipboard
import validators
from pyshorteners import Shortener

def Clear():
    e.delete(0,"end")
    l.config(text="")
    
def Copy():
     clipboard.copy(l.cget("text"))
     c=Label(win,text="Copied",font=(20))
     c.pack()
     win.after(2000,c.destroy)
     
def Paste():
    e.delete(0,"end")
    e.insert(0,clipboard.paste())     
    
def Shorten():
    link=e.get()
    valid=validators.url("https://"+link)
    if(valid==True):
        short=Shortener().tinyurl.short(link)
        l.config(text=short)
    else:
        l.config(text="Invalid Address")    
         

win =Tk()
win.title("URL")
win.geometry("700x300")
win.config(bg="#32a8a2")
Label(win,text="URL SHORTENER",font="Arial 15 bold",fg="black").pack(fill="x",pady=7)

e=Entry(win,font=(20),relief="sunken")
e.place(relwidth=.6,relx=.2,rely=.2)

paste=Image.open("C:\\Users\\DELL\\OneDrive\\Desktop\\url\\paste.png")
resized_paste=paste.resize((20,20),Image.LANCZOS)
new_paste=ImageTk.PhotoImage(resized_paste)

paste_b=Button(win,image=new_paste,command=Paste)
paste_b.place(relx=.16,rely=.2)

shorten_b=Button(win,text="Shorten",command=Shorten)
shorten_b.place(relx=.4,rely=.35)

clear_b=Button(win,text="Clear",command=Clear)
clear_b.place(relx=.5,rely=.35)

l=Label(win,bg="white",font=(20),relief="sunken")
l.place(relwidth=.6,relx=.2,rely=.55)

copy=Image.open("C:\\Users\\DELL\\OneDrive\\Desktop\\url\\copy.png")
resized_copy=copy.resize((20,20),Image.LANCZOS)
new_copy=ImageTk.PhotoImage(resized_copy)

copy_b=Button(win,image=new_copy,command=Copy)
copy_b.place(relx=.16,rely=.55)


win.mainloop()