import tkinter as tk
from tkinter import ttk, messagebox
import cx_Oracle
from datetime import datetime

def launch_insert_workouts(conn, cursor):
    win = tk.Toplevel()
    win.title("Add Workout Record")
    win.configure(bg="#1e1e1e")
    win.geometry("400x350")
    win.resizable(False, False)

    style = ttk.Style(win)
    style.theme_use("clam")
    style.configure("TLabel", background="#1e1e1e", foreground="#ffffff", font=('Segoe UI', 10))
    style.configure("TButton", background="#2d2d30", foreground="#ffffff", font=('Segoe UI', 10))
    style.configure("TEntry", fieldbackground="#2d2d30", foreground="#ffffff")

    labels = ["User ID:", "Workout Type:", "Duration (mins):", "Calories Burned:", "Date (DD-MM-YYYY):"]
    entries = []

    for i, label in enumerate(labels):
        ttk.Label(win, text=label).grid(row=i, column=0, padx=10, pady=5, sticky="e")
        entry = ttk.Entry(win)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries.append(entry)

    def insert_workout():
        try:
            if not all([entries[0].get().strip(), entries[1].get().strip(), entries[2].get().strip(), entries[3].get().strip()]):
                messagebox.showwarning("Missing Data", "Please fill in all fields except date.")
                return

            user_id = int(entries[0].get())
            workout_type = entries[1].get()
            duration = int(entries[2].get())
            calories_burned = float(entries[3].get())
            date_input = entries[4].get().strip()

            if not date_input:
                cursor.execute("""
                    INSERT INTO Workouts (user_id, workout_type, duration, calories_burned)
                    VALUES (:1, :2, :3, :4)
                """, (user_id, workout_type, duration, calories_burned))
            else:
                workout_date = datetime.strptime(date_input, "%d-%m-%Y")
                cursor.execute("""
                    INSERT INTO Workouts (user_id, workout_type, duration, calories_burned, workout_date)
                    VALUES (:1, :2, :3, :4, :5)
                """, (user_id, workout_type, duration, calories_burned, workout_date))

            conn.commit()
            messagebox.showinfo("Success", f"🏋️ {workout_type} for {duration} mins ({calories_burned} kcal) added.")
            for entry in entries:
                entry.delete(0, tk.END)

        except Exception as e:
            conn.rollback()
            messagebox.showerror("Error", f"⚠️ Failed to insert workout:\n{e}")

    ttk.Button(win, text="Add Entry", command=insert_workout).grid(row=6, column=0, columnspan=2, pady=20)
    win.protocol("WM_DELETE_WINDOW", win.destroy)

