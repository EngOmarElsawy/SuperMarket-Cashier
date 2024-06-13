# from bettersuper import mainFont,mainColor,frameBg
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import sqlite3
# ============ Fonts and Colors =============
mainFont = 'tajawal'
mainColor = '#0B2F3A' 
frameBg = '#0B4C5F'
#=================== Setting Screen ==================
root = Tk()
root = root
root.geometry('1330x800+30+10')
root.configure(background=frameBg)
root.title('Supermarket')
root.resizable(True,True)
root.iconbitmap('D:/Omar/Codezilla/Images/iice.ico')
title = Label(  root,text='ادارة المخزون',fg='white',bg=mainColor, font=('tajawal',15))
title.pack(fill=X)
# root.iconbitmap('../Downloads/311804053_3448602958752567_1147801703367297556_n')

# Create the root window
def mailAlert(current_amount,item_name,required_amount):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.application import MIMEApplication


# email information
    from_email = "omarelsawy160@gmail.com"
    to_email = "omar.future.123@gmail.com"
    password = "qxnsyaxbqeatgtxs"

    # item information
    # item_name = 
    # current_amount =  
    # required_amount = 0.
    if current_amount < required_amount:
        message = f"Subject: {item_name} supply low\n\nThe current amount of {item_name} is {current_amount}, which is less than the required amount of {required_amount}. Please restock as soon as possible."
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(from_email, password)
            connection.sendmail(from_email, to_email, message)
            print(f"Email sent to {to_email}")
    else:
        print(f"The current amount of {item_name} is sufficient")


# Create the table
table = ttk.Treeview(root, columns=('col1', 'col2', 'col3', 'col4', 'col5', 'col6','col7','col8','col9'), show='headings',height=40)


# Add 19 rows to every column
itemList2 = ['الرز', 'البرغل', 'قاسوليا', 'عدس', 'معكرونة', 'فريكة', 'حمص', 'فول', 'طعمية', 'بذنجان', 'بطاطس', 'ترمس حلو', 'بسلة', 'قلقاس', 'بميا', 'الترمس', 'اللوبيا', 'البازلاء', 'عدس احمر', 'عدس اخضر', 'الادمامي']
itemsList1 = ['تلفزيون', 'غسالة', 'ثلاجة', 'مكرويف', 'خلاط', 'مقلاة كهربائية', 'راديو', 'بلاي ستيشن', 'فلتر ماء', 'مكواة', 'مبرد', 'مروحة ارضية', 'تكييف', 'فرن غاز', 'مكنسة', 'سخان', 'مشترك كهربائي', 'شاشة كمبيوتر', 'مروحة سقف']
itemList3 = ['مصفاة', 'صحن', 'كأس', 'سكين', 'شوك', 'طنجرة', 'ملعقة', 'شاحن', 'سلة', 'صينية', 'وعاء الخلط', 'فتاحة العلب', 'مقشرة', 'محفظة', 'اكياس', 'سلة قمامة', 'اكواب', 'علب', 'لوحة التقطيع', 'حفارة', 'كبشة']
db = sqlite3.connect('mydatabase.db')
cr = db.cursor()
cr.execute("select * from Foods")
results = cr.fetchall()
for i in range(len(itemsList1)):
    table.insert("", "end", values=('\t'))
    table.insert("", "end", values=(itemsList1[i],results[i][4],results[i][5],itemList2[i],results[i][1],results[i][2],itemList3[i],results[i][7],results[i][8]))
for i in range(9):    
    table.column(f'col{i+1}',anchor='e',)
    table.tag_configure(f'col{i+1}',background='gray',foreground='white')
    table.column(f'col{i+1}', width=200, stretch=False,anchor='center')
    # table.tag_configure(f'col{i+1}',)

table.heading('col1', text='الادوات الكهربائية',anchor='e')
table.heading('col2', text='الكمية',anchor='e')
table.heading('col3', text=' السعر',anchor='e')
table.heading('col4', text=' الاغذية',anchor='e')
table.heading('col5', text=' الكمية',anchor='e')
table.heading('col6', text='السعر',anchor="e")
table.heading('col7', text='اللوازم المنزلية',anchor='e')
table.heading('col8', text='الكمية',anchor='e')
table.heading('col9', text='السعر',anchor="e")
table.pack(pady=25)

totalamountOfNutrition = 200
totalamountOfElec = 200
totalamountOfInventory = 200
cr.execute("select quantity1 from Foods")
amountOfNutrition = cr.fetchall()
cr.execute("select Nutrition from Foods")
nameOfNutrition = cr.fetchall()
cr.execute("select quantity2 from Foods")
amountOfElec = cr.fetchall()
cr.execute("select Electricity from Foods")
nameOfElec = cr.fetchall()
cr.execute("select quantity3 from Foods")
amountOfInventory = cr.fetchall()
cr.execute("select Inventory from Foods")
nameOfInventory = cr.fetchall()
for i in range(len(amountOfNutrition)):
    for j in range (len(nameOfNutrition)):
        if amountOfNutrition[i][0] != '' and float(amountOfNutrition[i][0]) < 0.2 * totalamountOfNutrition:
            messagebox.showerror('Alert',f'Amount of {nameOfNutrition[j][0]}')
            mailAlert(amountOfNutrition[i][0],nameOfNutrition[j],totalamountOfNutrition*0.2)
            break
        else:
            pass

for i in range(len(amountOfElec)):
    for j in range (len(nameOfElec)):
        if amountOfElec[i][0] != '' and float(amountOfElec[i][0]) < 0.2 * totalamountOfElec:
            messagebox.showerror('Alert',f'Amount of {nameOfElec[j][0]}')
            mailAlert(amountOfElec[i][0],nameOfElec[j],totalamountOfElec*0.2)
            break
        else:
            pass
for i in range(len(amountOfInventory)):
    for j in range (len(nameOfInventory)):
        if amountOfInventory[i][0] != '' and float(amountOfInventory[i][0]) < 0.2 * totalamountOfInventory:
            # item_name = nameOfInventory[j][0].strip("()'")
            messagebox.showerror('Alert',f'Amount of {nameOfNutrition[j][0]}')
            mailAlert(amountOfInventory[i][0],nameOfInventory[j],totalamountOfInventory*0.2)
            break
        else:
            pass
# # Create the text area
# text_area = tk.Text(root, height=3, font=('tajawal',18))
# text_area.pack()

# # Create the "Add Item" button
# add_item_button = tk.Button(root,bg=mainColor ,text="Add Item", command=add_item)
# add_item_button.pack(pady=10)


root.mainloop()