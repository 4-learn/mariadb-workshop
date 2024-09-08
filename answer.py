import mariadb
cursor = None
conn = None

try:
    # 建立連接
    conn = mariadb.connect(
        user="root",
        password="password123",
        host="localhost",
        database="school"
    )
    cursor = conn.cursor()
    print("Connected to MariaDB!")

    # 創建資料表
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INT PRIMARY KEY,
            name VARCHAR(50),
            grade INT
        )
    """)
    print("Table created successfully")

    # 插入三筆資料
    cursor.execute("INSERT INTO students (id, name, grade) VALUES (1, 'John Doe', 85)")
    cursor.execute("INSERT INTO students (id, name, grade) VALUES (2, 'Jane Smith', 92)")
    cursor.execute("INSERT INTO students (id, name, grade) VALUES (3, 'Emily Johnson', 78)")
    conn.commit()
    print("Data inserted successfully")

    # 查詢資料
    cursor.execute("SELECT * FROM students")
    for row in cursor:
        print(f"ID: {row[0]}, Name: {row[1]}, Grade: {row[2]}")

    # 更新某位學生的成績
    cursor.execute("UPDATE students SET grade = 95 WHERE name = 'Emily Johnson'")
    conn.commit()
    print("Data updated successfully")

except mariadb.Error as e:
    print(f"Error: {e}")

finally:
    # 關閉連接
    if cursor:
        cursor.close()
    if conn:
        conn.close()
    print("Connection closed.")

