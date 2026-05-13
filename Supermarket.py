from tkinter import *
from tkinter import messagebox
import sys
import subprocess
import sqlite3
import hashlib


def hash_pw(pw):
    return hashlib.sha256(pw.encode()).hexdigest()


# ============ User Database Setup ============
db = sqlite3.connect("Super.db")
cr = db.cursor()
cr.execute("CREATE TABLE IF NOT EXISTS Users(username TEXT PRIMARY KEY, password TEXT)")
cr.execute("SELECT COUNT(*) FROM Users")
if cr.fetchone()[0] == 0:
    cr.execute("INSERT INTO Users VALUES(?, ?)", ('omar', hash_pw('123456')))
    db.commit()

# ============ Window ============
pro = Tk()
pro.geometry('1000x450+280+50')
pro.resizable(False, False)
pro.title('Supermarket')
title = Label(pro, text='Supermarket System', fg='white', bg='gold', font=("tajawal", 16, 'bold'))
title.pack(fill=X)

color = '#0B2F3A'


def log():
    user  = En1.get()
    passw = En2.get()
    cr.execute("SELECT * FROM Users WHERE username = ? AND password = ?", (user, hash_pw(passw)))
    if cr.fetchone():
        subprocess.Popen([sys.executable, 'bettersuper.py'])
        pro.destroy()
    else:
        messagebox.showerror('خطأ', 'للأسف البيانات خاطئة')


photo = PhotoImage(file="./Supermarket.png")
imo   = Label(pro, image=photo)
imo.place(x=-20, y=25, width=1036, height=300)

F2 = Frame(pro, width=1000, height=150, background='#0B2F3A')
F2.place(x=0, y=300)

Label(F2, text='اسم المستخدم', fg='gold', bg=color, font=('tajawal', 12, 'bold')).place(x=780, y=25)
Label(F2, text='كلمة المرور',  fg='gold', bg=color, font=('tajawal', 12, 'bold')).place(x=780, y=70)

En1 = Entry(F2, font=('tajawal', 12, 'bold'), justify=CENTER)
En1.place(x=500, y=26)
En2 = Entry(F2, font=('tajawal', 12, 'bold'), justify=CENTER, show='*')
En2.place(x=500, y=71)

Button(F2, text='تسجيل الدخول', bg='#DBA901', font=('tajawal', 12, 'bold'),
       width=12, height=3, command=log).place(x=300, y=30)

pro.mainloop()
