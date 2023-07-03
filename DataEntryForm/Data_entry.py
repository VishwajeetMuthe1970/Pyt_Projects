from tkinter import *
import tkinter as tk
import sqlite3
from tkinter import messagebox

# from tkinter import messagebox

root = Tk()
root.geometry('600x500')
root.title("DATA ENTRY FORM")
root.config(bg="silver")

serial = StringVar()
area = StringVar()
name = StringVar()
mobile = StringVar()
gender = StringVar()
age = StringVar()
education = StringVar()
occupation = StringVar()


def data():
    serial_no = serial.get()
    Area = area.get()
    Name = name.get()
    Mob = mobile.get()
    Gen = gender.get()
    Ag = age.get()
    Edu = education.get()
    Occ = occupation.get()

    # Creating a Databse.
    conn = sqlite3.connect('Form.db')
    with conn:
        cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS BIODATA(Sr_No INT,AREA TEXT ,NAME TEXT ,MOBILE INT ,GENDER TEXT ,AGE INT,EDUCATION TEXT ,OCCUPATION TEXT )")
    cursor.execute(
        'INSERT INTO BIODATA(Sr_No,Area,Name,Mobile,Gender,Age,Education,Occupation) VALUES(?,?,?,?,?,?,?,?)',
        (serial_no, Area, Name, Mob, Gen, Ag, Edu, Occ))
    cursor.close()
    conn.commit()
    conn.close()

    entry_1.delete(0, END)
    entry_2.delete(0, END)
    entry_3.delete(0, END)
    entry_4.delete(0, END)
    entry_5.delete(0, END)
    entry_6.delete(0, END)
    entry_7.delete(0, END)
    entry_8.delete(0, END)



def edit():
    """
    Search for how to make the popup window to get the field number.
    :return:
    """
    pass


# TITLE
label_0 = Label(root, text="DATA ENTRY FORM", width=20, font=("Times New Roman""bold", 30), background="silver")
label_0.grid(row=3, column=2, padx=305, pady=15)
# Sub Title
label_1 = Label(root, text="AUDIENCE RESEARCH UNIT", width=30, font=("Times New Roman""bold", 15), background="silver")
label_1.grid(row=4, column=2, padx=105)
# Sr. No.
label_2 = Label(root, text="Sr. No.   ", width=10, font=("Times New Roman""bold", 14), background="silver")
label_2.grid(row=5, column=0, ipady=20)
# Area
label_3 = Label(root, text="Area        ", width=10, font=("Times New Roman""bold", 14), background="silver")
label_3.grid(row=6, column=0, padx=0, ipady=20, ipadx=0)
# Name
label_4 = Label(root, text="Name      ", width=10, font=("Times New Roman""bold", 14), background="silver")
label_4.grid(row=7, column=0, ipady=20)
# Mobile
label_5 = Label(root, text="Mobile    ", width=10, font=("Times New Roman""bold", 14), background="silver")
label_5.grid(row=8, column=0, ipady=20)
# Gender
label_6 = Label(root, text="Gender    ", width=10, font=("Times New Roman""bold", 14), background="silver")
label_6.grid(row=9, column=0, ipady=20)
# Age
label_7 = Label(root, text="Age       ", width=10, font=("Times New Roman""bold", 14), background="silver")
label_7.grid(row=10, column=0, ipady=20, ipadx=0)
# Education
label_8 = Label(root, text="Education ", width=10, font=("Times New Roman""bold", 14), background="silver")
label_8.grid(row=11, column=0, ipady=20)
# Occupation
label_9 = Label(root, text="Occupation", width=10, font=("Times New Roman""bold", 14), background="silver")
label_9.grid(row=12, column=0, ipady=20)

# Textbox
# Sr. nO.
entry_1 = tk.Entry(root, textvariable=serial)
entry_1.grid(row=5, column=1)
# Area
entry_2 = tk.Entry(root, textvariable=area)
entry_2.grid(row=6, column=1)
# Name
entry_3 = tk.Entry(root, textvariable=name)
entry_3.grid(row=7, column=1)
# Mobile
entry_4 = tk.Entry(root, textvariable=mobile)
entry_4.grid(row=8, column=1)
# Gender
entry_5 = tk.Entry(root, textvariable=gender)
entry_5.grid(row=9, column=1)
# Age
entry_6 = tk.Entry(root, textvariable=age)
entry_6.grid(row=10, column=1)
# Education
entry_7 = tk.Entry(root, textvariable=education)
entry_7.grid(row=11, column=1)
# Occupation
entry_8 = tk.Entry(root, textvariable=occupation)
entry_8.grid(row=12, column=1)

# BUTTONS

# Add Record
b1 = Button(root, text='Add Record', font=("Times New Roman""bold", 14), width=20, height=2, bg='grey', fg='white',
            command=data)
b1.grid(row=5, column=2, padx=305, pady=15)

# Edit Record
b2 = Button(root, text='Edit Record', font=("Times New Roman""bold", 14), width=20, height=2, bg='grey', fg='white',
            command=data)
b2.grid(row=6, column=2, padx=305, pady=15)

# Delete Record
b3 = Button(root, text='Delete Record', font=("Times New Roman""bold", 14), width=20, height=2, bg='grey', fg='white',
            command=data)
b3.grid(row=8, column=2, padx=305, pady=15)
# Save and Exit
b4 = Button(root, text='Save and Exit', font=("Times New Roman""bold", 14), width=20, height=2, bg='grey', fg='white',
            command=data)
b4.grid(row=9, column=2, padx=305, pady=15)
root.mainloop()
