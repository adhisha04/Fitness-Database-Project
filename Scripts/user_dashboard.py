import tkinter as tk
from tkinter import ttk
import cx_Oracle

def show_user_dashboard(conn,cursor):
    win = tk.Toplevel()
    win.title("User Dashboard")
    win.geometry("600x400")
    win.configure(bg="#1e1e1e")

    style = ttk.Style(win)
    style.theme_use("clam")
    style.configure("Treeview", background="#2e2e2e", fieldbackground="#2e2e2e", foreground="white", rowheight=25)
    style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"), background="#444")
    style.map("Treeview", background=[('selected', '#4a6984')])

    tree_frame = tk.Frame(win, bg="#1e1e1e")
    tree_frame.pack(padx=10, pady=10, fill="both", expand=True)

    tree = ttk.Treeview(tree_frame, columns=("ID", "Name", "Age", "Gender", "Weight", "Height"), show="headings")
    for col in ("ID", "Name", "Age", "Gender", "Weight", "Height"):
        tree.heading(col, text=col)
        tree.column(col, width=100, anchor=tk.CENTER)
    tree.pack(expand=True, fill="both")

    try:
        dsn_tns = cx_Oracle.makedsn("LAPTOP-A5H0NVJM", 1521, service_name="XE")
        conn = cx_Oracle.connect(user="system", password="admin123", dsn=dsn_tns)
        cursor = conn.cursor()
        cursor.execute("SELECT user_id, name, age, gender, weight, height FROM users")
        for row in cursor.fetchall():
            tree.insert("", "end", values=row)
        cursor.close()
        conn.close()
    except Exception as e:
        tk.messagebox.showerror("Database Error", str(e))


