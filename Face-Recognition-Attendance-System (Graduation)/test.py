import tkinter as tk
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
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
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog



root =tk.Tk()
root.geometry("600x400")
root.title('Face Recognition System')
root.state('zoomed')
root.wm_iconbitmap("camera.ico")






def add_data():
    if var_dep.get() == "Select department" or var_std_name.get() == "" or var_std_id.get()=="":
        messagebox.showerror("Error","All fields are required",parent=root)
    else:
        try:
            conn = mysql.connector.connect(host="localhost",username="root",password="Test@123",database="face_recognizer")
            my_cursor =conn.cursor()
            my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                var_dep.get(),
                var_course.get(),
                var_year.get(),
                var_semester.get(),
                var_std_id.get(),
                var_std_name.get(),
                var_div.get(),
                var_roll.get(),
                var_gender.get(),
                var_dob.get(),
                var_email.get(),
                var_phone.get(),
                var_address.get(),
                var_teacher.get(),
                var_radio1.get()
            ))
            conn.commit()
            fetch_data()
            conn.close()
            messagebox.showinfo("Success","Student details has been added succeffully",parent=root)
        except Exception as es:
            messagebox.showerror("error" , f"Due to : {str(es)}",parent=root)


#===============================================================================
def fetch_data():
    conn = mysql.connector.connect(host="localhost",username="root",password="Test@123",database="face_recognizer")
    my_cursor =conn.cursor()
    my_cursor.execute("select * from student")
    data = my_cursor.fetchall()

    if len(data)!= 0:
        student_table.delete(*student_table.get_children())
        for i in data:
            student_table.insert("", END , values=i)
        conn.commit()
    conn.close()


#============================================ get cursor ================

def get_cursor(event=""):
    cursor_focus=student_table.focus()
    content=student_table.item(cursor_focus)
    data=content["values"]
    # print(data)
    var_dep.set(data[0])
    var_course.set(data[1])
    var_year.set(data[2])
    var_semester.set(data[3])
    var_std_id.set(data[4])
    var_std_name.set(data[5])
    var_div.set(data[6])
    var_roll.set(data[7])
    var_gender.set(data[8])
    var_dob.set(data[9])
    var_email.set(data[10])
    var_phone.set(data[11])
    var_address.set(data[12])
    var_teacher.set(data[13])
    var_radio1.set(data[14])


    #=========== update function ===========


def update_data():
    if var_dep.get() == "Select department" or var_std_name.get() == "" or var_std_id.get()=="":
        messagebox.showerror("Error","All fields are required",parent=root)
    else:
        try:
            Update = messagebox.askyesno("Update","Are you sure you want to Update this student details",parent=root)

            if Update>0:

                conn = mysql.connector.connect(host="localhost",username="root",password="Test@123",database="face_recognizer")
                my_cursor =conn.cursor()
                my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Adress=%s,Teacher=%s,PhotoSample=%s where Student_id=%s", (

                        var_dep.get(),
                        var_course.get(),

                        var_year.get(),
                        var_semester.get(),

                        var_std_name.get(),

                        var_div.get(),

                        var_roll.get(),

                        var_gender.get(),

                        var_dob.get(),

                        var_email.get(),

                        var_phone.get(),

                        var_address.get(),

                        var_teacher.get(),
                        var_radio1.get(),

                        var_std_id.get(),







                ))

            else:
                if not Update:
                    return
            messagebox.showinfo("Success","Student details updated successfully",parent=root)
            conn.commit()
            fetch_data()
            conn.close()
        
        except Exception as es:
            messagebox.showerror("Error",f"Due to:{str(es)}",parent=root)

    
#================== delete funtion 
def delete_data():
    if var_std_id.get()=="":
        messagebox.showerror("Error","Student id must be required",parent=root)
    else:
        try:
            delete = messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=root)
            if delete>0:
                conn = mysql.connector.connect(host="localhost",username="root",password="Test@123",database="face_recognizer")
                my_cursor =conn.cursor()
                sql="delete from student where Student_id= %s"
                val=(var_std_id.get(),)
                my_cursor.execute(sql,val)
            else:
                if not delete:
                    return
            conn.commit()
            fetch_data()
            conn.close()
            messagebox.showinfo("Success","Student details deleted successfully",parent=root)
            
        except Exception as es:
            messagebox.showerror("Error",f"Due to:{str(es)}",parent=root)

#========================= Reset funtion

def reset_data():
    var_dep.set("Select Department")
    var_course.set("Select Course")

    var_year.set("Select Year")

    var_semester.set("Select Semester")

    var_std_id.set("")

    var_std_name.set("")

    var_div.set("Select Division")

    var_roll.set("")

    var_gender.set("Male")

    var_dob.set("")

    var_email.set("")

    var_phone.set("")

    var_address.set("")
    var_teacher.set("")
    var_radio1.set("")


#======= Generate data set or Take photo Samples =========

def generate_dataset():
    if var_dep.get() == "Select department" or var_std_name.get() == "" or var_std_id.get()=="":
        messagebox.showerror("Error","All fields are required",parent=root)
    else:
        try:
            
            conn = mysql.connector.connect(host="localhost",username="root",password="Test@123",database="face_recognizer")
            my_cursor =conn.cursor()
            my_cursor.execute("select * from student")
            myresult=my_cursor.fetchall()
            id=0
            for x in myresult:
                id+=1
            my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Adress=%s,Teacher=%s,PhotoSample=%s where Student_id=%s", (

                                                var_dep.get(),
                                                var_course.get(),

                                                var_year.get(),
                                                var_semester.get(),

                                                var_std_name.get(),

                                                var_div.get(),

                                                var_roll.get(),

                                                var_gender.get(),

                                                var_dob.get(),

                                                var_email.get(),

                                                var_phone.get(),

                                                var_address.get(),

                                                var_teacher.get(),
                                                var_radio1.get(),

                                                var_std_id.get()==id+1



                                                                                        ))
            conn.commit()
            fetch_data()
            reset_data()
            conn.close()


            # ======== load predifiend data on face frontals from opencv =========
            face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
            def face_cropped(img):
                gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                faces = face_classifier.detectMultiScale(gray,1.3,5)
                #scaling factor =1.3
                #minimum neighbour = 5
                for (x, y, w, h) in faces:
                    face_cropped=img[y:y+h,x:x+w]
                    return face_cropped
            cap = cv2.VideoCapture(0)
            img_id=0
            while True:
                ret,my_frame = cap.read()
                if face_cropped(my_frame) is not None:
                    img_id+=1
                    face = cv2.resize(face_cropped(my_frame),(450,450))
                    face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                    file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                    cv2.imwrite(file_name_path,face)
                    cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                    cv2.imshow("Cropped Face",face)
                

                if cv2.waitKey(1)==13 or int(img_id)==100:
                    break
            cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo("Result","Generating data sets compled!!!!")

        except Exception as es:
            messagebox.showerror("Error",f"Due to:{str(es)}",parent=root)



def student_page():
    home_page()
    main_student_frame = tk.Frame(main_frame,bg="#243641",highlightbackground='red',highlightthickness=0)
    main_student_frame.pack(side=tk.TOP,anchor=E,pady=0)
    main_student_frame.grid_propagate(False)
    main_student_frame.configure(width=screenwidth-screenwidth/10,height=screenheight-screenheight/25)

#============================ Variables ================
    global var_dep , var_std_id , var_course , var_year , var_semester , var_std_name , var_div , var_roll , var_gender , var_dob , var_email, var_phone , var_phone , var_teacher , var_address
    var_dep = StringVar()
    var_std_id = StringVar()

    var_course = StringVar()
    var_year = StringVar()
    var_semester = StringVar()
    var_std_name = StringVar()
    var_div = StringVar()
    var_roll = StringVar()
    var_gender = StringVar()
    var_dob = StringVar()
    var_email = StringVar()
    var_address = StringVar()
    var_phone = StringVar()
    var_teacher = StringVar()


    right_frame=LabelFrame(main_student_frame, bd=4,font=("times new roman",14,"bold"),text="Student Details",bg='white',pady=10 ,padx=10, relief=RIDGE,fg="#00008B")
    right_frame.grid(row=1,column=0,sticky='WENS',padx=5,pady=5)

    right_frame.grid_propagate(False)
    right_frame.configure(width=(screenwidth-screenwidth/10)/2.1,height=screenheight-screenheight/25)
    
    # right_frame.rowconfigure(0,weight=1)
    # right_frame.rowconfigure(1,weight=3)
    # right_frame.rowconfigure(2,weight=3)


    right_frame.columnconfigure(0,weight=1)
    right_frame.columnconfigure(1,weight=1)

    img_left=Image.open(r"C:\Users\Alahram\Desktop\Face-Recognition-Attendance-System (Graduation)\images\2.png")
    global photoimg_left
    photoimg_left=ImageTk.PhotoImage(img_left)

    f_lb1=Label(right_frame,image=photoimg_left,bg="#DDFFFD")
    f_lb1.grid(row=0,column=0,columnspan=2,sticky="WNE")

    current_course_frame=LabelFrame(right_frame, bd=4,font=("times new roman",14,"bold"),text="Current course information",bg='white',padx=10, relief=RIDGE,fg="#00008B")
    current_course_frame.grid(row=1,column=0,columnspan=2,sticky='WENS',padx=5,pady=5)


    # Department
    dep_label=Label(current_course_frame,text="Department:",font=("times new roman",14,"bold"),bg="white")
    dep_label.grid(row=0,column=0,padx=10,sticky="W")
    dep_combo=ttk.Combobox(current_course_frame,textvariable=var_dep,font=("times new roman",14,"bold"),width=17,state="readonly")
    dep_combo["values"]=("Select department","Computer","IT","Civil","Medical")
    dep_combo.current(0)
    dep_combo.grid(row=0,column=1,padx=4,pady=10,sticky="W")


# Course
    dep_label=Label(current_course_frame,text="Course:",font=("times new roman",14,"bold"),bg="white")
    dep_label.grid(row=1,column=0,padx=10,sticky="W")
    dep_combo=ttk.Combobox(current_course_frame,textvariable=var_course,font=("times new roman",14,"bold"),width=17,state="readonly")
    dep_combo["values"]=("Select course","Data structure","Computer networks","Embedded system","Computer vision")
    dep_combo.current(0)
    dep_combo.grid(row=1,column=1,padx=4,pady=10,sticky="W")

    # Year
    dep_label=Label(current_course_frame,text="Year:",font=("times new roman",14,"bold"),bg="white")
    dep_label.grid(row=0,column=2,padx=10,sticky="W")
    dep_combo=ttk.Combobox(current_course_frame,textvariable=var_year,font=("times new roman",14,"bold"),width=17,state="readonly")
    dep_combo["values"]=("Select Year","2022-2023","2023-2024","2024-2025","2025-2026")
    dep_combo.current(0)
    dep_combo.grid(row=0,column=3,padx=4,pady=10)

    # Semester
    dep_label=Label(current_course_frame,text="Semester:",font=("times new roman",14,"bold"),bg="white")
    dep_label.grid(row=1,column=2,padx=10,sticky="W")
    dep_combo=ttk.Combobox(current_course_frame,textvariable=var_semester,font=("times new roman",14,"bold"),width=17,state="readonly")
    dep_combo["values"]=("Select Semester","2022-2023","2023-2024","2024-2025","2025-2026")
    dep_combo.current(0)
    dep_combo.grid(row=1,column=3,padx=4,pady=10,sticky="W")


 #=========================== Class Student information=============================

    class_student_frame=LabelFrame(right_frame, bd=4,font=("times new roman",14,"bold"),text="Class Student Information",bg='white',padx=10, relief=RIDGE,fg="#00008B")
    class_student_frame.grid(row=2,column=0,columnspan=2,sticky='WENS',padx=5,pady=5)



    #student ID
    student_frame=Label(class_student_frame,text="StudentID:",font=("times new roman",14,"bold"),bg="white")
    student_frame.grid(row=0,column=0,padx=10,sticky="W")

    student_entry=ttk.Entry(class_student_frame,textvariable=var_std_id,width=20,font=("times new roman",14,"bold"))
    student_entry.grid(row=0,column=1,padx=10,pady=5,sticky="W")

    #student name
    student_frame=Label(class_student_frame,text="Student name:",font=("times new roman",14,"bold"),bg="white")
    student_frame.grid(row=0,column=2,padx=10,sticky="W")

    student_entry=ttk.Entry(class_student_frame,textvariable=var_std_name,width=20,font=("times new roman",14,"bold"))
    student_entry.grid(row=0,column=3,padx=10,pady=5,sticky="W")


    #Roll number
    student_frame=Label(class_student_frame,text="Roll number:-",font=("times new roman",14,"bold"),bg="white")
    student_frame.grid(row=1,column=0,padx=10,sticky="W")

    student_entry=ttk.Entry(class_student_frame,textvariable=var_roll,width=20,font=("times new roman",14,"bold"))
    student_entry.grid(row=1,column=1,padx=10,pady=5,sticky="W")


    #Gender
    student_frame=Label(class_student_frame,text="Gender:-",font=("times new roman",14,"bold"),bg="white")
    student_frame.grid(row=1,column=2,padx=10,sticky="W")

    # student_entry=ttk.Entry(class_student_frame,textvariable=var_gender,width=20,font=("times new roman",14,"bold"))
    # student_entry.grid(row=1,column=3,padx=10,pady=5,sticky="W")
    gender_combo=ttk.Combobox(class_student_frame,textvariable=var_gender,font=("times new roman",14,"bold"),width=18,state="readonly")
    gender_combo["values"]=("Select gender","Male","Female")
    gender_combo.current(0)
    gender_combo.grid(row=1,column=3,padx=4,pady=10)


    #Email
    student_frame=Label(class_student_frame,text="Email:-",font=("times new roman",14,"bold"),bg="white")
    student_frame.grid(row=2,column=0,padx=10,sticky="W")

    student_entry=ttk.Entry(class_student_frame,textvariable=var_email,width=20,font=("times new roman",14,"bold"))
    student_entry.grid(row=2,column=1,padx=10,pady=5,sticky="W")

    #Phone number
    student_frame=Label(class_student_frame,text="Phone number:-",font=("times new roman",14,"bold"),bg="white")
    student_frame.grid(row=2,column=2,padx=10,sticky="W")

    student_entry=ttk.Entry(class_student_frame,textvariable=var_phone,width=20,font=("times new roman",14,"bold"))
    student_entry.grid(row=2,column=3,padx=10,pady=5,sticky="W")


    #Adress
    student_frame=Label(class_student_frame,text="Adress:-",font=("times new roman",14,"bold"),bg="white")
    student_frame.grid(row=3,column=0,padx=10,sticky="W")

    student_entry=ttk.Entry(class_student_frame,textvariable=var_address,width=20,font=("times new roman",14,"bold"))
    student_entry.grid(row=3,column=1,padx=10,pady=5,sticky="W")


    #Date of birth
    student_frame=Label(class_student_frame,text="Date of birth:-",font=("times new roman",14,"bold"),bg="white")
    student_frame.grid(row=3,column=2,padx=10,sticky="W")

    student_entry=ttk.Entry(class_student_frame,textvariable=var_dob,width=20,font=("times new roman",14,"bold"))
    student_entry.grid(row=3,column=3,padx=10,pady=5,sticky="W")


    #Class division
    student_frame=Label(class_student_frame,text="Class division:",font=("times new roman",14,"bold"),bg="white")
    student_frame.grid(row=4,column=2,padx=10,sticky="W")

    # student_entry=ttk.Entry(class_student_frame,textvariable=var_div,width=20,font=("times new roman",14,"bold"))
    # student_entry.grid(row=4,column=3,padx=10,pady=5,sticky="W")
    Div_combo=ttk.Combobox(class_student_frame,textvariable=var_div,font=("times new roman",14,"bold"),width=18,state="readonly")
    Div_combo["values"]=("Select div","A","B","C","D")
    Div_combo.current(0)
    Div_combo.grid(row=4,column=3,padx=4,pady=10)


    #Teacher
    student_frame=Label(class_student_frame,text="Teacher:",font=("times new roman",14,"bold"),bg="white")
    student_frame.grid(row=4,column=0,padx=10,sticky="W")

    student_entry=ttk.Entry(class_student_frame,textvariable=var_teacher,width=20,font=("times new roman",14,"bold"))
    student_entry.grid(row=4,column=1,padx=10,pady=5,sticky="W")



#===================================== Radio buttons ======================================
    global var_radio1
    var_radio1 = StringVar()
    Radiobutton1 = ttk.Radiobutton(class_student_frame,variable=var_radio1,text="take photo sample",value="yes")
    Radiobutton1.grid(row=5,column=0)

    # var_radio2 = StringVar()

    Radiobutton2 = ttk.Radiobutton(class_student_frame,variable=var_radio1,text="no photo sample",value="No")
    Radiobutton2.grid(row=5,column=1)

#=====================================  buttons frame ======================================

    # buttons_frame = Frame(class_student_frame,bd=2 , relief= RIDGE)
    # buttons_frame.grid(row=6 , column=0)

    buttons_frame=LabelFrame(right_frame, bd=4,font=("times new roman",14,"bold"),text="Class Student Information",bg='white',padx=10, relief=RIDGE,fg="#00008B" )
    buttons_frame.grid(row=3,column=0,columnspan=2,sticky='WENS',padx=5,pady=5)

    buttons_frame.columnconfigure(0, weight=1)
    buttons_frame.columnconfigure(1, weight=1)
    buttons_frame.columnconfigure(2, weight=1)
    buttons_frame.columnconfigure(3, weight=1)


    save_button = Button(buttons_frame,command =add_data,text="Save",font=("times new roman",14,"bold"),bg="blue",fg="white",padx=1)
    save_button.grid(row=6,column=0,sticky="WENS",pady=2 ,padx=2)

    update_button = Button(buttons_frame,command=update_data,text="Update",font=("times new roman",14,"bold"),bg="blue",fg="white",padx=1)
    update_button.grid(row=6,column=1,sticky="WENS",pady=2,padx=2)

    delete_button = Button(buttons_frame,command=delete_data,text="Delete",font=("times new roman",14,"bold"),bg="blue",fg="white",padx=1)
    delete_button.grid(row=6,column=2,sticky="WENS",pady=2,padx=2)

    Reset_button = Button(buttons_frame,command=reset_data,text="Reset",font=("times new roman",14,"bold"),bg="blue",fg="white",padx=1)
    Reset_button.grid(row=6,column=3,sticky="WENS",pady=2,padx=2)

    take_photo_button = Button(buttons_frame,command=generate_dataset,text="Take photo sample",font=("times new roman",14,"bold"),bg="blue",fg="white",padx=1)
    take_photo_button.grid(row=7,column=0, columnspan=2,sticky="WENS",pady=2,padx=2)

    update_photo_button = Button(buttons_frame,text="Update photo sample",font=("times new roman",14,"bold"),bg="blue",fg="white",padx=1)
    update_photo_button.grid(row=7,column=2 ,columnspan=2,sticky="WENS",pady=2,padx=2)


#================= RIGHT FRAME =====================

    right_frame=LabelFrame(main_student_frame, bd=4,font=("times new roman",14,"bold"),text="Student Details",bg='white',pady=10 ,padx=10, relief=RIDGE,fg="#00008B")
    right_frame.grid(row=1,column=1,sticky='E',padx=5,pady=5)

    right_frame.grid_propagate(False)
    right_frame.configure(width=screenwidth-((screenwidth-screenwidth/10)/2.1),height=screenheight-screenheight/25)
    
    
    # right_frame.rowconfigure(0,weight=1)
    # right_frame.rowconfigure(1,weight=3)
    # right_frame.rowconfigure(2,weight=3)


    right_frame.columnconfigure(0,weight=1)
    right_frame.columnconfigure(1,weight=1)

    img_right=Image.open(r"C:\Users\Alahram\Desktop\Face-Recognition-Attendance-System (Graduation)\images\2.png")
    global photoimg_right
    photoimg_right=ImageTk.PhotoImage(img_right)

    f_lb1=Label(right_frame,image=photoimg_right,bg="#DDFFFD")
    f_lb1.grid(row=0,column=0,columnspan=2,sticky="WNE")

    current_course_frame=LabelFrame(right_frame, bd=4,font=("times new roman",14,"bold"),text="Current course information",bg='white',padx=10, relief=RIDGE,fg="#00008B")
    current_course_frame.grid(row=1,column=0,columnspan=2,sticky='WENS',padx=5,pady=5)


    # Department
    dep_label=Label(current_course_frame,text="Search by:",font=("times new roman",14,"bold"),bg="red")
    dep_label.grid(row=0,column=0,padx=10,sticky="W")
    dep_combo=ttk.Combobox(current_course_frame,font=("times new roman",14,"bold"),width=17,state="readonly")
    dep_combo["values"]=("Select","Roll number","Phone number")
    dep_combo.current(0)
    dep_combo.grid(row=0,column=1,padx=4,pady=10,sticky="W")

    search_entnry = ttk.Entry(current_course_frame,width=30,font=("times new roman",14,"bold"))
    search_entnry.grid(row=0,column=2,padx=10)

    save_button = Button(current_course_frame,text="Search",font=("times new roman",14,"bold"),bg="blue",fg="white",padx=1)
    save_button.grid(row=0,column=3,sticky="WENS",pady=0 ,padx=2 ,ipady=0 , ipadx=10)

    showall_button = Button(current_course_frame,text="Show all",font=("times new roman",14,"bold"),bg="blue",fg="white",padx=1)
    showall_button.grid(row=0,column=4,sticky="WENS",pady=0,padx=2 ,ipady=0 ,ipadx=10)






#=================================== TABLE FRAME ==============================



    



    table_frame = Frame(right_frame,bd=2,bg="white",relief=RIDGE)
    table_frame.place(x=5,y=300,width=(screenwidth-screenwidth/10)/2,height=350)

    scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
    scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
    global student_table
    student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","adress","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=student_table.xview)
    scroll_y.config(command=student_table.yview)


    student_table.heading("dep",text="Department")
    student_table.heading("course",text="course")
    student_table.heading("year",text="Year")
    student_table.heading("sem",text="Semester")
    student_table.heading("id",text="Student ID")
    student_table.heading("name",text="Name")
    student_table.heading("div",text="Division")
    student_table.heading("roll",text="Roll")
    student_table.heading("gender",text="Gender")
    student_table.heading("dob",text="DOB")
    student_table.heading("email",text="Email")
    student_table.heading("phone",text="Phone")
    student_table.heading("adress",text="Adress")
    student_table.heading("teacher",text="Teacher")
    student_table.heading("photo",text="Photo")


    student_table.column("dep",width=100)
    student_table.column("course",width=100)
    student_table.column("year",width=100)
    student_table.column("sem",width=100)
    student_table.column("id",width=100)
    student_table.column("name",width=100)
    student_table.column("div",width=100)
    student_table.column("roll",width=100)
    student_table.column("gender",width=100)
    student_table.column("dob",width=100)
    student_table.column("email",width=100)
    student_table.column("phone",width=100)
    student_table.column("adress",width=100)
    student_table.column("teacher",width=100)
    student_table.column("photo",width=100)
    student_table["show"]="headings"
    student_table.pack(fill=BOTH,expand=1)
    student_table.bind("<ButtonRelease>",get_cursor)
    fetch_data()


def home_page():
    #First image
    global photoimg
    global screenheight
    global screenwidth , bg_img
    photowidth = int(screenwidth-screenwidth/10)
    photoheight = int(screenheight)
    img=Image.open(r"C:\Users\Alahram\Desktop\Face-Recognition-Attendance-System (Graduation)\images\bg.jpg")
    img=img.resize((photowidth,photoheight),Image.Resampling.LANCZOS)
    photoimg=ImageTk.PhotoImage(img)

    bg_img=Label(main_frame,image=photoimg)
    bg_img.place(x=0,y=0,width=screenwidth-screenwidth/10,height=screenheight)
  
    

    buttons_frame = tk.Frame(main_frame,bg="#c3c3c3",highlightbackground='white',highlightthickness=0)
    buttons_frame.pack(side=tk.TOP,anchor=E,pady=(20,0))
    buttons_frame.grid_propagate(False)
    buttons_frame.configure(width=screenwidth-screenwidth/10,height=screenheight/25)

    buttons_frame.columnconfigure(0,weight=99)
    buttons_frame.columnconfigure(1,weight=1)
    buttons_frame.columnconfigure(2,weight=1)
    buttons_frame.columnconfigure(3,weight=1)
    buttons_frame.columnconfigure(4,weight=99)



    student_button = tk.Button (buttons_frame, text="Student Details", font=('Bold ', 18),fg= '#158aff',padx=0, bd=0, bg='#c3c3c3',command=lambda :indicate(home_indicate,student_page))
    student_button.grid(row=0,column=1,padx=0)

    attendance_button = tk.Button (buttons_frame, text="Attendance", font=('Bold ', 18),fg= '#158aff',padx=0, bd=0, bg='#c3c3c3',command=lambda :indicate(home_indicate,student_page))
    attendance_button.grid(row=0,column=2,padx=0)

    test = tk.Button (buttons_frame, text="Soon", font=('Bold ', 18),fg= '#158aff',padx=0, bd=0, bg='#c3c3c3',command=lambda :indicate(home_indicate,home_page))
    test.grid(row=0,column=3,padx=0)



    # student_frame = tk.Frame(main_frame,bg="#243641",highlightbackground='red',highlightthickness=0)
    # student_frame.pack(side=tk.TOP,anchor=E,pady=0)
    # student_frame.grid_propagate(False)
    # student_frame.configure(width=screenwidth-screenwidth/10,height=screenheight-screenheight/25)


    




    
def menu_page():
    home_frame = tk.Frame(main_frame)
    lb= tk.Label(home_frame,text='ffffffffffffffff Frame\n\nPage: 1',font=('bold',50))
    lb.pack()
    home_frame.pack()
def contact_page():
    home_frame = tk.Frame(main_frame)
    lb= tk.Label(home_frame,text='bbbbbbbbbb Frame\n\nPage: 1',font=('bold',50))
    lb.pack()
    home_frame.pack()
def about_page():
    home_frame = tk.Frame(main_frame)
    lb= tk.Label(home_frame,text='aaaaaaaaaa Frame\n\nPage: 1',font=('bold',50))
    lb.pack()
    home_frame.pack()
def delete_page():
    for frame in main_frame.winfo_children():
        frame.destroy()
def indicate(lb,page):
    home_indicate.config(bg="#c3c3c3")
    menu_indicate.config(bg="#c3c3c3")
    contact_indicate.config(bg="#c3c3c3")
    about_indicate.config(bg="#c3c3c3")
    delete_page()
    page()

    lb.config(bg='#158aff')








#======================================== Start =================================

screenwidth = int(root.winfo_screenwidth())
screenheight = int(root.winfo_screenheight())
# print(screenheight)
# print(screenwidth)


options_frame = tk.Frame(root,bg='#c3c3c3')
w = root.winfo_screenheight()/18
# print(w)
global college_img
img=Image.open(r"C:\Users\Alahram\Desktop\Face-Recognition-Attendance-System (Graduation)\images\2.png")
img=img.resize((int(screenwidth/10),int(screenheight/8)),Image.Resampling.LANCZOS)
college_img=ImageTk.PhotoImage(img)

College_label=Label(options_frame,image=college_img, background = '#c3c3c3')
College_label.place(x=0,y=0,width=screenwidth/10,height=screenheight/8)

home_btn = tk.Button (options_frame, text="Home", font=('Bold ', 18),fg= '#158aff', bd=0, bg='#c3c3c3',command=lambda :indicate(home_indicate,home_page))
home_btn.place(x=10,y=screenheight/3)
home_indicate = tk.Label(options_frame, text='',bg='#c3c3c3')
home_indicate.place(x=4,y=screenheight/3,width=5,height=43)

menu_btn = tk.Button (options_frame, text="Menu", font=('Bold ', 18),fg= '#158aff', bd=0, bg='#c3c3c3',command=lambda :indicate(menu_indicate,menu_page))
menu_btn.place(x=10,y=screenheight/3+w)
menu_indicate = tk.Label(options_frame, text='',bg='#c3c3c3')
menu_indicate.place(x=4,y=screenheight/3+w,width=5,height=43)

contact_btn = tk.Button (options_frame, text="Contact", font=('Bold ', 18),fg= '#158aff', bd=0, bg='#c3c3c3',command=lambda :indicate(contact_indicate,contact_page))
contact_btn.place(x=10,y=screenheight/3+2*w)
contact_indicate = tk.Label(options_frame, text='',bg='#c3c3c3')
contact_indicate.place(x=4,y=screenheight/3+2*w,width=5,height=43)

about = tk.Button (options_frame, text="Help", font=('Bold ', 18),fg= '#158aff', bd=0, bg='#c3c3c3',command=lambda :indicate(about_indicate,about_page))
about.place(x=10,y=screenheight/3+3*w)
about_indicate = tk.Label(options_frame, text='',bg='#c3c3c3')
about_indicate.place(x=4,y=screenheight/3+3*w,width=5,height=43)




options_frame.pack(side=tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width=screenwidth/10,height=screenheight)


main_frame = tk.Frame(root,highlightbackground='#c3c3c3',highlightthickness=0)
main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(width=screenwidth-screenwidth/10,height=screenheight)


home_page()
home_indicate.config(bg="#158aff")
def time():
                string = strftime('%H:%M:%S %p')
                Ibl.config(text=string)
                Ibl.after(1000, time)

Ibl = Label(options_frame, font =('Bold',16),background='#c3c3c3',foreground='#158aff',padx=0)
Ibl.place(x=0,y=screenheight-screenheight/10,width=160,height=50)
time()        



root.mainloop()