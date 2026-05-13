import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk
import random
import sqlite3
from datetime import datetime

# ============ Products (arabic_name, english_name, price) ============
PRODUCTS = [
    ('البقوليات', [
        ('الرز',         'Rice',           5),
        ('البرغل',       'Borkhl',         10),
        ('قاسوليا',      'Fasolia',        15),
        ('عدس',          '3ds',            2),
        ('معكرونة',      'Maqarona',       4),
        ('فريكة',        'Feryq',          5),
        ('حمص',          'Homs',           18),
        ('فول',          'Beans',          4),
        ('طعمية',        'Ta3meya',        4),
        ('بذنجان',       'Bazengan',       10),
        ('بطاطس',        'Potatoes',       5),
        ('ترمس حلو',     'Termas Helw',    15),
        ('بسلة',         'Besla',          4),
        ('قلقاس',        'Qolqas',         8),
        ('بميا',         'Bamya',          3),
        ('الترمس',       'Termas',         5),
        ('اللوبيا',      'Lobya',          5),
        ('البازلاء',     'Besala',         4),
        ('عدس احمر',     '3ds Ah7mar',     10),
        ('عدس اخضر',     '3ds A5der',      12),
        ('الادمامي',     'Admamy',         5),
    ]),
    ('اللوازم المنزلية', [
        ('مصفاة',        'Masfa',          20),
        ('صحن',          'Sahn',           20),
        ('كأس',          'Kas',            5),
        ('سكين',         'Knife',          10),
        ('شوك',          'Fork',           5),
        ('طنجرة',        'Tangara',        20),
        ('ملعقة',        'Spoon',          10),
        ('شاحن',         'Shahn',          40),
        ('سلة',          'Basket',         15),
        ('صينية',        'Sanya',          50),
        ('وعاء الخلط',   'W3a 5alt',       15),
        ('فتاحة العلب',  'Bottle Opener',  10),
        ('مقشرة',        'Makshra',        25),
        ('محفظة',        'Mahfza',         20),
        ('اكياس',        'Akyas',          10),
        ('سلة قمامة',    'Garbage Basket', 20),
        ('اكواب',        'Cups',           15),
        ('علب',          '3lba',           20),
        ('لوحة التقطيع', 'Cutting Plate',  10),
        ('حفارة',        'Hfaar',          30),
        ('كبشة',         'Kabsha',         25),
    ]),
    ('أدوات كهربائية', [
        ('تلفزيون',          'T.V.',            10000),
        ('غسالة',            'Washer',          15000),
        ('ثلاجة',            'Fridge',          20000),
        ('مكرويف',           'Microwave',       1000),
        ('خلاط',             'Blender',         1000),
        ('مقلاة كهربائية',   'Electric Pan',    2000),
        ('راديو',            'Radio',           500),
        ('بلاي ستيشن',       'Playstation',     15000),
        ('فلتر ماء',         'Water Filter',    3000),
        ('مكواة',            'Iron',            1000),
        ('مبرد',             'Cooler',          1000),
        ('مروحة ارضية',      'Floor Fan',       400),
        ('تكييف',            'Air Conditioner', 10000),
        ('فرن غاز',          'Gas Oven',        1000),
        ('مكنسة',            'Vacuum',          500),
        ('سخان',             'Heater',          3000),
        ('مشترك كهربائي',    'Power Strip',     500),
        ('شاشة كمبيوتر',     'Monitor',         5000),
        ('مروحة سقف',        'Ceiling Fan',     200),
    ]),
]

# ============ Database ============
db = sqlite3.connect("Super.db")
cr = db.cursor()
cr.execute("""CREATE TABLE IF NOT EXISTS Customer(
    customer_name TEXT, customer_phone TEXT, customer_bill TEXT, customer_address TEXT)""")
cr.execute("""CREATE TABLE IF NOT EXISTS Sales(
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    bill_number  TEXT,
    customer_name TEXT,
    customer_phone TEXT,
    total_amount  REAL,
    sale_date     TEXT)""")
db.commit()

# ============ Theme ============
mainFont  = 'tajawal'
mainColor = '#0B2F3A'
frameBg   = '#0B4C5F'

# ============ Root Window ============
root = Tk()
root.geometry('1330x800+30+10')
root.title('Supermarket')
root.resizable(False, False)
Label(root, text='ادارة المشتريات', fg='white', bg=mainColor, font=('tajawal', 15)).pack(fill=X)

# ============ State Variables ============
quantities      = [[IntVar() for _ in items] for _, items in PRODUCTS]
total_vars      = [StringVar(value='$0') for _ in PRODUCTS]
customername    = StringVar()
customerphone   = StringVar()
customerfatora  = StringVar(value=str(random.randint(1000, 9999)))
customeraddress = StringVar()
customermail    = StringVar()

# ============ Calculation ============
def category_total(idx):
    items = PRODUCTS[idx][1]
    return sum(quantities[idx][i].get() * items[i][2] for i in range(len(items)))

def total():
    totals = [category_total(i) for i in range(len(PRODUCTS))]
    for i, v in enumerate(total_vars):
        v.set(f'${totals[i]}')
    welcome()
    bill(totals)

# ============ Bill Display ============
def welcome():
    textarea.config(state=NORMAL)
    textarea.delete('1.0', END)
    textarea.insert(END, "\t Supermarket says Hello!")
    textarea.insert(END, "\n ======================================")
    textarea.insert(END, f"\n\tB.Num:   {customerfatora.get()}")
    textarea.insert(END, f"\n\tNAME:    {customername.get()}")
    textarea.insert(END, f"\n\tPHONE:   {customerphone.get()}")
    textarea.insert(END, f"\n\tADDRESS: {customeraddress.get()}")
    textarea.insert(END, f"\n\tEMAIL:   {customermail.get()}")
    textarea.insert(END, "\n======================================")
    textarea.insert(END, "\n Item              Qty    Price")
    textarea.insert(END, "\n======================================")

def bill(totals):
    for cat_idx, (_, items) in enumerate(PRODUCTS):
        for i, (ar_name, en_name, price) in enumerate(items):
            qty = quantities[cat_idx][i].get()
            if qty:
                textarea.insert(END, f"\n{en_name:<18} {qty:<6} {qty * price}")
    textarea.insert(END, "\n--------------------------------------")
    textarea.insert(END, f"\nTotal:             {sum(totals)}$")
    textarea.config(state=DISABLED)

# ============ Clear ============
def Clear():
    for cat_vars in quantities:
        for v in cat_vars:
            v.set(0)
    for v in total_vars:
        v.set('$0')
    customername.set('')
    customerphone.set('')
    customeraddress.set('')
    customermail.set('')
    textarea.config(state=NORMAL)
    textarea.delete(1.0, END)
    textarea.config(state=DISABLED)
    customerfatora.set(str(random.randint(1000, 9999)))

# ============ Database Functions ============
def Database_Add():
    try:
        EntFatora.config(state=NORMAL)
        cr.execute(
            "INSERT INTO Customer(customer_name, customer_phone, customer_bill, customer_address) VALUES(?, ?, ?, ?)",
            (EntName.get(), EntPhone.get(), EntFatora.get(), addressValue.get())
        )
        db.commit()
        messagebox.showinfo('ADDED', 'Customer Info Added')
        EntFatora.config(state=DISABLED)
    except sqlite3.OperationalError as e:
        messagebox.showerror('Error', str(e))

def Database_Search():
    EntFatora.config(state=NORMAL)
    cr.execute(
        "SELECT * FROM Customer WHERE customer_name = ? AND customer_phone = ?",
        (EntName.get(), EntPhone.get())
    )
    result = cr.fetchone()
    if result:
        messagebox.showinfo('Found', str(result))
    else:
        messagebox.showerror("Not Found", "Customer Not Found")
    EntFatora.config(state=DISABLED)

# ============ Save Bill ============
def Print():
    textarea.config(state=NORMAL)
    bill_text = textarea.get(1.0, END)
    now       = datetime.now()
    timestamp = now.strftime("\n======== %Y-%m-%d %H:%M:%S ============\n")
    with open("Fatora1.txt", "a+", encoding="utf-8") as f:
        f.write(f"\n\n{bill_text}{timestamp}")
    with open("Fatora.txt", "w", encoding="utf-8") as f:
        f.write(f"\n\n{bill_text}{timestamp}")
    grand = sum(category_total(i) for i in range(len(PRODUCTS)))
    cr.execute(
        "INSERT INTO Sales(bill_number, customer_name, customer_phone, total_amount, sale_date) VALUES(?, ?, ?, ?, ?)",
        (customerfatora.get(), customername.get(), customerphone.get(), grand, now.strftime("%Y-%m-%d %H:%M:%S"))
    )
    db.commit()
    textarea.config(state=DISABLED)
    messagebox.showinfo('Saved', 'Bill saved successfully')

# ============ Send Email ============
def Send():
    from mailtest import sendEmail, smtplib
    try:
        sendEmail(customermail.get())
        messagebox.showinfo('Sent', 'Receipt Sent')
    except smtplib.SMTPRecipientsRefused:
        messagebox.showerror("Error", "Write a valid email address")

# ============ Sales Report ============
def show_report():
    win = Toplevel(root)
    win.title('Sales Report')
    win.geometry('900x520')
    win.configure(bg=mainColor)
    Label(win, text='Sales History', font=('tajawal', 14, 'bold'), bg=mainColor, fg='gold').pack(pady=8)

    sf = Frame(win, bg=mainColor)
    sf.pack(fill=X, padx=10, pady=4)
    today = datetime.now().strftime("%Y-%m-%d")
    cr.execute("SELECT COALESCE(SUM(total_amount), 0) FROM Sales WHERE sale_date LIKE ?", (f"{today}%",))
    today_total = cr.fetchone()[0]
    cr.execute("SELECT COALESCE(SUM(total_amount), 0), COUNT(*) FROM Sales")
    all_total, count = cr.fetchone()
    Label(sf, text=f"Today: ${today_total:.0f}",   bg=mainColor, fg='white', font=('tajawal', 11)).pack(side=LEFT, padx=20)
    Label(sf, text=f"All Time: ${all_total:.0f}",  bg=mainColor, fg='white', font=('tajawal', 11)).pack(side=LEFT, padx=20)
    Label(sf, text=f"Total Bills: {count}",         bg=mainColor, fg='white', font=('tajawal', 11)).pack(side=LEFT, padx=20)

    frame = Frame(win)
    frame.pack(fill=BOTH, expand=True, padx=10, pady=10)
    cols = ('Bill #', 'Customer', 'Phone', 'Total', 'Date')
    tree = ttk.Treeview(frame, columns=cols, show='headings', height=22)
    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, width=160, anchor='center')
    scroll = ttk.Scrollbar(frame, orient=VERTICAL, command=tree.yview)
    tree.configure(yscrollcommand=scroll.set)
    cr.execute("SELECT bill_number, customer_name, customer_phone, total_amount, sale_date FROM Sales ORDER BY sale_date DESC")
    for row in cr.fetchall():
        tree.insert('', END, values=(row[0], row[1] or '—', row[2] or '—', f'${row[3]:.0f}', row[4]))
    tree.pack(side=LEFT, fill=BOTH, expand=True)
    scroll.pack(side=RIGHT, fill=Y)

# ============ UI: Customer Frame ============
F1 = Frame(root, bd=2, width=338, height=225, bg='#0B4C5F')
F1.place(x=990, y=35)
Label(F1, text='بيانات المشتري', font=('tajawal', 13, 'bold'), bg='#0B4C5F', fg='tomato').place(x=100, y=2)
for label_text, y_pos in [('الاسم', 18), ('رقم الهاتف', 48), ('رقم الفاتورة', 78), ('البريد الالكتروني', 108), ('العنوان', 138)]:
    Label(F1, text=label_text, font=('tajawal', 10), bg='#0B4C5F', fg='white').place(x=200, y=y_pos)
EntName      = Entry(F1, textvariable=customername,    justify='center'); EntName.place(x=20, y=18)
EntPhone     = Entry(F1, textvariable=customerphone,   justify='center'); EntPhone.place(x=20, y=48)
EntFatora    = Entry(F1, textvariable=customerfatora,  justify='center', state=DISABLED); EntFatora.place(x=20, y=78)
Entmail      = Entry(F1, textvariable=customermail,    justify='center'); Entmail.place(x=20, y=108)
addressValue = Entry(F1, textvariable=customeraddress, justify=CENTER);   addressValue.place(x=20, y=138)
Button(F1, text='بحث',   font=('tajawal', 11), width=9, bg='white', borderwidth=0, command=Database_Search).place(x=20,  y=180)
Button(F1, text='اضافة', font=('tajawal', 11), width=9, bg='white', borderwidth=0, command=Database_Add).place(   x=155, y=180)

# ============ UI: Bill Frame ============
F3 = Frame(root, bd=2, bg='#E3E4DB', width=350, height=440)
F3.place(x=985, y=262)
scroll_y = Scrollbar(F3, orient=VERTICAL)
textarea = Text(F3, bg='#E3E4DB', width=35, height=25, font=mainFont, yscrollcommand=scroll_y.set)
scroll_y.pack(side=LEFT, fill=Y)
scroll_y.config(command=textarea.yview)
textarea.pack(fill=BOTH, expand=1)
textarea.config(state=DISABLED)

# ============ UI: Controls Frame ============
F4 = Frame(root, bd=2, width=800, height=120, bg='#0B4C5F')
F4.place(x=640, y=678)
cat_labels = ['الحساب الكلي للبقوليات', 'حساب اللوازم المنزلية', 'حساب ادوات الكهرباء']
for i, (lbl, var) in enumerate(zip(cat_labels, total_vars)):
    Label(F4, text=lbl, font=(mainFont, 10, 'bold'), bg=frameBg, fg='gold').place(x=235, y=10 + i * 30)
    Entry(F4, textvariable=var, width=24, state=DISABLED).place(x=2, y=12 + i * 30)
Button(F4, text='الحساب',         width=15, borderwidth=0, font=mainFont, bg='#DBA901', command=total).place(      x=520, y=10)
Button(F4, text='تصدير الفاتورة', width=15, borderwidth=0, font=mainFont, bg='#DBA901', command=Print).place(      x=520, y=45)
Button(F4, text='فاتورة الكترونية',width=15, borderwidth=0, font=mainFont, bg='#DBA901', command=Send).place(      x=520, y=80)
Button(F4, text='تقرير المبيعات', width=13, borderwidth=0, font=mainFont, bg='#DBA901', command=show_report).place(x=360, y=80)
Button(F4, text='افراغ الحقول',   width=13, borderwidth=0, font=mainFont, bg='#DBA901', command=Clear).place(      x=360, y=10)
Button(F4, text='اغلاق البرنامج', width=13, borderwidth=0, font=mainFont, bg='#DBA901', command=root.quit).place(  x=360, y=45)

# ============ UI: Product Frames ============
FRAME_CONFIGS = [(1, 318, 800), (321, 318, 800), (641, 338, 640)]
for cat_idx, (cat_name, items) in enumerate(PRODUCTS):
    x, w, h = FRAME_CONFIGS[cat_idx]
    frame = Frame(root, bd=2, width=w, height=h, bg=frameBg)
    frame.place(x=x, y=35)
    Label(frame, text=cat_name, font=(mainFont, 15, 'bold'), bg=frameBg, fg='gold').place(x=80, y=0)
    for i, (ar_name, _, price) in enumerate(items):
        y_pos = 50 + i * 30
        Label(frame, text=ar_name, font=(mainFont, 11), bg=frameBg, fg='white').place(x=175, y=y_pos)
        Entry(frame, textvariable=quantities[cat_idx][i], width=14).place(x=70, y=y_pos)

root.mainloop()
