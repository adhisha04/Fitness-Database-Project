# gui_user_entry.py
import cx_Oracle
import tkinter as tk
from tkinter import ttk, messagebox

# DB Connection
def launch_window(conn, cursor):
    win = tk.Toplevel()
    win.title("Add User")
    win.configure(bg="#1e1e1e")
    win.geometry("600x400")
    win.resizable(False, False)

    # Fonts and Colors
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TLabel", background="#1e1e1e", foreground="#ffffff", font=('Segoe UI', 10))
    style.configure("TButton", background="#2d2d30", foreground="#ffffff", font=('Segoe UI', 10))
    style.configure("TEntry", fieldbackground="#2d2d30", foreground="#ffffff")
    style.configure("TCombobox", fieldbackground="#2d2d30", foreground="#ffffff")
    style.configure("Treeview", background="#2d2d30", fieldbackground="#2d2d30", foreground="white")

    # Entry Fields
    tk.Label(win, text="Name:", bg="#1e1e1e", fg="white").grid(row=0, column=0, padx=10, pady=5, sticky="e")
    tk.Label(win, text="Age:", bg="#1e1e1e", fg="white").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    tk.Label(win, text="Gender:", bg="#1e1e1e", fg="white").grid(row=2, column=0, padx=10, pady=5, sticky="e")
    tk.Label(win, text="Weight (kg):", bg="#1e1e1e", fg="white").grid(row=3, column=0, padx=10, pady=5, sticky="e")
    tk.Label(win, text="Height (cm):", bg="#1e1e1e", fg="white").grid(row=4, column=0, padx=10, pady=5, sticky="e")

    name_entry = ttk.Entry(win)
    age_entry = ttk.Entry(win)
    gender_entry = ttk.Combobox(win, values=["Male", "Female", "Other"], state="readonly")
    gender_entry.set("Select")
    weight_entry = ttk.Entry(win)
    height_entry = ttk.Entry(win)

    name_entry.grid(row=0, column=1, padx=10, pady=5)
    age_entry.grid(row=1, column=1, padx=10, pady=5)
    gender_entry.grid(row=2, column=1, padx=10, pady=5)
    weight_entry.grid(row=3, column=1, padx=10, pady=5)
    height_entry.grid(row=4, column=1, padx=10, pady=5)

    def submit():
        name = name_entry.get().strip()
        age = age_entry.get().strip()
        gender = gender_entry.get()
        weight = weight_entry.get().strip()
        height = height_entry.get().strip()

        # Validation
        if not name or not age or not gender or gender == "Select" or not weight or not height:
            messagebox.showwarning("Input Error", "Please fill in all fields correctly.")
            return

        if not age.isdigit() or not is_float(weight) or not is_float(height):
            messagebox.showwarning("Input Error", "Age must be an integer. Weight and Height must be numbers.")
            return

        try:
            cursor.execute("""
                INSERT INTO Users (user_id, name, age, gender, weight, height)
                VALUES (Users_seq.nextval, :1, :2, :3, :4, :5)
            """, (name, int(age), gender, float(weight), float(height)))
            conn.commit()
            messagebox.showinfo("Success", "Data submitted successfully!")
            clear_fields()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to insert data:\n{e}")

    def is_float(value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def view_data():
        try:
            cursor.execute("SELECT name, age, gender, weight, height FROM Users")
            records = cursor.fetchall()
            for row in tree.get_children():
                tree.delete(row)
            for row in records:
                tree.insert("", tk.END, values=row)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to retrieve data:\n{e}")

    def clear_fields():
        name_entry.delete(0, tk.END)
        age_entry.delete(0, tk.END)
        gender_entry.set("Select")
        weight_entry.delete(0, tk.END)
        height_entry.delete(0, tk.END)

    ttk.Button(win, text="Submit", command=submit).grid(row=5, column=0, padx=10, pady=10)
    ttk.Button(win, text="View Data", command=view_data).grid(row=5, column=1, padx=10, pady=10)

    # Treeview for displaying data
    tree = ttk.Treeview(win, columns=("Name", "Age", "Gender", "Weight", "Height"), show="headings")
    for col in ("Name", "Age", "Gender", "Weight", "Height"):
        tree.heading(col, text=col)
        tree.column(col, width=100)
    tree.grid(row=6, column=0, columnspan=2, padx=10, pady=20)

    # ✅ Move scrollbar here inside the function
    scrollbar = ttk.Scrollbar(win, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.grid(row=6, column=2, sticky="ns", pady=20)

