import cx_Oracle

def fetch_all_workouts():
    conn = cx_Oracle.connect("system/admin123@localhost/XE")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Workouts")
    rows = cursor.fetchall()

    print("💪 Workout Tracking Data:")
    for row in rows:
        print(f"Workout ID: {row[0]}, User ID: {row[1]}, Type: {row[2]}, Duration: {row[3]} mins, "
              f"Calories Burned: {row[4]}, Date: {row[5]}")

    cursor.close()
    conn.close()

# Optional test run
if __name__ == "__main__":
    fetch_all_workouts()
