import sqlite3

conn = sqlite3.connect('Student.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM DB_student")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()