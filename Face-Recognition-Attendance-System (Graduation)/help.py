from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import webbrowser
import turtle




class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
        self.root.wm_iconbitmap("camera.ico")
       
        title_lbl=Label(self.root,text="HELP DESK",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1358,height=40)

        img_top=Image.open(r"C:\Users\Alahram\Desktop\Face-Recognition-Attendance-System (Graduation)\images\help2.jpg")

        img_top=img_top.resize((1530,790),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1358,height=643)

        dev_label=Button(f_lbl,text="Email: ommarselim@gmail.com",font=("times new roman",15,"bold"),fg="blue",bg="white",command=self.my_open)
        dev_label.place(x=510,y=215)

        
    

    def my_open(self):
        url = "https://www.google.com"
        webbrowser.open_new(url)


if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()  