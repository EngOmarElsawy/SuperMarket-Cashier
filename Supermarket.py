from tkinter import *
from tkinter import messagebox
from PIL import *
import webbrowser
import os
import sys as system
import subprocess

pro = Tk()
pro.geometry('1000x450+280+50')
pro.resizable(False, True)
pro.title('Supermarket')
pro.iconbitmap('.././Downloads/geometric-circuit-board-chip-logo-260nw-1316268161.ico')
pro.resizable(False,False)
title = Label(pro, text='Supermarket System', fg='white', bg='gold', font=("tajawal", 16, 'bold'))
title.pack(fill=X)


u1 = 'https://www.facebook.com/profile.php?id=100008086907024'
u2 = 'https://web.telegram.org/z/'

def Open1():
    webbrowser.open_new(u1)
def Open2():
    webbrowser.open_new(u2)
def about1():
    messagebox.showinfo('المطور',' عمر الصاوي')
def about2():
    messagebox.showinfo('مشروع',' سوبرماركت')
def log():
    user = En1.get()
    passw = En2.get()
    if user == 'omar' and passw == '123456':
        fileName = './bettersuper.py'
        os.system('open bettersuper.py')
        pro.destroy()
    else:
        messagebox.showerror('خطأ','للأسف البيانات خاطئة')

color = '#0B2F3A'

# F1 = Frame(pro, width=230, height=420, bg='#0B2F3A')
# F1.place(x=570, y=37) 
# Title1 = Label(F1, text="مشروع سوبر ماركت", bg='#0B2F3A',fg='white' , font=('tajawal', 12, 'bold'))
# Title1.place(x=42, y=10)
# Title2 = Label(F1, text="المطور عمر الصاوي", bg='#0B2F3A',fg='white' , font=('tajawal', 12, 'bold'))
# Title2.place(x=52, y=50)
# Title3 = Label(F1, text="وسائل الأتصال بنا", bg='#0B2F3A',fg='white' , font=('tajawal', 12, 'bold'))
# Title3.place(x=50, y=90)

# B1 = Button(F1, text='حسابنا علي الفيس بوك', width=26 , fg='black', bg='#DBA901',font=('tajawal', 12, 'bold'),command=Open1)
# B1.place(x=6, y=150)
# B2 = Button(F1, text='حسابنا علي التليجرام', width=26 , fg='black', bg='#DBA901',font=('tajawal', 12, 'bold'),command=Open2)
# B4 = Button(F1, text='لمحة عن المشروع', width=26 , fg='black', bg='#DBA901',font=('tajawal', 12, 'bold'),command=about2)
# B4.place(x=6, y=200)
# B5 = Button(F1, text='لمحة عن المطور', width=26 , fg='black', bg='#DBA901',font=('tajawal', 12, 'bold'),command=about1)
# B5.place(x=6, y=250)
# B6 = Button(F1, text='اغلاق البرنامج', width=26 , fg='black', bg='#DBA901',font=('tajawal', 12, 'bold'),command=quit)
# B6.place(x=6, y=300)

photo = PhotoImage(file="./Supermarket.png")
imo = Label(pro, image=photo)
imo.place(x=-20,y=25,width=1036,height=300)

F2 = Frame(pro, width=1000, height=150, background='#0B2F3A')
F2.place(x=0, y=300)


L1 = Label(F2, text='اسم المستخدم', fg='gold', bg=color , font=('tajawal', 12, 'bold'))
L1.place(x=780, y=25)
L2 = Label(F2, text='كلمة المرور', fg='gold', bg=color , font=('tajawal', 12, 'bold'))
L2.place(x=780, y=70)
En1 = Entry(F2, font=('tajawal', 12, 'bold'), justify=CENTER)
En1.place(x=500, y=26)
En2 = Entry(F2, font=('tajawal', 12, 'bold'), justify=CENTER)
En2.place(x=500, y=71)
B = Button(F2, text='تسجيل الدخول', bg='#DBA901', font=('tajawal', 12, 'bold'), width=12, height=3,command=log)
B.place(x=300,y=30)


pro.mainloop()
