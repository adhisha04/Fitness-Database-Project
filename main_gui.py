import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import cx_Oracle

# Custom modules
import gui_user_entry
import insert_calories
import insert_workouts
import summary_view
import manage_entries
import user_dashboard
import user_view
import view_calories_gui
import view_workouts_gui

# Setup DB connection
dsn = cx_Oracle.makedsn("localhost", 1521, service_name="XE")
conn = cx_Oracle.connect(user="system", password="admin123", dsn=dsn)
cursor = conn.cursor()

# Define launcher functions
def launch_insert_calories():
    insert_calories.launch_insert_calories(conn, cursor)

def launch_insert_workouts():
    insert_workouts.launch_insert_workouts(conn, cursor)

def launch_user_dashboard():
    user_dashboard.show_user_dashboard(conn, cursor)

def launch_summary_view():
    summary_view.launch_summary_view(conn, cursor)

def launch_manage_entries():
    manage_entries.launch_entry_manager(conn, cursor)

def launch_user_view():
    user_view.view_users()

def launch_add_user():
    gui_user_entry.launch_window(conn, cursor)

def launch_view_calories():
    view_calories_gui.view_calories_gui()

def launch_view_workouts():
    view_workouts_gui.view_workouts_gui()

# Main GUI Window
def main():
    root = tk.Tk()
    root.title("Personal Fitness Manager")
    root.geometry("420x600")
    root.configure(bg="#121212")

    tk.Label(root, text="🏋️ Fitness Manager", font=("Arial", 18, "bold"),
             bg="#121212", fg="white").pack(pady=20)

    buttons = [
        ("User Dashboard", launch_user_dashboard),
        ("Add User", launch_add_user),
        ("View Users", launch_user_view),
        ("Add Calorie Entry", launch_insert_calories),
        ("Add Workout Entry", launch_insert_workouts),
        ("View Calorie Records", launch_view_calories),
        ("View Workout Records", launch_view_workouts),
        ("View Summary", launch_summary_view),
        ("Edit / Delete Entries", launch_manage_entries),
        ("Exit", root.quit)
    ]

    for text, cmd in buttons:
        tk.Button(root, text=text, command=cmd, font=("Arial", 12), width=30,
                  bg="#1f1f1f", fg="white", activebackground="#333",
                  activeforeground="white").pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()

