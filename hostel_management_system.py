import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# Database Initialization
def initialize_database():
    conn = sqlite3.connect("hostel_management_system.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        room_number TEXT NOT NULL,
        phone_number TEXT NOT NULL,
        guardian_name TEXT,
        guardian_phone TEXT
    )
    """)
    conn.commit()
    conn.close()

# Functions for the System
def add_student():
    name = name_entry.get()
    room_number = room_number_entry.get()
    phone_number = phone_number_entry.get()
    guardian_name = guardian_name_entry.get()
    guardian_phone = guardian_phone_entry.get()

    if name and room_number and phone_number:
        conn = sqlite3.connect("hostel_management_system.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO students (name, room_number, phone_number, guardian_name, guardian_phone) VALUES (?, ?, ?, ?, ?)",
                       (name, room_number, phone_number, guardian_name, guardian_phone))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Student added successfully!")
        clear_entries()
        load_students()
    else:
        messagebox.showwarning("Input Error", "Please fill in all required fields.")

def clear_entries():
    name_entry.delete(0, tk.END)
    room_number_entry.delete(0, tk.END)
    phone_number_entry.delete(0, tk.END)
    guardian_name_entry.delete(0, tk.END)
    guardian_phone_entry.delete(0, tk.END)

def load_students():
    for row in student_table.get_children():
        student_table.delete(row)

    conn = sqlite3.connect("hostel_management_system.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    for student in students:
        student_table.insert("", tk.END, values=student)
    conn.close()

def delete_student():
    selected_item = student_table.selection()
    if selected_item:
        student_id = student_table.item(selected_item)["values"][0]
        conn = sqlite3.connect("hostel_management_system.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Student record deleted!")
        load_students()
    else:
        messagebox.showwarning("Selection Error", "Please select a student to delete.")

def search_student():
    query = search_entry.get()
    for row in student_table.get_children():
        student_table.delete(row)

    conn = sqlite3.connect("hostel_management_system.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE name LIKE ?", ('%' + query + '%',))
    students = cursor.fetchall()
    for student in students:
        student_table.insert("", tk.END, values=student)
    conn.close()

# GUI Setup
root = tk.Tk()
root.title("Hostel Management System")
root.geometry("800x500")

# Labels and Entry Fields
tk.Label(root, text="Student Name").grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Room Number").grid(row=1, column=0, padx=10, pady=5)
room_number_entry = tk.Entry(root)
room_number_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Phone Number").grid(row=2, column=0, padx=10, pady=5)
phone_number_entry = tk.Entry(root)
phone_number_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Guardian Name").grid(row=3, column=0, padx=10, pady=5)
guardian_name_entry = tk.Entry(root)
guardian_name_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Guardian Phone").grid(row=4, column=0, padx=10, pady=5)
guardian_phone_entry = tk.Entry(root)
guardian_phone_entry.grid(row=4, column=1, padx=10, pady=5)

# Buttons
tk.Button(root, text="Add Student", command=add_student).grid(row=5, column=0, padx=10, pady=10)
tk.Button(root, text="Clear Fields", command=clear_entries).grid(row=5, column=1, padx=10, pady=10)
tk.Button(root, text="Delete Student", command=delete_student).grid(row=5, column=2, padx=10, pady=10)

# Search Bar
tk.Label(root, text="Search Student by Name").grid(row=6, column=0, padx=10, pady=5)
search_entry = tk.Entry(root)
search_entry.grid(row=6, column=1, padx=10, pady=5)
tk.Button(root, text="Search", command=search_student).grid(row=6, column=2, padx=10, pady=5)

# Student Table
columns = ("ID", "Name", "Room Number", "Phone Number", "Guardian Name", "Guardian Phone")
student_table = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    student_table.heading(col, text=col)
    student_table.column(col, width=100)
student_table.grid(row=7, column=0, columnspan=3, padx=10, pady=10)

# Initialize Database and Load Students
initialize_database()
load_students()

root.mainloop()