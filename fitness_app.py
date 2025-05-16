import os

def display_menu():
    print("\n" + "="*50)
    print("🔷 Personal Fitness Management System 🔷")
    print("="*50)
    print("1. ➕ Add New User")
    print("2. 🍽️  Add Calorie Intake")
    print("3. 🏋️  Add Workout")
    print("4. 👥 View Users")
    print("5. 📊 View Calories")
    print("6. 📈 View Workouts")
    print("7. 🧾 View Summary")
    print("8. 🛠️  Manage Entries (Add/Delete/Update)")
    print("9. ❌ Exit")
    print("="*50)

def run_script(script_name, message):
    print(f"\n--- Running {script_name} ---\n")
    os.system(f"python {script_name}")
    print()

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-9): ").strip()

        if choice == '1':
            run_script("insert_data.py", "Add New User")
        elif choice == '2':
            run_script("insert_calories.py", "Add Calorie Intake")
        elif choice == '3':
            run_script("insert_workouts.py", "Add Workout")
        elif choice == '4':
            run_script("user_dashboard.py", "View Users")
        elif choice == '5':
            run_script("view_calories.py", "View Calories")
        elif choice == '6':
            run_script("view_workouts.py", "View Workouts")
        elif choice == '7':
            run_script("summary_view.py", "View Summary")
        elif choice == '8':
            run_script("manage_entries.py", "Manage Entries")
        elif choice == '9':
            print("\n👋 Exiting the application. Stay fit!")
            break
        else:
            print("❌ Invalid choice! Please enter a number between 1 and 9.")

if __name__ == "__main__":
    main()
