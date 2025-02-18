from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector



class studentclass:
    def __init__(self, root):
        self.root = root
        self.root.title("Students Results Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()
        
        # Title label with image
        title = Label(self.root, text="Manage Student Details",
                      font=("goudy old style", 20, "bold"), bg="#033054", fg="white")
        title.place(x=10, y=15, width=1180, height=35)
        
        # Variables
        self.var_student_id = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_contact = StringVar()
        self.var_course_id = StringVar()
        self.var_search = StringVar()
        
        # Widgets
        lbl_student_id = Label(self.root, text="Student ID", font=("Times new roman", 15, "bold"), bg="white")
        lbl_student_id.place(x=10, y=60)

        lbl_name = Label(self.root, text="Name", font=("Times new roman", 15, "bold"), bg="white")
        lbl_name.place(x=10, y=100)
        
        lbl_email = Label(self.root, text="Email", font=("Times new roman", 15, "bold"), bg="white")
        lbl_email.place(x=10, y=140)
        
        lbl_gender = Label(self.root, text="Gender", font=("Times new roman", 15, "bold"), bg="white")
        lbl_gender.place(x=10, y=180)
        
        lbl_dob = Label(self.root, text="D.O.B", font=("Times new roman", 15, "bold"), bg="white")
        lbl_dob.place(x=10, y=220)
        
        lbl_contact = Label(self.root, text="Contact", font=("Times new roman", 15, "bold"), bg="white")
        lbl_contact.place(x=10, y=260)

        lbl_course_id = Label(self.root, text="Course ID", font=("Times new roman", 15, "bold"), bg="white")
        lbl_course_id.place(x=10, y=300)

        lbl_address = Label(self.root, text="Address", font=("Times new roman", 15, "bold"), bg="white")
        lbl_address.place(x=10, y=340)
        
        # Entry fields
        self.txt_student_id = Entry(self.root, textvariable=self.var_student_id, font=("Times new roman", 12, "italic"), bg="lightyellow")
        self.txt_student_id.place(x=150, y=60, width=200)

        self.txt_name = Entry(self.root, textvariable=self.var_name, font=("Times new roman", 12, "italic"), bg="lightyellow")
        self.txt_name.place(x=150, y=100, width=200)
        
        self.txt_email = Entry(self.root, textvariable=self.var_email, font=("Times new roman", 12, "italic"), bg="lightyellow")
        self.txt_email.place(x=150, y=140, width=200)
        
        # Gender radio buttons
        self.gender_frame = Frame(self.root, bg="white")
        self.gender_frame.place(x=150, y=180, width=200, height=30)
        
        self.rbtn_male = Radiobutton(self.gender_frame, text="Male", variable=self.var_gender, value="Male", font=("Times new roman", 12, "italic"), bg="white")
        self.rbtn_male.place(x=0, y=0)
        
        self.rbtn_female = Radiobutton(self.gender_frame, text="Female", variable=self.var_gender, value="Female", font=("Times new roman", 12, "italic"), bg="white")
        self.rbtn_female.place(x=80, y=0)

        self.txt_dob = Entry(self.root, textvariable=self.var_dob, font=("Times new roman", 12, "italic"), bg="lightyellow")
        self.txt_dob.place(x=150, y=220, width=200)

        self.txt_contact = Entry(self.root, textvariable=self.var_contact, font=("Times new roman", 12, "italic"), bg="lightyellow")
        self.txt_contact.place(x=150, y=260, width=200)

        self.txt_course_id = Entry(self.root, textvariable=self.var_course_id, font=("Times new roman", 12, "italic"), bg="lightyellow")
        self.txt_course_id.place(x=150, y=300, width=200)

        self.txt_address = Text(self.root, font=("Times new roman", 12, "italic"), bg="lightyellow")
        self.txt_address.place(x=150, y=340, width=500, height=100)
        
        # Buttons
        self.btn_add = Button(self.root, text='Save', font=("Cambria", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2", command=self.add)
        self.btn_add.place(x=150, y=450, width=110, height=40)
        
        self.btn_update = Button(self.root, text='Update', font=("Cambria", 15, "bold"), bg="#4caf50", fg="white", cursor="hand2", command=self.update)
        self.btn_update.place(x=270, y=450, width=110, height=40)
        
        self.btn_delete = Button(self.root, text='Delete', font=("Cambria", 15, "bold"), bg="#f44336", fg="white", cursor="hand2", command=self.delete)
        self.btn_delete.place(x=390, y=450, width=110, height=40)
        
        self.btn_clear = Button(self.root, text="Clear", font=("Cambria", 15, "bold"), bg="#607d8b", fg="white", cursor="hand2", command=self.clear)
        self.btn_clear.place(x=510, y=450, width=110, height=40)
        
        # Search panel
        lbl_search_name = Label(self.root, text="Name/ID", font=("Times new roman", 15, "bold"), bg="white")
        lbl_search_name.place(x=720, y=60)        
        
        self.txt_search_name = Entry(self.root, textvariable=self.var_search, font=("Times new roman", 15, "bold"), bg="lightyellow")
        self.txt_search_name.place(x=870, y=60, width=180)

        self.btn_search = Button(self.root, text='Search', font=("Cambria", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2", command=self.search)
        self.btn_search.place(x=1070, y=60, width=120, height=28)
        
        # Content frame for Treeview
        self.c_frame = Frame(self.root, bd=2, relief=RIDGE)
        self.c_frame.place(x=720, y=100, width=470, height=340)
        
        # Treeview widget
        self.StudentTable = ttk.Treeview(self.c_frame, columns=("student_id", "name", "email", "gender", "dob", "contact", "course_id", "address"))
        self.StudentTable.pack(fill=BOTH, expand=1)

        # Treeview headings
        self.StudentTable.heading("student_id", text="Student ID")
        self.StudentTable.heading("name", text="Name")
        self.StudentTable.heading("email", text="Email")
        self.StudentTable.heading("gender", text="Gender")
        self.StudentTable.heading("dob", text="D.O.B")
        self.StudentTable.heading("contact", text="Contact")
        self.StudentTable.heading("course_id", text="Course ID")
        self.StudentTable.heading("address", text="Address")
        
        # Configure columns
        self.StudentTable["show"] = "headings"
        self.StudentTable.column("student_id", width=100)
        self.StudentTable.column("name", width=150)
        self.StudentTable.column("email", width=150)
        self.StudentTable.column("gender", width=100)
        self.StudentTable.column("dob", width=100)
        self.StudentTable.column("contact", width=100)
        self.StudentTable.column("course_id", width=100)
        self.StudentTable.column("address", width=250)
        
        # Scrollbars
        scroll_x = Scrollbar(self.c_frame, orient=HORIZONTAL, command=self.StudentTable.xview)
        scroll_y = Scrollbar(self.c_frame, orient=VERTICAL, command=self.StudentTable.yview)
        self.StudentTable.configure(xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.StudentTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()

    def connect_db(self):
        self.conn = mysql.connector.connect(host="localhost", user="root", password="123456", database="course_db")
        self.cursor = self.conn.cursor()

    def add(self):
        self.connect_db()
        if self.var_student_id.get() == "" or self.var_name.get() == "":
            messagebox.showerror("Error", "All fields should be required", parent=self.root)
        else:
            try:
                self.cursor.execute("SELECT * FROM student WHERE student_id=%s", (self.var_student_id.get(),))
                row = self.cursor.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "This Student ID already exists", parent=self.root)
                else:
                    self.cursor.execute("INSERT INTO student (student_id, name, email, gender, dob, contact, course_id, address) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (
                        self.var_student_id.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_course_id.get(),
                        self.txt_address.get("1.0", END)
                    ))
                    self.conn.commit()
                    messagebox.showinfo("Success", "Student added successfully", parent=self.root)
                    self.show()
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
            self.conn.close()

    def show(self):
        self.connect_db()
        try:
            self.cursor.execute("SELECT * FROM student")
            rows = self.cursor.fetchall()
            self.StudentTable.delete(*self.StudentTable.get_children())
            for row in rows:
                self.StudentTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        self.conn.close()

    def get_data(self, ev):
        f = self.StudentTable.focus()
        content = (self.StudentTable.item(f))
        row = content['values']
        self.var_student_id.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_dob.set(row[4])
        self.var_contact.set(row[5])
        self.var_course_id.set(row[6])
        self.txt_address.delete("1.0", END)
        self.txt_address.insert(END, row[7])

    def update(self):
        self.connect_db()
        try:
            if self.var_student_id.get() == "" or self.var_name.get() == "":
                messagebox.showerror("Error", "All fields should be required", parent=self.root)
            else:
                self.cursor.execute("UPDATE student SET name=%s, email=%s, gender=%s, dob=%s, contact=%s, course_id=%s, address=%s WHERE student_id=%s", (
                    self.var_name.get(),
                    self.var_email.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_contact.get(),
                    self.var_course_id.get(),
                    self.txt_address.get("1.0", END),
                    self.var_student_id.get()
                ))
                self.conn.commit()
                messagebox.showinfo("Success", "Student updated successfully", parent=self.root)
                self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        self.conn.close()

    def delete(self):
        self.connect_db()
        try:
            if self.var_student_id.get() == "" or self.var_name.get() == "":
                messagebox.showerror("Error", "All fields should be required", parent=self.root)
            else:
                self.cursor.execute("DELETE FROM student WHERE student_id=%s", (self.var_student_id.get(),))
                self.conn.commit()
                messagebox.showinfo("Success", "Student deleted successfully", parent=self.root)
                self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        self.conn.close()

    def clear(self):
        self.var_student_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_contact.set("")
        self.var_course_id.set("")
        self.txt_address.delete("1.0", END)
        self.var_search.set("")

    def search(self):
        self.connect_db()
        try:
            query = "SELECT * FROM student WHERE student_id LIKE %s OR name LIKE %s"
            search_id = f"%{self.var_search.get()}%"
            search_name = f"%{self.var_search.get()}%"
            self.cursor.execute(query, (search_id, search_name))
            rows = self.cursor.fetchall()
            self.StudentTable.delete(*self.StudentTable.get_children())
            for row in rows:
                self.StudentTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        self.conn.close()
        
if __name__ == "__main__":
    root = Tk()
    obj = studentclass(root)
    root.mainloop()
