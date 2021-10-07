from tkinter import * 
import tkinter as tk
from datetime import datetime
from tkinter import messagebox
import pyshorteners



class url_shortner:

       
        def create(self):
                if self.url.get() == "":
                        messagebox.showerror("Error","Please Paste an URL")
                else:
                        self.urls = self.url.get()
                        self.s = pyshorteners.Shortener()
                        self.short_url = self.s.tinyurl.short(self.urls)
                        
                        self.output = Entry(self.root,font=('verdana',10,'bold'),fg="white",width=30,relief=GROOVE,borderwidth=2,border=2)
                        self.output.insert(END,self.short_url)
                        self.output.place(x=80,y=120)

                        
                        



        
        
        
        def __init__(self):
                self.root = tk.Tk()
                self.root.geometry('500x200')
                self.root.maxsize(500,200)
                self.root.minsize(500,200)
                self.root.title('Url Shortner [+]MH1>')
                self.root['bg'] = "white"

                self.title = Label(self.root,text="URL Shortner [+]MH1>",font=('verdana',15,'bold'),bg="Black",fg="White")
                self.title.place(x=100,y=10)
                self.title1 = Label(self.root,text="By:Moro-H4CK3R",font=('verdana',15,'bold'),bg="white",fg="Black")
                self.title1.place(x=8,y=170)
                self.date = Label(self.root,text=datetime.now().date(),fg="Black",font=('white',10,'bold'))
                self.date.place(x=400,y=5)



                Label(self.root,text="Paste Your Url Here ..",font=('verdana',20,'bold'),fg="white").place(x=50,y=50)

                self.url = Entry(self.root,width=50,bg="blue",relief=GROOVE,borderwidth=2,border=2)
                self.url.place(x=50,y=80)

                self.button = Button(self.root,relief=GROOVE,text="Create",font=('verdana',8,'bold'),bg="Black",fg="white",command=self.create)
                self.button.place(x=390,y=78)
                self.root.mainloop()










if __name__ == '__main__':
        url_shortner()