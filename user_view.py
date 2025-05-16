import tkinter as tk
from tkinter import ttk, messagebox
import cx_Oracle

def view_users():
    win = tk.Toplevel()
    win.title("All Users")
    win.configure(bg="#1e1e1e")
    win.geometry("600x400")

    style = ttk.Style(win)
    style.theme_use("clam")
    style.configure("Treeview",
                    background="#2e2e2e",
                    fieldbackground="#2e2e2e",
                    foreground="white",
                    rowheight=25)
    style.map('Treeview', background=[('selected', '#4a6984')])

    tree = ttk.Treeview(win, columns=("ID", "Name", "Age", "Gender", "Weight", "Height"), show="headings")
    for col in ("ID", "Name", "Age", "Gender", "Weight", "Height"):
        tree.heading(col, text=col)
        tree.column(col, width=100, anchor=tk.CENTER)
    tree.pack(fill="both", expand=True, padx=10, pady=10)

    try:
        dsn_tns = cx_Oracle.makedsn("LAPTOP-A5H0NVJM", 1521, service_name="XE")
        conn = cx_Oracle.connect(user="system", password="admin123", dsn=dsn_tns)
        cursor = conn.cursor()

        cursor.execute("SELECT user_id, name, age, gender, weight, height FROM users")
        for row in cursor.fetchall():
            tree.insert("", "end", values=row)

    except Exception as e:
        messagebox.showerror("Database Error", str(e))

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

# Optional test run
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    view_users()
    root.mainloop()

