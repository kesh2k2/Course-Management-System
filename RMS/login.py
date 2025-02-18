from tkinter import *
from tkinter import messagebox
import mysql.connector


class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("400x400+450+150")
        self.root.config(bg="lightblue")

        # Variables for username and password
        self.var_username = StringVar()
        self.var_password = StringVar()

        # Title
        title = Label(self.root, text="Login", font=("Goudy Old Style", 30, "bold"), bg="lightblue", fg="#033054")
        title.place(x=0, y=30, relwidth=1)

        # Username Label and Entry
        lbl_user = Label(self.root, text="Username", font=("Goudy Old Style", 15, "bold"), bg="lightblue", fg="black")
        lbl_user.place(x=50, y=100)
        self.txt_user = Entry(self.root, textvariable=self.var_username, font=("Goudy Old Style", 15), bg="white")
        self.txt_user.place(x=150, y=100, width=200)

        # Password Label and Entry
        lbl_pass = Label(self.root, text="Password", font=("Goudy Old Style", 15, "bold"), bg="lightblue", fg="black")
        lbl_pass.place(x=50, y=160)
        self.txt_pass = Entry(self.root, textvariable=self.var_password, font=("Goudy Old Style", 15), bg="white", show="*")
        self.txt_pass.place(x=150, y=160, width=200)

        # Login Button
        btn_login = Button(self.root, text="Login", font=("Goudy Old Style", 15, "bold"), bg="#033054", fg="white", command=self.login)
        btn_login.place(x=150, y=220, width=200, height=40)

    def login(self):
        if self.var_username.get() == "" or self.var_password.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="123456", database="course_db")
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (self.var_username.get(), self.var_password.get()))
                row = cursor.fetchone()

                if row is None:
                    messagebox.showerror("Error", "Invalid Username or Password", parent=self.root)
                else:
                    messagebox.showinfo("Success", "Login Successful!", parent=self.root)
                    self.root.destroy()  # Close login window
                    self.open_dashboard()  # Open the dashboard after successful login

                conn.close()
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def open_dashboard(self):
        from dashboard import RMS  # Import the dashboard class
        root = Tk()
        obj = RMS(root)  # Open the dashboard after login
        root.mainloop()

# Starting the application
if __name__ == "__main__":
    root = Tk()
    app = LoginWindow(root)
    root.mainloop()
