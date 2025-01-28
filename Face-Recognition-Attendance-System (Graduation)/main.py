from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_Recgonition
from attendance import Attendance
from developer import Developer
from help import Help
import tkinter
from time import strftime
from datetime import datetime


class Face_Recognition_System:
    def __init__(self,root):
        
        self.root=root
        self.root.geometry("{}x{}+0+0".format(root.winfo_screenwidth(),root.winfo_screenheight()))
        self.root.title("Face Recognition System")
        root.config(bg="white")
        self.root.wm_iconbitmap("camera.ico")
        

        width = int(root.winfo_screenwidth()/3)

        height = int(root.winfo_screenheight()/5)

        #First image

        img=Image.open(r"C:\Users\Alahram\Desktop\Face-Recognition-Attendance-System (Graduation)\images\1.jpg")
        img=img.resize((width,height),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lb1=Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=width,height=height)

        #Second image

        img1=Image.open(r"C:\Users\Alahram\Desktop\Face-Recognition-Attendance-System (Graduation)\images\3.jpg")
        img1=img1.resize((width,height),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lb1=Label(self.root,image=self.photoimg1)
        f_lb1.place(x=width,y=0,width=width,height=height)

        #Third image

        img2=Image.open(r"C:\Users\Alahram\Desktop\Face-Recognition-Attendance-System (Graduation)\images\2.png")
        img2=img2.resize((width,height),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lb1=Label(self.root,image=self.photoimg2)
        f_lb1.place(x=width*2,y=0,width=width,height=height)

        #Background image

        img3=Image.open(r"C:\Users\Alahram\Desktop\Face-Recognition-Attendance-System (Graduation)\images\5.jpg")
        img3=img3.resize((root.winfo_screenwidth(),root.winfo_screenheight()-height),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=int(width/3),width=root.winfo_screenwidth(),height=root.winfo_screenheight()-height)


        title_lbl= Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font =("times new roman",30,"bold"),bg="white",fg="#00008B")
        title_lbl.place(x=0,y=10,width=root.winfo_screenwidth(),height=root.winfo_screenheight()/22)


        b_size = int(root.winfo_screenwidth()/5)
        margin_size = int(root.winfo_screenwidth()/25)




        #=============time===========
        def time():
                string = strftime('%H:%M:%S %p')
                Ibl.config(text=string)
                Ibl.after(1000, time)

        Ibl = Label(title_lbl, font =('time new roman' ,22, 'bold'),background='white',foreground='#00008B',padx=50)
        Ibl.place(x=20,y=0,width=200,height=50)
        time()        





        #Student button

        img4=Image.open(r"C:\Users\Alahram\Desktop\Face-Recognition-Attendance-System (Graduation)\images\student4.jpg")
        img4=img4.resize((b_size,b_size),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img,image=self.photoimg4,cursor="hand2",command = self.student_details )
        b1.place(x=margin_size,y=margin_size,width=b_size ,height=b_size)

        b1_label=Button(bg_img,text="Student Details",command = self.student_details ,cursor="hand2",font =("times new roman",15,"bold"),bg="white",fg="#00008B")
        b1_label.place(x=margin_size,y=margin_size+b_size,width=b_size ,height=40)



        #FaceDetector button

        img5=Image.open(r"C:\Users\Alahram\Desktop\Face-Recognition-Attendance-System (Graduation)\images\student.jpg")
        img5=img5.resize((b_size,b_size),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command= self.face_data)
        b1.place(x=(margin_size*2)+b_size,y=margin_size,width=b_size ,height=b_size)

        b1_label=Button(bg_img,text="Face Detector",cursor="hand2",font =("times new roman",15,"bold"),bg="white",fg="#00008B",command= self.face_data)
        b1_label.place(x=(margin_size*2)+b_size,y=margin_size+b_size,width=b_size ,height=40)

        

        #Attendance button

        img6=Image.open(r"C:\Users\Alahram\Desktop\Face-Recognition-Attendance-System (Graduation)\images\attendance.jpg")
        img6=img6.resize((b_size,b_size),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command= self.Attendance_data)
        b1.place(x=(margin_size*3)+b_size*2,y=margin_size,width=b_size ,height=b_size)

        b1_label=Button(bg_img,text="Attendance",command= self.Attendance_data,cursor="hand2",font =("times new roman",15,"bold"),bg="white",fg="#00008B")
        b1_label.place(x=(margin_size*3)+b_size*2,y=margin_size+b_size,width=b_size ,height=40)


        #Train databutton

        img7=Image.open(r"C:\Users\Alahram\Desktop\Face-Recognition-Attendance-System (Graduation)\images\train.jpg")
        img7=img7.resize((b_size,b_size),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.train_data)
        b1.place(x=(margin_size*4)+b_size*3,y=margin_size,width=b_size ,height=b_size)

        b1_label=Button(bg_img,text="Train Data",cursor="hand2",font =("times new roman",15,"bold"),bg="white",fg="#00008B",bd=0 ,command=self.train_data )
        b1_label.place(x=(margin_size*4)+b_size*3,y=margin_size+b_size,width=b_size ,height=40)


    #=======================================================================================





        #Helpdesk button

        img8=Image.open(r"C:\Users\Alahram\Desktop\Face-Recognition-Attendance-System (Graduation)\images\help.jpg")
        img8=img8.resize((b_size,int(b_size/2)),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.help)
        b1.place(x=margin_size,y=margin_size*2+b_size,width=b_size ,height=int(b_size/2))

        b1_label=Button(bg_img,text="Help",cursor="hand2",font =("times new roman",15,"bold"),bg="white",fg="#00008B",command=self.help)
        b1_label.place(x=margin_size,y=margin_size*2+b_size,width=b_size ,height=40)


        #photos

        img9=Image.open(r"C:\Users\Alahram\Desktop\Face-Recognition-Attendance-System (Graduation)\images\photos.jpg")
        img9=img9.resize((b_size,int(b_size/2)),Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=margin_size*2+b_size,y=margin_size*2+b_size,width=b_size ,height=int(b_size/2))

        b1_label=Button(bg_img,command=self.open_img,text="photos",cursor="hand2",font =("times new roman",15,"bold"),bg="white",fg="#00008B")
        b1_label.place(x=margin_size*2+b_size,y=margin_size*2+b_size,width=b_size ,height=40)


        #developer

        img10=Image.open(r"C:\Users\Alahram\Desktop\Face-Recognition-Attendance-System (Graduation)\images\webdeveloper1.jpg")
        img10=img10.resize((b_size,int(b_size/2)),Image.Resampling.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        
        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=margin_size*3+b_size*2,y=margin_size*2+b_size,width=b_size ,height=int(b_size/2))

        b1_label=Button(bg_img,text="developer",cursor="hand2",font =("times new roman",15,"bold"),bg="white",fg="#00008B",command=self.developer_data)
        b1_label.place(x=margin_size*3+b_size*2,y=margin_size*2+b_size,width=b_size ,height=40)


        #exit

        img11=Image.open(r"C:\Users\Alahram\Desktop\Face-Recognition-Attendance-System (Graduation)\images\exit.jpg")
        img11=img11.resize((b_size,int(b_size/2)),Image.Resampling.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)
        
        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.IExit)
        b1.place(x=margin_size*4+b_size*3,y=margin_size*2+b_size,width=b_size ,height=int(b_size/2))

        b1_label=Button(bg_img,text="exit",cursor="hand2",font =("times new roman",15,"bold"),bg="white",fg="#00008B",command=self.IExit)
        b1_label.place(x=margin_size*4+b_size*3,y=margin_size*2+b_size,width=b_size ,height=40)


    def open_img(self):
        os.startfile("data")
    def IExit(self):
            self.IExit=tkinter.messagebox.askyesno("Face Recognitin","Are you sure exit this project",parent=self.root)
            if  self.IExit >0:
                self.root.destroy()
            else:
                return  
        
        #============================================== Buttons Functions ==============    

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)


    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recgonition(self.new_window)

    def Attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)


    def developer_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Developer(self.new_window) 

         

    def help(self):
            self.new_window=Toplevel(self.root)
            self.app=Help(self.new_window)          



    



if __name__== "__main__":
    root=Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
