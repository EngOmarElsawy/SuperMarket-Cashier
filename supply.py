from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
import configparser
import smtplib

mainFont  = 'tajawal'
mainColor = '#0B2F3A'
frameBg   = '#0B4C5F'

root = Tk()
root.geometry('1330x800+30+10')
root.configure(background=frameBg)
root.title('Supermarket - Inventory')
root.resizable(True, True)
Label(root, text='ادارة المخزون', fg='white', bg=mainColor, font=('tajawal', 15)).pack(fill=X)


def mailAlert(current_amount, item_name, required_amount):
    config        = configparser.ConfigParser()
    config.read('config.ini')
    from_email    = config['email']['from_email']
    password      = config['email']['password']
    manager_email = config['email']['manager_email']
    message = (
        f"Subject: Low Stock Alert - {item_name}\n\n"
        f"The current amount of {item_name} is {current_amount}, "
        f"which is below the required threshold of {required_amount:.0f}. "
        f"Please restock as soon as possible."
    )
    with smtplib.SMTP("smtp.gmail.com", 587) as conn:
        conn.starttls()
        conn.login(from_email, password)
        conn.sendmail(from_email, manager_email, message)
    print(f"Low-stock alert sent for {item_name}")


# ============ Item Name Lists ============
itemList_food  = ['الرز', 'البرغل', 'قاسوليا', 'عدس', 'معكرونة', 'فريكة', 'حمص', 'فول', 'طعمية',
                  'بذنجان', 'بطاطس', 'ترمس حلو', 'بسلة', 'قلقاس', 'بميا', 'الترمس', 'اللوبيا',
                  'البازلاء', 'عدس احمر', 'عدس اخضر', 'الادمامي']
itemList_elec  = ['تلفزيون', 'غسالة', 'ثلاجة', 'مكرويف', 'خلاط', 'مقلاة كهربائية', 'راديو',
                  'بلاي ستيشن', 'فلتر ماء', 'مكواة', 'مبرد', 'مروحة ارضية', 'تكييف', 'فرن غاز',
                  'مكنسة', 'سخان', 'مشترك كهربائي', 'شاشة كمبيوتر', 'مروحة سقف']
itemList_house = ['مصفاة', 'صحن', 'كأس', 'سكين', 'شوك', 'طنجرة', 'ملعقة', 'شاحن', 'سلة', 'صينية',
                  'وعاء الخلط', 'فتاحة العلب', 'مقشرة', 'محفظة', 'اكياس', 'سلة قمامة', 'اكواب',
                  'علب', 'لوحة التقطيع', 'حفارة', 'كبشة']

# ============ Database ============
db = sqlite3.connect('mydatabase.db')
cr = db.cursor()
cr.execute("SELECT * FROM Foods")
results = cr.fetchall()

# ============ Inventory Table ============
cols = ('col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7', 'col8', 'col9')
table = ttk.Treeview(root, columns=cols, show='headings', height=40)
headers = ['الادوات الكهربائية', 'الكمية', 'السعر', 'الاغذية', 'الكمية', 'السعر', 'اللوازم المنزلية', 'الكمية', 'السعر']
for col, header in zip(cols, headers):
    table.heading(col, text=header, anchor='e')
    table.column(col, width=200, stretch=False, anchor='center')

for i, row in enumerate(results):
    elec  = itemList_elec[i]  if i < len(itemList_elec)  else ''
    food  = itemList_food[i]  if i < len(itemList_food)  else ''
    house = itemList_house[i] if i < len(itemList_house) else ''
    table.insert("", "end", values=(elec, row[4], row[5], food, row[1], row[2], house, row[7], row[8]))

table.pack(pady=25)

# ============ Low-Stock Alerts (one check per item, no nested loops) ============
THRESHOLD = 0.2 * 200

cr.execute("SELECT Nutrition, quantity1, Electricity, quantity2, Inventory, quantity3 FROM Foods")
for i, (food_name, qty1, elec_name, qty2, house_name, qty3) in enumerate(cr.fetchall()):
    food_label  = itemList_food[i]  if i < len(itemList_food)  else food_name
    elec_label  = itemList_elec[i]  if i < len(itemList_elec)  else elec_name
    house_label = itemList_house[i] if i < len(itemList_house) else house_name

    if qty1 and float(qty1) < THRESHOLD:
        messagebox.showerror('Alert', f'Low stock: {food_label}')
        mailAlert(float(qty1), food_label, THRESHOLD)

    if qty2 and float(qty2) < THRESHOLD:
        messagebox.showerror('Alert', f'Low stock: {elec_label}')
        mailAlert(float(qty2), elec_label, THRESHOLD)

    if qty3 and float(qty3) < THRESHOLD:
        messagebox.showerror('Alert', f'Low stock: {house_label}')
        mailAlert(float(qty3), house_label, THRESHOLD)

root.mainloop()
