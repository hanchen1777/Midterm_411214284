# initial environment
# import modules
import tkinter as tk
import sqlite3
from tkinter import messagebox

# basic GUI 
root = tk.Tk()
root.title('INTEGRATION')
root.geometry('300x400')  # 調整視窗大小

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

# Print function
def print_student():
    student_id = entry_id.get()
    student_name = entry_name.get()
    print ('Student ID: {}'.format(student_id))
    print ('Student Name: {}'.format(student_name))
    print ('-'*30)

button_print = tk.Button(root, text='Print', command=print_student)
button_print.pack(pady=15)

# Connect to database
conn = sqlite3.connect('Student.db')
cursor = conn.cursor()

# Create student function
def create_student():
    student_id = entry_id.get()
    student_name = entry_name.get().lower()
    if student_id == '' or student_name == '':
        messagebox.showwarning("Warning", "Student ID or Name cannot be empty!")
        return
    cursor.execute('INSERT INTO DB_student (db_student_id, db_student_name) VALUES(?,?)', (student_id, student_name))
    conn.commit()
    messagebox.showinfo("Success", f"Student {student_name} added.")
    print ('Student ID: {}'.format(student_id))
    print ('Student Name: {}'.format(student_name))
    print ('-' * 30)

button_create = tk.Button(root, text='Create', command=create_student)
button_create.pack(pady=10)

# Overview function
def overview_student():
    cursor.execute('SELECT * from DB_student')
    overview = cursor.fetchall()
    print(overview)
    messagebox.showinfo("Overview", "\n".join([str(s) for s in overview]))

button_overview = tk.Button(root, text='Overview', command=overview_student)
button_overview.pack(pady=10)

# ===== 新增 Delete Button 功能 =====
def delete_student():
    student_id = entry_id.get()
    if student_id == '':
        messagebox.showwarning("Warning", "Please enter Student ID to delete.")
        return
    cursor.execute('SELECT * FROM DB_student WHERE db_student_id=?', (student_id,))
    result = cursor.fetchone()
    if result:
        cursor.execute('DELETE FROM DB_student WHERE db_student_id=?', (student_id,))
        conn.commit()
        messagebox.showinfo("Success", f"Student ID {student_id} deleted.")
        print(f"Deleted Student ID: {student_id}")
    else:
        messagebox.showerror("Error", f"Student ID {student_id} not found.")

button_delete = tk.Button(root, text='Delete', command=delete_student)
button_delete.pack(pady=15)
# =================================

root.mainloop()

def delete_student():
    student_id = entry_id.get()
    cursor.execute('SELECT * from DB_student where db_student_id = ?',(student_id))
    delete = cursor.fetchall()
    cursor.execute('DELETE from DB_student where db_student_id = ?',(student_id))
    print('Following row is delete:', delete)
    conn.commit()

botton_delete = tk.Button(root, text = 'Delete', command = delete_student)
botton_delete.pack(pady = 25)