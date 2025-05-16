import tkinter as tk
from tkinter import ttk, messagebox
import cx_Oracle
from datetime import datetime

def launch_insert_calories(conn, cursor):
    win = tk.Toplevel()
    win.title("Add Calorie Intake")
    win.configure(bg="#1e1e1e")
    win.geometry("400x350")
    win.resizable(False, False)

    style = ttk.Style(win)
    style.theme_use("clam")
    style.configure("TLabel", background="#1e1e1e", foreground="white", font=('Segoe UI', 10))
    style.configure("TEntry", fieldbackground="#2d2d30", foreground="white")
    style.configure("TButton", background="#2d2d30", foreground="white", font=('Segoe UI', 10))

    labels = ["User ID:", "Meal Type:", "Food Item:", "Calories:", "Date (DD-MM-YYYY):"]
    entries = []

    for i, label in enumerate(labels):
        ttk.Label(win, text=label).grid(row=i, column=0, padx=10, pady=5, sticky="e")
        entry = ttk.Entry(win)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries.append(entry)

    def insert_calorie_data():
        try:
            user_id = entries[0].get().strip()
            meal_type = entries[1].get().strip()
            food_item = entries[2].get().strip()
            calories = entries[3].get().strip()
            date_input = entries[4].get().strip()

            if not all([user_id, meal_type, food_item, calories]):
                messagebox.showwarning("Missing Data", "Please fill in all fields except date.")
                return

            user_id = int(user_id)
            calories = float(calories)

            if not date_input:
                cursor.execute("""
                    INSERT INTO Nutrition (user_id, meal_type, food_item, calories)
                    VALUES (:1, :2, :3, :4)
                """, (user_id, meal_type, food_item, calories))
            else:
                date = datetime.strptime(date_input, "%d-%m-%Y")
                cursor.execute("""
                    INSERT INTO Nutrition (user_id, meal_type, food_item, calories, entry_date)
                    VALUES (:1, :2, :3, :4, :5)
                """, (user_id, meal_type, food_item, calories, date))

            conn.commit()
            messagebox.showinfo("Success", f"✅ Added {meal_type} - {food_item} ({calories} kcal)")
            for entry in entries:
                entry.delete(0, tk.END)

        except Exception as e:
            conn.rollback()
            messagebox.showerror("Error", f"⚠️ Failed to insert calorie data:\n{e}")

    ttk.Button(win, text="Add Entry", command=insert_calorie_data).grid(row=6, column=0, columnspan=2, pady=20)
    win.protocol("WM_DELETE_WINDOW", win.destroy)


