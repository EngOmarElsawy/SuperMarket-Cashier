from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
import configparser
import smtplib

mainFont  = 'tajawal'
mainColor = '#0B2F3A'
frameBg   = '#0B4C5F'

root = Tk()
root.geometry('1330x820+30+10')
root.configure(background=mainColor)
root.title('Supermarket — Inventory')
root.resizable(True, True)
Label(root, text='ادارة المخزون', fg='white', bg=mainColor,
      font=('tajawal', 15, 'bold')).pack(fill=X, pady=2)


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

# ============ Treeview Style ============
style = ttk.Style()
style.theme_use('default')
style.configure('Inventory.Treeview',
    background='#0D3A4A',
    foreground='white',
    fieldbackground='#0D3A4A',
    rowheight=28,
    font=(mainFont, 10))
style.configure('Inventory.Treeview.Heading',
    background='#0B2F3A',
    foreground='#DBA901',
    font=(mainFont, 11, 'bold'),
    relief='flat',
    padding=6)
style.map('Inventory.Treeview',
    background=[('selected', '#1A6B8A')],
    foreground=[('selected', 'white')])

# ============ Table Frame with Scrollbar ============
table_frame = Frame(root, bg=mainColor)
table_frame.pack(fill=BOTH, expand=True, padx=15, pady=10)

cols = ('col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7', 'col8', 'col9')
table = ttk.Treeview(table_frame, columns=cols, show='headings',
                     height=30, style='Inventory.Treeview')

headers = ['الادوات الكهربائية', 'الكمية', 'السعر',
           'الاغذية', 'الكمية', 'السعر',
           'اللوازم المنزلية', 'الكمية', 'السعر']
col_widths = [175, 90, 90, 175, 90, 90, 175, 90, 90]
for col, header, w in zip(cols, headers, col_widths):
    table.heading(col, text=header, anchor='center')
    table.column(col, width=w, stretch=False, anchor='center')

table.tag_configure('even', background='#0B4C5F', foreground='white')
table.tag_configure('odd',  background='#0D3A4A', foreground='white')
table.tag_configure('low',  background='#7B2020', foreground='#FFD0D0')

vsb = ttk.Scrollbar(table_frame, orient=VERTICAL,   command=table.yview)
hsb = ttk.Scrollbar(table_frame, orient=HORIZONTAL, command=table.xview)
table.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

table.grid(row=0, column=0, sticky='nsew')
vsb.grid(row=0, column=1, sticky='ns')
hsb.grid(row=1, column=0, sticky='ew')
table_frame.grid_rowconfigure(0, weight=1)
table_frame.grid_columnconfigure(0, weight=1)

# Mouse-wheel scrolling
table.bind('<MouseWheel>', lambda e: table.yview_scroll(-1 * (e.delta // 120), 'units'))

# ============ Populate Table ============
THRESHOLD = 0.2 * 200

for i, row in enumerate(results):
    elec  = itemList_elec[i]  if i < len(itemList_elec)  else ''
    food  = itemList_food[i]  if i < len(itemList_food)  else ''
    house = itemList_house[i] if i < len(itemList_house) else ''

    qty1 = row[1] if row[1] else 0
    qty2 = row[4] if row[4] else 0
    qty3 = row[7] if row[7] else 0

    is_low = (qty1 and float(qty1) < THRESHOLD) or \
             (qty2 and float(qty2) < THRESHOLD) or \
             (qty3 and float(qty3) < THRESHOLD)

    if is_low:
        tag = 'low'
    elif i % 2 == 0:
        tag = 'even'
    else:
        tag = 'odd'

    table.insert("", "end",
                 values=(elec, qty2, row[5], food, qty1, row[2], house, qty3, row[8]),
                 tags=(tag,))

# ============ Status Bar ============
status_frame = Frame(root, bg='#0B2F3A', pady=4)
status_frame.pack(fill=X, side=BOTTOM)
low_count = sum(
    1 for row in results
    if (row[1] and float(row[1]) < THRESHOLD) or
       (row[4] and float(row[4]) < THRESHOLD) or
       (row[7] and float(row[7]) < THRESHOLD)
)
status_text = f"  {len(results)} items total   |   {low_count} below threshold (highlighted in red)"
Label(status_frame, text=status_text, bg='#0B2F3A',
      fg='#AAD4E8', font=(mainFont, 10)).pack(side=LEFT)

# ============ Low-Stock Alerts ============
cr.execute("SELECT Nutrition, quantity1, Electricity, quantity2, Inventory, quantity3 FROM Foods")
for i, (food_name, qty1, elec_name, qty2, house_name, qty3) in enumerate(cr.fetchall()):
    food_label  = itemList_food[i]  if i < len(itemList_food)  else food_name
    elec_label  = itemList_elec[i]  if i < len(itemList_elec)  else elec_name
    house_label = itemList_house[i] if i < len(itemList_house) else house_name

    if qty1 and float(qty1) < THRESHOLD:
        messagebox.showerror('Low Stock', f'Low stock: {food_label} ({qty1} remaining)')
        mailAlert(float(qty1), food_label, THRESHOLD)

    if qty2 and float(qty2) < THRESHOLD:
        messagebox.showerror('Low Stock', f'Low stock: {elec_label} ({qty2} remaining)')
        mailAlert(float(qty2), elec_label, THRESHOLD)

    if qty3 and float(qty3) < THRESHOLD:
        messagebox.showerror('Low Stock', f'Low stock: {house_label} ({qty3} remaining)')
        mailAlert(float(qty3), house_label, THRESHOLD)

root.mainloop()
