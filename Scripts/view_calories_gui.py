import tkinter as tk
from tkinter import ttk, messagebox
import cx_Oracle

def view_calories_gui():
    win = tk.Toplevel()
    win.title("View Calorie Intake")
    win.configure(bg="#1e1e1e")
    win.geometry("750x400")

    style = ttk.Style(win)
    style.theme_use("clam")
    style.configure("Treeview", background="#2e2e2e", foreground="white", fieldbackground="#2e2e2e", rowheight=25)
    style.configure("Treeview.Heading", background="#3a3a3a", foreground="white", font=('Segoe UI', 10, 'bold'))

    columns = ("ID", "User ID", "Date", "Meal", "Food Item", "Calories")
    tree = ttk.Treeview(win, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor=tk.CENTER, width=110)

    tree.pack(side="left", fill="both", expand=True)

    scrollbar = ttk.Scrollbar(win, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    try:
        conn = cx_Oracle.connect("system/admin123@localhost/XE")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Nutrition")
        for row in cursor.fetchall():
            tree.insert("", tk.END, values=row)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch data:\n{e}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

