# Integration.py
# --------------------------
# initial environment
# import modules
import tkinter as tk
import sqlite3

# basic GUI 
root = tk.Tk()
root.title('INTEGRATION')
root.geometry('300x400')  # 調整視窗大小

# --------------------------
# student ID label and entry
label_id = tk.Label(root, text='Student ID')
label_id.pack(pady=(15,5))
entry_id = tk.Entry(root, width=25)
entry_id.pack()

# student name label and entry
label_name = tk.Label(root, text='Student Name')
label_name.pack(pady=(10,5))
entry_name = tk.Entry(root, width=25)
entry_name.pack()

# --------------------------
# function: print student info
def print_student():
    student_id = entry_id.get()
    student_name = entry_name.get()
    print('Student ID: {}'.format(student_id))
    print('Student Name: {}'.format(student_name))
    print('-' * 30)

# button: Print
button_print = tk.Button(root, text='Print', command=print_student)
button_print.pack(pady=15)

# --------------------------
# connect to database
conn = sqlite3.connect('Student.db')
cursor = conn.cursor()

# --------------------------
# function: create student
def create_student():
    student_id = entry_id.get()
    student_name = entry_name.get().lower()

    # 防止空白資料被新增
    if not student_id or not student_name:
        print("⚠️ Please enter both Student ID and Name!")
        return

    cursor.execute('INSERT INTO DB_student (db_student_id, db_student_name) VALUES (?, ?)', (student_id, student_name))
    conn.commit()

    print(f"✅ Added Student ID: {student_id}, Name: {student_name}")
    print('-' * 30)

# button: Create
button_create = tk.Button(root, text='Create', command=create_student)
button_create.pack(pady=10)

# --------------------------
# function: overview all students
def overview_student():
    cursor.execute('SELECT * from DB_student')
    overview = cursor.fetchall()
    print('📋 All Students:')
    for row in overview:
        print(row)
    print('-' * 30)

# button: Overview
button_overview = tk.Button(root, text='Overview', command=overview_student)
button_overview.pack(pady=10)

# --------------------------
# function: delete student
def delete_student():
    student_id = entry_id.get()

    if not student_id:
        print("⚠️ Please enter a Student ID to delete.")
        return

    cursor.execute('DELETE FROM DB_student WHERE db_student_id = ?', (student_id,))
    conn.commit()

    print(f"🗑️ Deleted record with Student ID: {student_id}")
    print('-' * 30)

# button: Delete
button_delete = tk.Button(root, text='Delete', command=delete_student)
button_delete.pack(pady=10)

# --------------------------
# GUI loop
root.mainloop()