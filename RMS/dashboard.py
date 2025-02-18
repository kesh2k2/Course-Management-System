from tkinter import *
from PIL import Image, ImageTk
from course import courseclass
from studentclass import studentclass
from addresultclass import addresultclass
from checkresultclass import checkresultclass
from tkcalendar import Calendar
from tkinter import messagebox

class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Course Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#7D94B5")

        # Load and process the logo image
        self.logo_image = Image.open("D:/RMS/images/logo_pp.png")
        self.logo_image = self.logo_image.resize((50, 50), Image.LANCZOS)
        self.logo_dash = ImageTk.PhotoImage(self.logo_image)

        # Title label with image
        title = Label(self.root, text="Course Management System", image=self.logo_dash, compound=LEFT,
                      font=("goudy old style", 20, "bold"), bg="#033054", fg="white")
        title.place(x=0, y=0, relwidth=1, height=50)

        # Menus Frame
        M_Frame = LabelFrame(self.root, text="MENUS", font=("times new roman", 15, "bold"), bg="#E4F6F8", fg="black")
        M_Frame.place(x=0, y=70, width=1360, height=60)

        btn_course = Button(M_Frame, text="Course", font=("cambria", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.add_course)
        btn_course.place(x=20, y=5, width=200, height=40)
        btn_student = Button(M_Frame, text="Student", font=("cambria", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.add_student)
        btn_student.place(x=240, y=5, width=200, height=40)
        btn_result = Button(M_Frame, text="Result", font=("cambria", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.add_result)
        btn_result.place(x=460, y=5, width=200, height=40)
        btn_view = Button(M_Frame, text="View Student Results", font=("cambria", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.view_result)
        btn_view.place(x=680, y=5, width=200, height=40)
        btn_logout = Button(M_Frame, text="Logout", font=("cambria", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.logout)
        btn_logout.place(x=900, y=5, width=200, height=40)
        btn_exit = Button(M_Frame, text="Exit", font=("cambria", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.exit_app)
        btn_exit.place(x=1120, y=5, width=200, height=40)

        # Load and process the background image
        self.bg_image = Image.open("D:/Result Management System/images/bg.jpg")
        self.bg_img = ImageTk.PhotoImage(self.bg_image)

        # Background image label
        self.lbl_bg = Label(self.root, image=self.bg_img)
        self.lbl_bg.place(x=0, y=175, width=1350, height=350)

        # Update details
        self.lbl_course = Label(self.root, text="Total Courses\n[ 0 ]", font=("cambria", 16), bd=10, relief=RIDGE, bg="#e43b06", fg="White")
        self.lbl_course.place(x=50, y=560, width=200, height=80)

        self.lbl_student = Label(self.root, text="Total Students\n[ 0 ]", font=("cambria", 16), bd=10, relief=RIDGE, bg="#0676ad", fg="White")
        self.lbl_student.place(x=350, y=560, width=200, height=80)

        self.lbl_result = Label(self.root, text="Total Results\n[ 0 ]", font=("cambria", 16), bd=10, relief=RIDGE, bg="#038074", fg="White")
        self.lbl_result.place(x=650, y=560, width=200, height=80)

        # Left Frame for Calendar and Reminder
        left_frame = Frame(self.root, bd=6, relief=RIDGE, bg="#939185")
        left_frame.place(x=938, y=526, width=380, height=115)

        # Reminder
        remind_label = Label(left_frame, text="Reminder", font=("goudy old style", 15, "bold"), bg="#FBE9D0", fg="#0b5377")
        remind_label.pack(pady=10)

        self.reminder_entry = Entry(left_frame, font=("Arial", 12), bd=2, relief=RIDGE)
        self.reminder_entry.pack(pady=2)

        btn_add_reminder = Button(left_frame, text="Add Reminder", font=("cambria", 12, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.add_reminder)
        btn_add_reminder.pack(pady=2)

        # Footer label with image
        footer = Label(self.root, text="SRMS - Students Result Management System\nContact Us for any Technical Issue: 075 3546554",
                       font=("goudy old style", 12, "bold"), bg="#262626", fg="white")
        footer.pack(side=BOTTOM, fill=X)

    def add_course(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = courseclass(self.new_win)
        
    def add_student(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = studentclass(self.new_win)
        
    def add_result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = addresultclass(self.new_win) 
        
    def view_result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = checkresultclass(self.new_win) 
        
    def add_reminder(self):
        reminder_text = self.reminder_entry.get()
        if reminder_text:
            messagebox.showinfo("Reminder Added", f"Reminder '{reminder_text}' added successfully!")
            self.reminder_entry.delete(0, END)
        else:
            messagebox.showwarning("Empty Reminder", "Please enter a reminder text.")
    
    def logout(self):
        if messagebox.askokcancel("Logout", "Are you sure you want to log out?"):
            self.root.destroy()  # Close the current application window
            # You may want to add code here to redirect to a login window or another main entry point of your application.

    def exit_app(self):
        if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
            self.root.destroy()  # Close the application

    def update_counts(self, courses, students, results):
        # Update the labels with the given counts
        self.lbl_course.config(text=f"Total Courses\n[ {courses} ]")
        self.lbl_student.config(text=f"Total Students\n[ {students} ]")
        self.lbl_result.config(text=f"Total Results\n[ {results} ]")

if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()
