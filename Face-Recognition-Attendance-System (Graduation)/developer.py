from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2




class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
        self.root.wm_iconbitmap("camera.ico")

        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1358,height=40)

        img_top=Image.open(r"C:\Users\Alahram\Desktop\Face-Recognition-Attendance-System (Graduation)\images\large2.jpg")
        img_top=img_top.resize((1358,643),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1358,height=643)

        #=======frame============
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=900,y=0,width=440,height=600)

        
        
        #Developer info
        dev_label=Label(main_frame,text="blaa blaa blaa bla blaa blaa blaa bla blaa blaa blaa bla blaa blaa blaa bla  ",font=("times new roman",15,"bold"),bg="white")
        dev_label.place(x=0,y=5)

        
        dep_label=Label(main_frame,text="blaa blaa blaa bla blaa blaa blaa bla blaa blaa blaa bla blaa blaa blaa bla blaa blaa blaa bla blaa blaa blaa bla ",font=("times new roman",15,"bold"),bg="white")
        dep_label.place(x=0,y=40)

        
        img2=Image.open(r"C:\Users\Alahram\Desktop\Face-Recognition-Attendance-System (Graduation)\images\4.jpg")
        img2=img2.resize((500,390),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(main_frame,image=self.photoimg2)
        f_lbl.place(x=0,y=210,width=500,height=390)






if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()        