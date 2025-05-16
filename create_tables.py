import cx_Oracle

# Database connection
dsn_tns = cx_Oracle.makedsn("LAPTOP-A5H0NVJM", 1521, service_name="XE")
conn = cx_Oracle.connect(user="system", password="admin123", dsn=dsn_tns)
cursor = conn.cursor()

# Utility function to safely drop tables
def safe_drop_table(table_name):
    try:
        cursor.execute(f"""
        BEGIN
            EXECUTE IMMEDIATE 'DROP TABLE {table_name} CASCADE CONSTRAINTS';
        EXCEPTION
            WHEN OTHERS THEN
                IF SQLCODE != -942 THEN
                    RAISE;
                END IF;
        END;
        """)
    except Exception as e:
        print(f"⚠️ Error dropping {table_name}: {e}")

# Drop existing tables if they exist
safe_drop_table("Nutrition")
safe_drop_table("Workouts")
safe_drop_table("Users")

# Drop existing sequence and trigger if they exist
for obj in ["user_seq", "workout_seq", "workout_id_trigger"]:
    try:
        cursor.execute(f"DROP {'SEQUENCE' if 'seq' in obj else 'TRIGGER'} {obj}")
    except:
        pass

# Create Users table
cursor.execute("""
    CREATE TABLE Users (
        user_id NUMBER PRIMARY KEY,
        name VARCHAR2(100) NOT NULL,
        age NUMBER(3) CHECK (age > 0),
        gender VARCHAR2(10),
        weight NUMBER(5,2),
        height NUMBER(5,2),
        join_date DATE DEFAULT SYSDATE
    )
""")

# Create Workouts table
cursor.execute("""
    CREATE TABLE Workouts (
        workout_id NUMBER PRIMARY KEY,
        user_id NUMBER,
        workout_type VARCHAR2(100),
        duration NUMBER,
        calories_burned NUMBER(5,2),
        workout_date DATE DEFAULT SYSDATE,
        FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE
    )
""")

# Create Nutrition table
cursor.execute("""
    CREATE TABLE Nutrition (
        nutrition_id NUMBER PRIMARY KEY,
        user_id NUMBER,
        meal_type VARCHAR2(50),
        food_item VARCHAR2(100),
        calories NUMBER(5,2),
        entry_date DATE DEFAULT SYSDATE,
        FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE
    )
""")

# Create sequences
cursor.execute("CREATE SEQUENCE user_seq START WITH 1 INCREMENT BY 1")
cursor.execute("CREATE SEQUENCE workout_seq START WITH 1 INCREMENT BY 1")

# Create trigger for auto-incrementing workout_id
cursor.execute("""
    CREATE OR REPLACE TRIGGER workout_id_trigger
    BEFORE INSERT ON Workouts
    FOR EACH ROW
    BEGIN
        SELECT workout_seq.NEXTVAL INTO :new.workout_id FROM dual;
    END;
""")

print("✅ Tables, sequences, and triggers created successfully.")

# Commit changes and close resources
conn.commit()
cursor.close()
conn.close()

