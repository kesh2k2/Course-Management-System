from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import mysql.connector

class courseclass:
    def __init__(self, root):
        self.root = root
        self.root.title("Students Results Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()
        
        # Title label with image
        title = Label(self.root, text="Manage Course Details",
                      font=("goudy old style", 20, "bold"), bg="#033054", fg="white")
        title.place(x=10, y=15, width=1180, height=35)
        
        # Variables
        self.var_course = StringVar()
        self.var_duration = StringVar()
        self.var_charges = StringVar()
        self.var_search = StringVar()
        
        # Widgets
        lbl_courseName = Label(self.root, text="Course Name", font=("Times new roman", 15, "bold"), bg="white")
        lbl_courseName.place(x=10, y=60)

        lbl_duration = Label(self.root, text="Duration", font=("Times new roman", 15, "bold"), bg="white")
        lbl_duration.place(x=10, y=100)
        
        lbl_charges = Label(self.root, text="Charges", font=("Times new roman", 15, "bold"), bg="white")
        lbl_charges.place(x=10, y=140)
        
        lbl_description = Label(self.root, text="Description", font=("Times new roman", 15, "bold"), bg="white")
        lbl_description.place(x=10, y=180)
        
        # Entry fields
        self.txt_courseName = Entry(self.root, textvariable=self.var_course, font=("Times new roman", 12, "italic"), bg="lightyellow")
        self.txt_courseName.place(x=150, y=60, width=200)

        self.txt_duration = Entry(self.root, textvariable=self.var_duration, font=("Times new roman", 12, "italic"), bg="lightyellow")
        self.txt_duration.place(x=150, y=100, width=200)
        
        self.txt_charges = Entry(self.root, textvariable=self.var_charges, font=("Times new roman", 12, "italic"), bg="lightyellow")
        self.txt_charges.place(x=150, y=140, width=200)
        
        self.txt_description = Text(self.root, font=("Times new roman", 12, "italic"), bg="lightyellow")
        self.txt_description.place(x=150, y=180, width=500, height=100)
        
        # Buttons
        self.btn_add = Button(self.root, text='Save', font=("Cambria", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2", command=self.add)
        self.btn_add.place(x=150, y=400, width=110, height=40)
        
        self.btn_update = Button(self.root, text='Update', font=("Cambria", 15, "bold"), bg="#4caf50", fg="white", cursor="hand2", command=self.update)
        self.btn_update.place(x=270, y=400, width=110, height=40)
        
        self.btn_delete = Button(self.root, text='Delete', font=("Cambria", 15, "bold"), bg="#f44336", fg="white", cursor="hand2", command=self.delete)
        self.btn_delete.place(x=390, y=400, width=110, height=40)
        
        self.btn_clear = Button(self.root, text="Clear", font=("Cambria", 15, "bold"), bg="#607d8b", fg="white", cursor="hand2", command=self.clear)
        self.btn_clear.place(x=510, y=400, width=110, height=40)
        
        # Search panel
        lbl_search_courseName = Label(self.root, text="Course Name", font=("Times new roman", 15, "bold"), bg="white")
        lbl_search_courseName.place(x=720, y=60)        
        
        self.txt_search_courseName = Entry(self.root, textvariable=self.var_search, font=("Times new roman", 15, "bold"), bg="lightyellow")
        self.txt_search_courseName.place(x=870, y=60, width=180)

        self.btn_search = Button(self.root, text='Search', font=("Cambria", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2", command=self.search)
        self.btn_search.place(x=1070, y=60, width=120, height=28)
        
        # Content frame for Treeview
        self.c_frame = Frame(self.root, bd=2, relief=RIDGE)
        self.c_frame.place(x=720, y=100, width=470, height=340)
        
        # Treeview widget
        self.CourseTable = ttk.Treeview(self.c_frame, columns=("cid", "name", "duration", "charges", "description"))
        self.CourseTable.pack(fill=BOTH, expand=1)

        # Treeview headings
        self.CourseTable.heading("cid", text="Course ID")
        self.CourseTable.heading("name", text="Course Name")
        self.CourseTable.heading("duration", text="Duration")
        self.CourseTable.heading("charges", text="Charges")
        self.CourseTable.heading("description", text="Description")
        
        # Configure columns
        self.CourseTable["show"] = "headings"
        self.CourseTable.column("cid", width=100)
        self.CourseTable.column("name", width=150)
        self.CourseTable.column("duration", width=100)
        self.CourseTable.column("charges", width=100)
        self.CourseTable.column("description", width=250)
        
        # Scrollbars
        scroll_x = Scrollbar(self.c_frame, orient=HORIZONTAL, command=self.CourseTable.xview)
        scroll_y = Scrollbar(self.c_frame, orient=VERTICAL, command=self.CourseTable.yview)
        self.CourseTable.configure(xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.CourseTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()

    def connect_db(self):
        self.conn = mysql.connector.connect(host="localhost", user="root", password="123456", database="course_db")
        self.cursor = self.conn.cursor()

    def add(self):
        self.connect_db()
        if self.var_course.get() == "":
            messagebox.showerror("Error", "Course Name should be required", parent=self.root)
        else:
            try:
                self.cursor.execute("SELECT * FROM course WHERE name=%s", (self.var_course.get(),))
                row = self.cursor.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "This course title already available", parent=self.root)
                else:
                    self.cursor.execute("INSERT INTO course (name, duration, charges, description) VALUES (%s, %s, %s, %s)", (
                        self.var_course.get(),
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_description.get("1.0", END)
                    ))
                    self.conn.commit()
                    messagebox.showinfo("Success", "Course added successfully", parent=self.root)
                    self.show()
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
            self.conn.close()

    def show(self):
        self.connect_db()
        try:
            self.cursor.execute("SELECT * FROM course")
            rows = self.cursor.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        self.conn.close()

    def get_data(self, ev):
        f = self.CourseTable.focus()
        content = (self.CourseTable.item(f))
        row = content['values']
        self.var_course.set(row[1])
        self.var_duration.set(row[2])
        self.var_charges.set(row[3])
        self.txt_description.delete("1.0", END)
        self.txt_description.insert(END, row[4])

    def update(self):
        self.connect_db()
        try:
            if self.var_course.get() == "":
                messagebox.showerror("Error", "Course Name should be required", parent=self.root)
            else:
                self.cursor.execute("UPDATE course SET name=%s, duration=%s, charges=%s, description=%s WHERE id=%s", (
                    self.var_course.get(),
                    self.var_duration.get(),
                    self.var_charges.get(),
                    self.txt_description.get("1.0", END),
                    self.CourseTable.item(self.CourseTable.focus())["values"][0]
                ))
                self.conn.commit()
                messagebox.showinfo("Success", "Course updated successfully", parent=self.root)
                self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        self.conn.close()

    def delete(self):
        self.connect_db()
        try:
            if self.var_course.get() == "":
                messagebox.showerror("Error", "Course Name should be required", parent=self.root)
            else:
                self.cursor.execute("DELETE FROM course WHERE name=%s", (self.var_course.get(),))
                self.conn.commit()
                messagebox.showinfo("Success", "Course deleted successfully", parent=self.root)
                self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        self.conn.close()

    def clear(self):
        self.var_course.set("")
        self.var_duration.set("")
        self.var_charges.set("")
        self.txt_description.delete("1.0", END)
        self.var_search.set("")

    def search(self):
        self.connect_db()
        try:
            self.cursor.execute(f"SELECT * FROM course WHERE name LIKE '%{self.var_search.get()}%'")
            rows = self.cursor.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        self.conn.close()

if __name__ == "__main__":
    root = Tk()
    obj = courseclass(root)
    root.mainloop()
