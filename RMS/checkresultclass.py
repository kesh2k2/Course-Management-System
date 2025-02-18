from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector

class checkresultclass:
    def __init__(self, root):
        self.root = root
        self.root.title("Check Student Result")
        self.root.geometry("600x400+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        # Title label
        title = Label(self.root, text="Check Student Result", font=("goudy old style", 20, "bold"), bg="#033054", fg="white")
        title.place(x=10, y=15, width=580, height=35)

        # Variables
        self.var_student_id = StringVar()
        self.var_name = StringVar()
        self.var_result = StringVar()

        # Widgets
        lbl_student_id = Label(self.root, text="Student ID", font=("Times new roman", 15, "bold"), bg="white")
        lbl_student_id.place(x=10, y=60)

        self.txt_student_id = Entry(self.root, textvariable=self.var_student_id, font=("Times new roman", 12, "italic"), bg="lightyellow")
        self.txt_student_id.place(x=150, y=60, width=200)

        lbl_name = Label(self.root, text="Name", font=("Times new roman", 15, "bold"), bg="white")
        lbl_name.place(x=10, y=100)

        self.txt_name = Entry(self.root, textvariable=self.var_name, font=("Times new roman", 12, "italic"), bg="lightyellow", state='readonly')
        self.txt_name.place(x=150, y=100, width=200)

        lbl_result = Label(self.root, text="Result", font=("Times new roman", 15, "bold"), bg="white")
        lbl_result.place(x=10, y=140)

        self.txt_result = Entry(self.root, textvariable=self.var_result, font=("Times new roman", 12, "italic"), bg="lightyellow", state='readonly')
        self.txt_result.place(x=150, y=140, width=200)

        # Buttons
        self.btn_fetch = Button(self.root, text='Fetch Details', font=("Cambria", 15, "bold"), bg="#4caf50", fg="white", cursor="hand2", command=self.fetch_details)
        self.btn_fetch.place(x=360, y=60, width=120, height=28)

        self.btn_clear = Button(self.root, text="Clear", font=("Cambria", 15, "bold"), bg="#607d8b", fg="white", cursor="hand2", command=self.clear)
        self.btn_clear.place(x=150, y=200, width=110, height=40)

    def connect_db(self):
        self.conn = mysql.connector.connect(host="localhost", user="root", password="123456", database="course_db")
        self.cursor = self.conn.cursor()

    def fetch_details(self):
        self.connect_db()
        try:
            self.cursor.execute("SELECT name FROM student WHERE student_id=%s", (self.var_student_id.get(),))
            row = self.cursor.fetchone()
            if row is None:
                messagebox.showerror("Error", "Invalid Student ID", parent=self.root)
                self.clear()
            else:
                self.var_name.set(row[0])
                self.cursor.execute("SELECT result FROM results WHERE student_id=%s", (self.var_student_id.get(),))
                result_row = self.cursor.fetchone()
                if result_row is None:
                    messagebox.showerror("Error", "No results found for this student", parent=self.root)
                    self.clear()
                else:
                    self.var_result.set(result_row[0])
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        self.conn.close()

    def clear(self):
        self.var_student_id.set("")
        self.var_name.set("")
        self.var_result.set("")

if __name__ == "__main__":
    root = Tk()
    obj = checkresultclass(root)
    root.mainloop()
