import tkinter as tk
from tkinter import messagebox

def launch_summary_view(conn, cursor):
    window = tk.Toplevel()
    window.title("Summary View")
    window.configure(bg="#1e1e1e")
    window.geometry("500x400")

    # --- Input field for User ID ---
    tk.Label(window, text="Enter User ID:", bg="#1e1e1e", fg="white").pack(pady=5)
    user_id_entry = tk.Entry(window)
    user_id_entry.pack(pady=5)

    result_text = tk.Text(window, height=15, width=60, bg="#2e2e2e", fg="white")
    result_text.pack(pady=10)

    def show_summary():
        user_id = user_id_entry.get()
        if not user_id.isdigit():
            messagebox.showerror("Input Error", "User ID must be a number.")
            return
        
        result_text.delete("1.0", tk.END)
        try:
            # Calorie Summary
            cursor.execute("SELECT SUM(calories) FROM Nutrition WHERE user_id = :1", (user_id,))
            total_cal = cursor.fetchone()[0] or 0

            # Workout Summary
            cursor.execute("SELECT SUM(calories_burned) FROM Workouts WHERE user_id = :1", (user_id,))
            total_burn = cursor.fetchone()[0] or 0

            result = f"Summary for User ID {user_id}:\n\n"
            result += f"Total Calories Consumed: {total_cal}\n"
            result += f"Total Calories Burned: {total_burn}\n"
            result += f"Net Calories: {total_cal - total_burn}\n"

            result_text.insert(tk.END, result)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(window, text="Show Summary", command=show_summary, bg="blue", fg="white").pack(pady=10)

