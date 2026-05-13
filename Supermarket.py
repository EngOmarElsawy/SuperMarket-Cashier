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
pro.title('Supermarket — Login')
Label(pro, text='Supermarket System', fg='white', bg='#DBA901',
      font=("tajawal", 16, 'bold')).pack(fill=X)

color    = '#0B2F3A'
BTN_CLR  = '#DBA901'
BTN_HOV  = '#F0C030'


def log(event=None):
    user  = En1.get().strip()
    passw = En2.get()
    cr.execute("SELECT * FROM Users WHERE username = ? AND password = ?", (user, hash_pw(passw)))
    if cr.fetchone():
        subprocess.Popen([sys.executable, 'bettersuper.py'])
        pro.destroy()
    else:
        err_label.config(text='Username or password is incorrect', fg='#FF6B6B')


def toggle_password():
    if En2.cget('show') == '*':
        En2.config(show='')
        toggle_btn.config(text='Hide')
    else:
        En2.config(show='*')
        toggle_btn.config(text='Show')


# ============ Background Image ============
photo = PhotoImage(file="./Supermarket.png")
Label(pro, image=photo).place(x=-20, y=25, width=1036, height=300)

# ============ Login Form ============
F2 = Frame(pro, width=1000, height=150, background=color)
F2.place(x=0, y=300)
F2.pack_propagate(False)

# Labels
Label(F2, text='اسم المستخدم', fg='#DBA901', bg=color, font=('tajawal', 12, 'bold')).place(x=780, y=22)
Label(F2, text='كلمة المرور',  fg='#DBA901', bg=color, font=('tajawal', 12, 'bold')).place(x=780, y=67)

# Entries
En1 = Entry(F2, font=('tajawal', 12), justify=CENTER, relief='flat',
            highlightthickness=1, highlightcolor='#DBA901', highlightbackground='#555')
En1.place(x=490, y=22, width=270, height=30)

En2 = Entry(F2, font=('tajawal', 12), justify=CENTER, show='*', relief='flat',
            highlightthickness=1, highlightcolor='#DBA901', highlightbackground='#555')
En2.place(x=490, y=67, width=230, height=30)

# Show/Hide password toggle
toggle_btn = Button(F2, text='Show', bg='#1A3A4A', fg='#AAD4E8',
                    font=('tajawal', 9), borderwidth=0, cursor='hand2',
                    command=toggle_password, relief='flat')
toggle_btn.place(x=725, y=72)

# Login button with hover effect
login_btn = Button(F2, text='تسجيل الدخول', bg=BTN_CLR, fg='#1A1A1A',
                   font=('tajawal', 12, 'bold'), width=12, height=2,
                   borderwidth=0, cursor='hand2', relief='flat', command=log)
login_btn.place(x=290, y=30)
login_btn.bind('<Enter>', lambda e: login_btn.config(bg=BTN_HOV))
login_btn.bind('<Leave>', lambda e: login_btn.config(bg=BTN_CLR))

# Inline error label
err_label = Label(F2, text='', bg=color, fg='#FF6B6B', font=('tajawal', 10))
err_label.place(x=390, y=110)

# Enter key triggers login from either field
En1.bind('<Return>', log)
En2.bind('<Return>', log)

# Focus username field on launch
En1.focus_set()

pro.mainloop()
