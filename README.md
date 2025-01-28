# Attendance-management-system-using-face-recognition
This Python project is an Attendance Management System using Face Recognition. It is built using the Tkinter library for the graphical user interface (GUI) and OpenCV for face detection and recognition. The system also integrates with a MySQL database to store student details and attendance records. Below are the key features, details, and information about the project:

Key Features
Face Recognition-Based Attendance:

The system uses face recognition to mark attendance automatically.

It captures live video from the webcam, detects faces, and matches them with the pre-trained dataset to identify students.

Attendance is marked in real-time and stored in a CSV file.

Student Management:

Add, update, delete, and reset student details.

Store student information such as name, ID, roll number, department, course, year, semester, gender, date of birth, email, phone number, address, and teacher name.

Training the Face Recognition Model:

The system allows you to train the face recognition model using student images.

It uses the LBPH (Local Binary Patterns Histograms) algorithm for face recognition.

Attendance Management:

View and manage attendance records.

Import and export attendance data in CSV format.

User-Friendly GUI:

The GUI is designed using Tkinter, making it easy to navigate.

It includes buttons for different functionalities like student details, attendance, face recognition, and training the model.

Database Integration:

The system connects to a MySQL database to store and retrieve student information.

The database schema includes tables for student details and attendance records.

Real-Time Clock:

A real-time clock is displayed on the GUI to keep track of the current time.

Exit Functionality:

The system provides an option to exit the application gracefully.

Technical Details
Libraries and Tools Used:

Tkinter: For creating the GUI.

OpenCV: For face detection and recognition.

PIL (Pillow): For image processing and displaying images in the GUI.

MySQL Connector: For database connectivity.

CSV Module: For handling attendance records in CSV format.

NumPy: For numerical operations during face recognition.

Face Recognition Workflow:

The system uses the Haar Cascade classifier for face detection.

It trains the face recognition model using the LBPH algorithm.

The trained model is saved in an XML file (classifier.xml).

Database Schema:

The MySQL database has a table named student to store student details.

The table includes fields such as Student_id, Name, Roll, Dep, Course, Year, Semester, Division, Gender, Dob, Email, Phone, Adress, Teacher, and PhotoSample.

File Structure:

Images: Contains background images and icons used in the GUI.

Data: Stores the dataset of student images used for training the face recognition model.

CSV Files: Attendance records are stored in CSV files (e.g., omar.csv).

Code Structure:

The code is organized into a class Face_Recognition_System, which handles all functionalities.

Methods are defined for each feature, such as add_data(), update_data(), delete_data(), reset_data(), generate_dataset(), train_classifier(), and face_recognition().

Functionalities
Home Page:

Displays a background image and provides navigation buttons for different features.

Student Details:

Allows the user to add, update, delete, and reset student information.

Includes fields for entering student details and radio buttons for taking photo samples.

Attendance Page:

Displays attendance records in a table.

Allows the user to import and export attendance data in CSV format.

Face Recognition:

Captures live video from the webcam and detects faces.

Matches detected faces with the trained dataset and marks attendance.

Train Data:

Trains the face recognition model using the student images stored in the data folder.

Help and Exit:

Provides a help section (currently placeholder text) and an exit button to close the application.

How It Works
Student Registration:

The user adds student details through the GUI.

The system captures photo samples of the student using the webcam and stores them in the data folder.

Training the Model:

The system trains the face recognition model using the captured images.

The trained model is saved in classifier.xml.

Attendance Marking:

The system captures live video from the webcam.

It detects faces, matches them with the trained dataset, and marks attendance in real-time.

Attendance records are stored in a CSV file.

Attendance Management:

The user can view, import, and export attendance records.

Advantages
Automated Attendance: Reduces manual effort in marking attendance.

User-Friendly Interface: Easy to use with a clean and intuitive GUI.

Scalable: Can be extended to handle more students and additional features.

Database Integration: Ensures data persistence and easy retrieval.

Limitations
Dependence on Lighting and Pose: Face recognition accuracy may vary depending on lighting conditions and the student's pose.

Training Time: Training the model with a large dataset can be time-consuming.

Hardware Dependency: Requires a webcam for face detection and recognition.

Future Enhancements
Multi-Face Detection: Improve the system to detect and recognize multiple faces simultaneously.

Cloud Integration: Store attendance records and student details in the cloud for remote access.

Mobile App: Develop a mobile app for easier access and attendance marking.

Advanced Algorithms: Implement more advanced face recognition algorithms like Deep Learning-based models for better accuracy.

Real-Time Notifications: Send real-time notifications to students and teachers about attendance status.

Conclusion
This project is a robust Attendance Management System that leverages face recognition technology to automate the attendance process. It is suitable for educational institutions, offices, or any organization that requires an efficient and accurate attendance tracking system. The integration of a GUI, database, and face recognition makes it a comprehensive solution for managing attendance.
