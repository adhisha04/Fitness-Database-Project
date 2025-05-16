# 🏋️ Personal Fitness Management System

A complete **GUI-based fitness tracking application** built using **Python, Tkinter**, and **Oracle Database**. This project allows users to manage their fitness data, including user profiles, calorie intake, workout sessions, and summary views.

---

## 📁 Features

### 👤 User Management
- Add new users (Name, Age, Gender, Weight, Height)
- View all users
- Edit or delete user records
- Track Join Date (auto or manual)

### 🍽️ Calorie Intake Tracking
- Record meals with food item, meal type, calories, and date
- View and delete calorie entries
- Automatically sets the date to today if not entered

### 🏋️ Workout Tracking
- Log workout sessions (type, duration, calories burned, date)
- View and delete workout records

### 📊 Summary View
- See total calories consumed vs. calories burned for each user
- Filter by user ID or view for all users

### ⚙️ Entry Manager
- Manage calorie and workout entries in a tabbed interface
- Delete entries via selection

---

## 🛠️ Technology Stack

- **Frontend**: Python `Tkinter` GUI
- **Database**: Oracle 11g/12c+
- **Driver**: `cx_Oracle`

---

## 🔧 Setup Instructions

 1. 📦 Requirements
- Python 3.10+ (tested on Python 3.13)
- Oracle XE installed and running
- `cx_Oracle` installed
  ```bash
  pip install cx_Oracle

2. 🗄️ Create Tables
Run the script to create the database structure:
python create_tables.py

3. ➕ Insert Sample Users
python insert_data.py

🚀 Launch the Application:

Option 1: GUI Launcher
python main_gui.py

Option 2: Menu-based Console App
python fitness_app.py

📂 Project Structure
File	                  Description
main_gui.py	        Main launcher window
insert_calories.py	GUI to insert nutrition info
insert_workouts.py	GUI to log workouts
user_dashboard.py	Console-based user summary
user_view.py	        GUI to view, update, delete users
manage_entries.py	Tabbed GUI to delete calorie/workout data
summary_view.py	        GUI to view calorie vs workout summaries
gui_user_entry.py	GUI to add users
create_tables.py	Creates the required Oracle DB tables
insert_data.py	        Inserts initial user data
view_calories_gui.py	GUI view of all calorie entries
view_workouts_gui.py	GUI view of all workouts

🙋‍♂️ Authors
Adhisha
