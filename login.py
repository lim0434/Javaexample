import sqlite3
from tkinter import Tk, Canvas, Entry, Button, messagebox

# Function to login a user
def login_user():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    username = login_entry_1.get().strip()
    password = login_entry_2.get().strip()

    # Validate input
    if not username or not password:
        messagebox.showerror("Error", "Username and password are required!")
        conn.close()
        return

    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    result = c.fetchone()

    if result:
        messagebox.showinfo("Success", "Login successful!")
        login_window.destroy()
        show_dashboard()
    else:
        messagebox.showerror("Error", "Invalid username or password!")

    conn.close()

# Function to show the dashboard
def show_dashboard():
    dashboard = Tk()
    dashboard.geometry("800x500")
    dashboard.configure(bg="#81BEEB")
    dashboard.title("User Dashboard")

    dashboard_label = Canvas(dashboard, bg="#81BEEB", height=300, width=400, bd=0, highlightthickness=0, relief="ridge")
    dashboard_label.create_text(200, 100, text="Welcome to the Dashboard!", font=("Arial", 20), fill="#000000")
    dashboard_label.pack()

    # Logout button
    logout_button = Button(dashboard, text="Logout", bg="#FF0000", fg="#FFFFFF", font=("Arial", 14),
                           command=lambda: logout(dashboard))
    logout_button.pack(pady=20)

    dashboard.mainloop()

# Function to logout
def logout(dashboard):
    dashboard.destroy()
    show_login_page()

# Login Page
def show_login_page():
    global login_entry_1, login_entry_2, login_window

    login_window = Tk()
    login_window.geometry("613x388")
    login_window.title("Login Form")
    login_window.configure(bg="#81BEEB")

    canvas = Canvas(login_window, bg="#81BEEB", height=388, width=613, bd=0, highlightthickness=0, relief="ridge")
    canvas.place(x=0, y=0)

    canvas.create_text(133, 35, anchor="nw", text="LOGIN FORM", font=("Inter Medium", 24 * -1), fill="#000000")

    canvas.create_text(81, 114, anchor="nw", text="Username:", font=("Inter Bold", 18 * -1), fill="#000000")
    login_entry_1 = Entry(login_window, bd=0, bg="#D9D9D9", fg="#000716", font=("Inter", 14))
    login_entry_1.place(x=270, y=114, width=249, height=29)

    canvas.create_text(81, 176, anchor="nw", text="Password:", font=("Inter Bold", 18 * -1), fill="#000000")
    login_entry_2 = Entry(login_window, bd=0, bg="#D9D9D9", fg="#000716", show="*", font=("Inter", 14))
    login_entry_2.place(x=270, y=176, width=249, height=29)

    login_button = Button(login_window, text="Login", bg="#4CAF50", fg="#FFFFFF", font=("Inter Bold", 14),
                          command=login_user)
    login_button.place(x=325, y=238, width=139, height=40)

    login_window.mainloop()

# Main section for login
if __name__ == "__main__":
    show_login_page()
