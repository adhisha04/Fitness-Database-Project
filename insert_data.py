import cx_Oracle

# Connect to Oracle Database
dsn_tns = cx_Oracle.makedsn("LAPTOP-A5H0NVJM", 1521, service_name="XE")
conn = cx_Oracle.connect(user="system", password="admin123", dsn=dsn_tns)
cursor = conn.cursor()

# Insert sample user data
cursor.execute("INSERT INTO Users (user_id, name, age, gender, weight, height) VALUES (3, 'Adhisha', 20, 'Female', 55.5, 165.0)")
cursor.execute("INSERT INTO Users (user_id, name, age, gender, weight, height) VALUES (4, 'John Doe', 22, 'Male', 70.2, 175.5)")

# Commit changes
conn.commit()

print("✅ Sample data inserted successfully!")

# Close connection
cursor.close()
conn.close()
