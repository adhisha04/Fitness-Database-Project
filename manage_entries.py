import tkinter as tk
from tkinter import ttk, messagebox
import cx_Oracle

def launch_entry_manager(conn, cursor):
    win = tk.Toplevel()
    win.title("Manage Calorie and Workout Entries")
    win.configure(bg="#1e1e1e")
    win.geometry("800x500")

    style = ttk.Style(win)
    style.theme_use("clam")
    style.configure("Treeview", background="#2e2e2e", fieldbackground="#2e2e2e", foreground="white", rowheight=25)
    style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"), background="#444")
    style.map("Treeview", background=[('selected', '#4a6984')])

    tab_control = ttk.Notebook(win)
    calorie_tab = ttk.Frame(tab_control)
    workout_tab = ttk.Frame(tab_control)

    tab_control.add(calorie_tab, text="Calorie Intake")
    tab_control.add(workout_tab, text="Workout Sessions")
    tab_control.pack(expand=1, fill="both")

    # --- Calorie Tab ---
    calorie_frame = tk.Frame(calorie_tab)
    calorie_frame.pack(fill="both", expand=True, padx=10, pady=10)

    calorie_tree = ttk.Treeview(calorie_frame, columns=("ID", "User", "Date", "Calories"), show="headings")
    for col in ("ID", "User", "Date", "Calories"):
        calorie_tree.heading(col, text=col)
        calorie_tree.column(col, width=150, anchor=tk.CENTER)
    calorie_tree.pack(side="left", fill="both", expand=True)

    cal_scrollbar = ttk.Scrollbar(calorie_frame, orient="vertical", command=calorie_tree.yview)
    calorie_tree.configure(yscrollcommand=cal_scrollbar.set)
    cal_scrollbar.pack(side="right", fill="y")

    def refresh_calories():
        calorie_tree.delete(*calorie_tree.get_children())
        cursor.execute("SELECT nutrition_id, user_id, TO_CHAR(entry_date, 'DD-MON-YYYY'), calories FROM nutrition")
        for row in cursor.fetchall():
            calorie_tree.insert("", "end", values=row)

    def delete_selected_calorie():
        selected = calorie_tree.selection()
        if not selected:
            messagebox.showwarning("Select Entry", "Please select a calorie entry to delete.")
            return
        nutrition_id = calorie_tree.item(selected[0])['values'][0]
        try:
            cursor.execute("DELETE FROM Nutrition WHERE nutrition_id = :1", (nutrition_id,))
            conn.commit()
            refresh_calories()
            messagebox.showinfo("Deleted", "✅ Calorie entry deleted.")
        except Exception as e:
            messagebox.showerror("Error", f"❌ Failed to delete calorie entry:\n{e}")

    ttk.Button(calorie_tab, text="Delete Selected", command=delete_selected_calorie).pack(pady=5)

    # --- Workout Tab ---
    workout_frame = tk.Frame(workout_tab)
    workout_frame.pack(fill="both", expand=True, padx=10, pady=10)

    workout_tree = ttk.Treeview(workout_frame, columns=("ID", "User", "Date", "Calories Burned"), show="headings")
    for col in ("ID", "User", "Date", "Calories Burned"):
        workout_tree.heading(col, text=col)
        workout_tree.column(col, width=150, anchor=tk.CENTER)
    workout_tree.pack(side="left", fill="both", expand=True)

    workout_scrollbar = ttk.Scrollbar(workout_frame, orient="vertical", command=workout_tree.yview)
    workout_tree.configure(yscrollcommand=workout_scrollbar.set)
    workout_scrollbar.pack(side="right", fill="y")

    def refresh_workouts():
        workout_tree.delete(*workout_tree.get_children())
        cursor.execute("SELECT workout_id, user_id, TO_CHAR(workout_date, 'DD-MON-YYYY'), calories_burned FROM Workouts")
        for row in cursor.fetchall():
            workout_tree.insert("", "end", values=row)

    def delete_selected_workout():
        selected = workout_tree.selection()
        if not selected:
            messagebox.showwarning("Select Entry", "Please select a workout entry to delete.")
            return
        workout_id = workout_tree.item(selected[0])['values'][0]
        try:
            cursor.execute("DELETE FROM Workouts WHERE workout_id = :1", (workout_id,))
            conn.commit()
            refresh_workouts()
            messagebox.showinfo("Deleted", "✅ Workout entry deleted.")
        except Exception as e:
            messagebox.showerror("Error", f"❌ Failed to delete workout entry:\n{e}")

    ttk.Button(workout_tab, text="Delete Selected", command=delete_selected_workout).pack(pady=5)

    refresh_calories()
    refresh_workouts()

