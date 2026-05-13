import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk
import random
import sqlite3
from datetime import datetime

# ============ Products — mutable lists so prices can be updated at runtime ============
PRODUCTS = [
    ['البقوليات', [
        ['الرز',         'Rice',           5],
        ['البرغل',       'Borkhl',         10],
        ['قاسوليا',      'Fasolia',        15],
        ['عدس',          '3ds',            2],
        ['معكرونة',      'Maqarona',       4],
        ['فريكة',        'Feryq',          5],
        ['حمص',          'Homs',           18],
        ['فول',          'Beans',          4],
        ['طعمية',        'Ta3meya',        4],
        ['بذنجان',       'Bazengan',       10],
        ['بطاطس',        'Potatoes',       5],
        ['ترمس حلو',     'Termas Helw',    15],
        ['بسلة',         'Besla',          4],
        ['قلقاس',        'Qolqas',         8],
        ['بميا',         'Bamya',          3],
        ['الترمس',       'Termas',         5],
        ['اللوبيا',      'Lobya',          5],
        ['البازلاء',     'Besala',         4],
        ['عدس احمر',     '3ds Ah7mar',     10],
        ['عدس اخضر',     '3ds A5der',      12],
        ['الادمامي',     'Admamy',         5],
    ]],
    ['اللوازم المنزلية', [
        ['مصفاة',        'Masfa',          20],
        ['صحن',          'Sahn',           20],
        ['كأس',          'Kas',            5],
        ['سكين',         'Knife',          10],
        ['شوك',          'Fork',           5],
        ['طنجرة',        'Tangara',        20],
        ['ملعقة',        'Spoon',          10],
        ['شاحن',         'Shahn',          40],
        ['سلة',          'Basket',         15],
        ['صينية',        'Sanya',          50],
        ['وعاء الخلط',   'W3a 5alt',       15],
        ['فتاحة العلب',  'Bottle Opener',  10],
        ['مقشرة',        'Makshra',        25],
        ['محفظة',        'Mahfza',         20],
        ['اكياس',        'Akyas',          10],
        ['سلة قمامة',    'Garbage Basket', 20],
        ['اكواب',        'Cups',           15],
        ['علب',          '3lba',           20],
        ['لوحة التقطيع', 'Cutting Plate',  10],
        ['حفارة',        'Hfaar',          30],
        ['كبشة',         'Kabsha',         25],
    ]],
    ['أدوات كهربائية', [
        ['تلفزيون',          'T.V.',            10000],
        ['غسالة',            'Washer',          15000],
        ['ثلاجة',            'Fridge',          20000],
        ['مكرويف',           'Microwave',       1000],
        ['خلاط',             'Blender',         1000],
        ['مقلاة كهربائية',   'Electric Pan',    2000],
        ['راديو',            'Radio',           500],
        ['بلاي ستيشن',       'Playstation',     15000],
        ['فلتر ماء',         'Water Filter',    3000],
        ['مكواة',            'Iron',            1000],
        ['مبرد',             'Cooler',          1000],
        ['مروحة ارضية',      'Floor Fan',       400],
        ['تكييف',            'Air Conditioner', 10000],
        ['فرن غاز',          'Gas Oven',        1000],
        ['مكنسة',            'Vacuum',          500],
        ['سخان',             'Heater',          3000],
        ['مشترك كهربائي',    'Power Strip',     500],
        ['شاشة كمبيوتر',     'Monitor',         5000],
        ['مروحة سقف',        'Ceiling Fan',     200],
    ]],
]

# ============ Database ============
db = sqlite3.connect("Super.db")
cr = db.cursor()
cr.execute("""CREATE TABLE IF NOT EXISTS Customer(
    customer_name TEXT, customer_phone TEXT, customer_bill TEXT, customer_address TEXT)""")
cr.execute("""CREATE TABLE IF NOT EXISTS Sales(
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    bill_number   TEXT,
    customer_name TEXT,
    customer_phone TEXT,
    total_amount  REAL,
    sale_date     TEXT)""")
# Prices table — owner can edit prices via the UI; defaults seeded from PRODUCTS above
cr.execute("""CREATE TABLE IF NOT EXISTS Prices (
    cat_idx  INTEGER NOT NULL,
    item_idx INTEGER NOT NULL,
    ar_name  TEXT,
    en_name  TEXT,
    price    REAL NOT NULL,
    PRIMARY KEY (cat_idx, item_idx))""")
cr.execute("SELECT COUNT(*) FROM Prices")
if cr.fetchone()[0] == 0:
    for ci, (_, items) in enumerate(PRODUCTS):
        for ii, item in enumerate(items):
            cr.execute("INSERT INTO Prices VALUES(?,?,?,?,?)", (ci, ii, item[0], item[1], item[2]))
    db.commit()

# Override PRODUCTS prices with whatever the owner last saved
cr.execute("SELECT cat_idx, item_idx, price FROM Prices ORDER BY cat_idx, item_idx")
for ci, ii, p in cr.fetchall():
    if ci < len(PRODUCTS) and ii < len(PRODUCTS[ci][1]):
        PRODUCTS[ci][1][ii][2] = p

# ============ Theme ============
mainFont  = 'tajawal'
mainColor = '#0B2F3A'
frameBg   = '#0B4C5F'
BTN_COLOR = '#DBA901'
BTN_HOVER = '#F0C030'
CAT_COLORS = ['#5DBB63', '#64B5F6', '#FFB74D']

# ============ Root Window ============
root = Tk()
root.geometry('1500x820+30+10')
root.title('Supermarket')
root.resizable(False, False)
Label(root, text='ادارة المشتريات', fg='white', bg=mainColor, font=('tajawal', 15)).pack(fill=X)

# ============ State Variables ============
quantities      = [[IntVar() for _ in items] for _, items in PRODUCTS]
total_vars      = [StringVar(value='$0') for _ in PRODUCTS]
grand_total_var = StringVar(value='$0')
customername    = StringVar()
customerphone   = StringVar()
customerfatora  = StringVar(value=str(random.randint(1000, 9999)))
customeraddress = StringVar()
customermail    = StringVar()

# ============ Calculation ============
def category_total(idx):
    items = PRODUCTS[idx][1]
    try:
        return sum(quantities[idx][i].get() * items[i][2] for i in range(len(items)))
    except TclError:
        return 0

def update_live_total(*_):
    try:
        totals = [category_total(i) for i in range(len(PRODUCTS))]
        for i, v in enumerate(total_vars):
            v.set(f'${totals[i]:,}')
        grand = sum(totals)
        grand_total_var.set(f'${grand:,}')
        root.title(f'Supermarket  ·  ${grand:,}')
    except Exception:
        pass

for cat_vars in quantities:
    for v in cat_vars:
        v.trace_add('write', update_live_total)

# ============ Helpers ============
def styled_btn(parent, bg=None, **kw):
    bg = bg or BTN_COLOR
    kw.setdefault('borderwidth', 0)
    kw.setdefault('font', mainFont)
    kw.setdefault('cursor', 'hand2')
    kw.setdefault('relief', 'flat')
    btn = Button(parent, bg=bg, **kw)
    hover = BTN_HOVER if bg == BTN_COLOR else '#DDDDDD'
    btn.bind('<Enter>', lambda e: btn.config(bg=hover))
    btn.bind('<Leave>', lambda e: btn.config(bg=bg))
    return btn

def cust_row(frame, row, label_text, var, disabled=False):
    """Add a label+entry pair to the customer grid frame."""
    Label(frame, text=label_text, font=('tajawal', 10),
          bg='#0B4C5F', fg='#AAD4E8').grid(
        row=row, column=1, padx=(4, 10), pady=4, sticky='e')
    kw = dict(textvariable=var, justify='center', relief='flat',
              highlightthickness=1, highlightbackground='#1A6080')
    if disabled:
        kw['state'] = DISABLED
        kw['disabledbackground'] = '#E8E8E8'
    ent = Entry(frame, **kw)
    ent.grid(row=row, column=0, padx=(10, 4), pady=4, sticky='ew')
    return ent

# ============ Bill Display ============
def welcome():
    textarea.config(state=NORMAL)
    textarea.delete('1.0', END)
    textarea.insert(END, "  ★  Supermarket  ★\n",              'store')
    textarea.insert(END, "══════════════════════════\n",        'div')
    textarea.insert(END, f"  Bill #  {customerfatora.get()}\n", 'meta')
    textarea.insert(END, f"  {customername.get() or '—'}\n",    'meta')
    textarea.insert(END, f"  {customerphone.get() or '—'}\n",   'meta')
    textarea.insert(END, f"  {customeraddress.get() or '—'}\n", 'meta')
    textarea.insert(END, f"  {customermail.get() or '—'}\n",    'meta')
    textarea.insert(END, "══════════════════════════\n",        'div')
    textarea.insert(END, "  Item            Qty  Price\n",      'col_hdr')
    textarea.insert(END, "──────────────────────────\n",        'div')

def bill(totals):
    for cat_idx, (cat_name, items) in enumerate(PRODUCTS):
        has_items = any(quantities[cat_idx][i].get() for i in range(len(items)))
        if has_items:
            textarea.insert(END, f"  ▸ {cat_name}\n", 'cat_hdr')
        for i, (ar_name, en_name, price) in enumerate(items):
            qty = quantities[cat_idx][i].get()
            if qty:
                textarea.insert(END,
                    f"  {en_name:<16} {qty:<4} ${qty * price:,}\n", 'item')
    textarea.insert(END, "══════════════════════════\n",              'div')
    textarea.insert(END, f"  TOTAL:          ${sum(totals):,}\n",     'total')
    textarea.config(state=DISABLED)

def total():
    totals = [category_total(i) for i in range(len(PRODUCTS))]
    welcome()
    bill(totals)

# ============ Clear ============
def Clear():
    for cat_vars in quantities:
        for v in cat_vars:
            v.set(0)
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
    win.geometry('920x540')
    win.configure(bg=mainColor)
    Label(win, text='Sales History', font=('tajawal', 15, 'bold'),
          bg=mainColor, fg='gold').pack(pady=10)
    sf = Frame(win, bg='#0B4C5F', pady=8)
    sf.pack(fill=X, padx=15)
    today = datetime.now().strftime("%Y-%m-%d")
    cr.execute("SELECT COALESCE(SUM(total_amount), 0) FROM Sales WHERE sale_date LIKE ?", (f"{today}%",))
    today_total = cr.fetchone()[0]
    cr.execute("SELECT COALESCE(SUM(total_amount), 0), COUNT(*) FROM Sales")
    all_total, count = cr.fetchone()
    for text in [f"  Today: ${today_total:,.0f}", f"  All Time: ${all_total:,.0f}", f"  Total Bills: {count}  "]:
        Label(sf, text=text, bg='#0B4C5F', fg='white', font=('tajawal', 12)).pack(side=LEFT, padx=15)
    style = ttk.Style(win)
    style.theme_use('default')
    style.configure('Report.Treeview',
        background='#0D3A4A', foreground='white', fieldbackground='#0D3A4A',
        rowheight=26, font=(mainFont, 10))
    style.configure('Report.Treeview.Heading',
        background='#0B2F3A', foreground='gold', font=(mainFont, 11, 'bold'), relief='flat')
    style.map('Report.Treeview', background=[('selected', '#1A6B8A')])
    frame = Frame(win, bg=mainColor)
    frame.pack(fill=BOTH, expand=True, padx=15, pady=10)
    cols = ('Bill #', 'Customer', 'Phone', 'Total', 'Date')
    tree = ttk.Treeview(frame, columns=cols, show='headings', height=22, style='Report.Treeview')
    for col, w in zip(cols, (90, 180, 130, 100, 180)):
        tree.heading(col, text=col)
        tree.column(col, width=w, anchor='center')
    tree.tag_configure('even', background='#0B4C5F')
    tree.tag_configure('odd',  background='#0D3A4A')
    scroll = ttk.Scrollbar(frame, orient=VERTICAL, command=tree.yview)
    tree.configure(yscrollcommand=scroll.set)
    cr.execute("SELECT bill_number, customer_name, customer_phone, total_amount, sale_date FROM Sales ORDER BY sale_date DESC")
    for idx, row in enumerate(cr.fetchall()):
        tree.insert('', END,
            values=(row[0], row[1] or '—', row[2] or '—', f'${row[3]:,.0f}', row[4]),
            tags=('even' if idx % 2 == 0 else 'odd',))
    tree.pack(side=LEFT, fill=BOTH, expand=True)
    scroll.pack(side=RIGHT, fill=Y)

# ============ Price Editor ============
def show_price_editor():
    win = Toplevel(root)
    win.title('Price Editor — تعديل الأسعار')
    win.geometry('660x580')
    win.configure(bg=mainColor)
    win.resizable(False, True)

    Label(win, text='Edit Item Prices  —  تعديل الأسعار',
          font=(mainFont, 14, 'bold'), bg=mainColor, fg='gold').pack(pady=8)
    Label(win, text='Change any price then click Save. Prices are stored in the database.',
          font=(mainFont, 9), bg=mainColor, fg='#AAD4E8').pack()

    # Scrollable inner frame
    outer = Frame(win, bg=mainColor)
    outer.pack(fill=BOTH, expand=True, padx=10, pady=6)

    canvas = Canvas(outer, bg=mainColor, highlightthickness=0)
    vsb    = Scrollbar(outer, orient=VERTICAL, command=canvas.yview)
    canvas.configure(yscrollcommand=vsb.set)
    vsb.pack(side=RIGHT, fill=Y)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)

    inner   = Frame(canvas, bg=mainColor)
    win_id  = canvas.create_window((0, 0), window=inner, anchor='nw')
    inner.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))
    canvas.bind('<Configure>', lambda e: canvas.itemconfig(win_id, width=e.width))
    canvas.bind('<MouseWheel>', lambda e: canvas.yview_scroll(-1 * (e.delta // 120), 'units'))

    inner.grid_columnconfigure(0, minsize=170)
    inner.grid_columnconfigure(1, minsize=160)
    inner.grid_columnconfigure(2, minsize=100)

    price_vars  = []
    current_row = 0

    for ci, (cat_name, items) in enumerate(PRODUCTS):
        Label(inner, text=cat_name, font=(mainFont, 12, 'bold'),
              bg=mainColor, fg=CAT_COLORS[ci]).grid(
            row=current_row, column=0, columnspan=3, pady=(14, 2), padx=10, sticky='w')
        current_row += 1
        for hdr, col in [('الاسم', 0), ('Name (EN)', 1), ('Price  ($)', 2)]:
            Label(inner, text=hdr, font=(mainFont, 9, 'bold'),
                  bg=mainColor, fg='#888').grid(row=current_row, column=col, padx=10, sticky='w')
        current_row += 1

        for ii, item in enumerate(items):
            ar_name, en_name, price = item[0], item[1], item[2]
            row_bg = '#0B4C5F' if ii % 2 == 0 else '#0D3A4A'
            Label(inner, text=ar_name, font=(mainFont, 10),
                  bg=row_bg, fg='white').grid(
                row=current_row, column=0, padx=10, pady=1, sticky='ew')
            Label(inner, text=en_name, font=(mainFont, 10),
                  bg=row_bg, fg='#CCCCCC').grid(
                row=current_row, column=1, padx=10, pady=1, sticky='ew')
            pvar = StringVar(value=str(int(price) if price == int(price) else price))
            Entry(inner, textvariable=pvar, width=10, justify='center',
                  font=(mainFont, 10), relief='flat',
                  highlightthickness=1, highlightbackground='#1A6080').grid(
                row=current_row, column=2, padx=10, pady=1, sticky='ew')
            price_vars.append((ci, ii, pvar))
            current_row += 1

    def save_prices():
        skipped = []
        for ci, ii, pvar in price_vars:
            try:
                val = float(pvar.get())
                if val < 0:
                    raise ValueError
                PRODUCTS[ci][1][ii][2] = val
                cr.execute("UPDATE Prices SET price=? WHERE cat_idx=? AND item_idx=?",
                           (val, ci, ii))
            except (ValueError, TclError):
                skipped.append(PRODUCTS[ci][1][ii][1])
        db.commit()
        update_live_total()
        if skipped:
            messagebox.showwarning('Warning',
                f"Invalid values skipped (must be a positive number):\n{', '.join(skipped)}",
                parent=win)
        else:
            messagebox.showinfo('Saved', 'All prices updated!', parent=win)
            win.destroy()

    styled_btn(win, text='  Save All Prices  ', font=(mainFont, 11, 'bold'),
               command=save_prices).pack(pady=10)

# ============ Customer Database Viewer ============
def show_customer_db():
    win = Toplevel(root)
    win.title('Customer Database — قاعدة بيانات العملاء')
    win.geometry('900x560')
    win.configure(bg=mainColor)
    win.resizable(True, True)

    Label(win, text='Customer Database  —  قاعدة بيانات العملاء',
          font=(mainFont, 14, 'bold'), bg=mainColor, fg='gold').pack(pady=(10, 4))

    # Search bar
    bar = Frame(win, bg='#0B4C5F', pady=6)
    bar.pack(fill=X, padx=15, pady=(0, 6))
    Label(bar, text='بحث / Search:', bg='#0B4C5F', fg='#AAD4E8',
          font=(mainFont, 11)).pack(side=RIGHT, padx=(10, 6))
    search_var = StringVar()
    Entry(bar, textvariable=search_var, font=(mainFont, 11), width=28, relief='flat',
          highlightthickness=1, highlightbackground='#1A6080').pack(side=RIGHT, padx=4)

    # Treeview
    tv_style = ttk.Style(win)
    tv_style.theme_use('default')
    tv_style.configure('Cust.Treeview',
        background='#0D3A4A', foreground='white', fieldbackground='#0D3A4A',
        rowheight=28, font=(mainFont, 10))
    tv_style.configure('Cust.Treeview.Heading',
        background='#0B2F3A', foreground='#DBA901',
        font=(mainFont, 11, 'bold'), relief='flat')
    tv_style.map('Cust.Treeview', background=[('selected', '#1A6B8A')])

    table_frame = Frame(win, bg=mainColor)
    table_frame.pack(fill=BOTH, expand=True, padx=15)

    cols = ('الاسم', 'رقم الهاتف', 'رقم الفاتورة', 'العنوان')
    tree = ttk.Treeview(table_frame, columns=cols, show='headings',
                        height=18, style='Cust.Treeview')
    sort_rev = {}
    for col, w in zip(cols, (200, 150, 110, 300)):
        tree.heading(col, text=col, command=lambda c=col: sort_col(c))
        tree.column(col, width=w, anchor='center')
    tree.tag_configure('even', background='#0B4C5F')
    tree.tag_configure('odd',  background='#0D3A4A')

    vsb = ttk.Scrollbar(table_frame, orient=VERTICAL,   command=tree.yview)
    hsb = ttk.Scrollbar(table_frame, orient=HORIZONTAL, command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(row=0, column=0, sticky='nsew')
    vsb.grid(row=0, column=1, sticky='ns')
    hsb.grid(row=1, column=0, sticky='ew')
    table_frame.grid_rowconfigure(0, weight=1)
    table_frame.grid_columnconfigure(0, weight=1)
    tree.bind('<MouseWheel>', lambda e: tree.yview_scroll(-1 * (e.delta // 120), 'units'))

    def load_data(filter_text=''):
        for row in tree.get_children():
            tree.delete(row)
        if filter_text:
            cr.execute(
                "SELECT customer_name, customer_phone, customer_bill, customer_address "
                "FROM Customer WHERE customer_name LIKE ? OR customer_phone LIKE ? OR customer_bill LIKE ?",
                (f'%{filter_text}%', f'%{filter_text}%', f'%{filter_text}%'))
        else:
            cr.execute(
                "SELECT customer_name, customer_phone, customer_bill, customer_address FROM Customer")
        for idx, row in enumerate(cr.fetchall()):
            tree.insert('', END,
                values=(row[0] or '—', row[1] or '—', row[2] or '—', row[3] or '—'),
                tags=('even' if idx % 2 == 0 else 'odd',))
        count_lbl.config(text=f'  {len(tree.get_children())} record(s)')

    def sort_col(col):
        data = [(tree.set(k, col), k) for k in tree.get_children('')]
        rev = sort_rev.get(col, False)
        data.sort(key=lambda x: x[0], reverse=rev)
        sort_rev[col] = not rev
        for idx, (_, k) in enumerate(data):
            tree.move(k, '', idx)
            tree.item(k, tags=('even' if idx % 2 == 0 else 'odd',))

    search_var.trace_add('write', lambda *_: load_data(search_var.get().strip()))

    def delete_selected():
        sel = tree.selection()
        if not sel:
            return
        vals = tree.item(sel[0])['values']
        if messagebox.askyesno('حذف / Delete',
                               f'Delete customer record?\n{vals[0]}  —  Bill #{vals[2]}',
                               parent=win):
            cr.execute("DELETE FROM Customer WHERE customer_name=? AND customer_bill=?",
                       (vals[0], vals[2]))
            db.commit()
            load_data(search_var.get().strip())

    # Bottom bar
    bot = Frame(win, bg=mainColor, pady=6)
    bot.pack(fill=X, padx=15)
    count_lbl = Label(bot, text='', bg=mainColor, fg='#AAD4E8', font=(mainFont, 10))
    count_lbl.pack(side=LEFT)
    styled_btn(bot, text='حذف المحدد / Delete', command=delete_selected,
               bg='#8B2020', font=(mainFont, 10)).pack(side=RIGHT, padx=4)
    styled_btn(bot, text='تحديث / Refresh',
               command=lambda: load_data(search_var.get().strip()),
               font=(mainFont, 10)).pack(side=RIGHT, padx=4)

    load_data()


# ============ UI: Customer Frame — grid layout ============
F1 = Frame(root, bd=0, width=416, height=235, bg='#0B4C5F')
F1.place(x=1082, y=35)
F1.grid_propagate(False)
F1.grid_columnconfigure(0, weight=1)    # entry side (left)
F1.grid_columnconfigure(1, minsize=185) # label side (right) — wide enough for البريد الالكتروني

Label(F1, text='بيانات المشتري', font=('tajawal', 13, 'bold'),
      bg='#0B4C5F', fg='tomato').grid(row=0, column=0, columnspan=2, pady=(6, 4))

EntName      = cust_row(F1, 1, 'الاسم',              customername)
EntPhone     = cust_row(F1, 2, 'رقم الهاتف',         customerphone)
EntFatora    = cust_row(F1, 3, 'رقم الفاتورة',       customerfatora, disabled=True)
Entmail      = cust_row(F1, 4, 'البريد الالكتروني',  customermail)
addressValue = cust_row(F1, 5, 'العنوان',            customeraddress)

btn_row = Frame(F1, bg='#0B4C5F')
btn_row.grid(row=6, column=0, columnspan=2, pady=(6, 4))
styled_btn(btn_row, text='بحث',   font=('tajawal', 11), width=9,
           command=Database_Search, bg='white').pack(side=LEFT, padx=8)
styled_btn(btn_row, text='اضافة', font=('tajawal', 11), width=9,
           command=Database_Add,    bg='white').pack(side=LEFT, padx=8)

# ============ UI: Bill Header + Frame ============
bill_hdr = Frame(root, width=416, height=26, bg='#072030')
bill_hdr.place(x=1082, y=272)
Label(bill_hdr, text='  الفاتورة  ·  Receipt',
      font=('tajawal', 10, 'bold'), bg='#072030', fg='#DBA901').place(x=8, y=3)

F3 = Frame(root, bd=0, bg='#F7F5EE', width=416, height=384)
F3.place(x=1082, y=300)
scroll_y = Scrollbar(F3, orient=VERTICAL)
textarea = Text(F3, bg='#F7F5EE', fg='#1A1A1A', width=40, height=24,
                font=('Courier', 11), yscrollcommand=scroll_y.set,
                padx=6, pady=6, wrap=NONE)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_y.config(command=textarea.yview)
textarea.pack(fill=BOTH, expand=True)
textarea.config(state=DISABLED)

# Bill text tags for visual hierarchy
textarea.tag_configure('store',   font=('Courier', 11, 'bold'), foreground='#0B2F3A', justify='center')
textarea.tag_configure('div',     foreground='#AAAAAA')
textarea.tag_configure('meta',    font=('Courier', 9),          foreground='#444444')
textarea.tag_configure('col_hdr', font=('Courier', 9, 'bold'),  foreground='#555555')
textarea.tag_configure('cat_hdr', font=('Courier', 9, 'bold'),  foreground='#888888')
textarea.tag_configure('item',    font=('Courier', 10),         foreground='#111111')
textarea.tag_configure('total',   font=('Courier', 11, 'bold'), foreground='#0B2F3A')

# ============ UI: Controls Frame (full-width bottom strip) ============
F4 = Frame(root, bd=0, width=1500, height=130, bg='#0B4C5F')
F4.place(x=0, y=688)

# ── Totals sub-frame: grid-managed so labels never bleed into buttons ──
tot = Frame(F4, bg=frameBg, width=330, height=128)
tot.place(x=1, y=1)
tot.grid_propagate(False)
tot.grid_columnconfigure(0, weight=1)      # entry (grows)
tot.grid_columnconfigure(1, minsize=148)   # label (fixed, fits longest Arabic text)

_tot_rows = [
    ('البقوليات',    total_vars[0],   'white', '#0D3A4A', CAT_COLORS[0], False),
    ('المنزليات',    total_vars[1],   'white', '#0D3A4A', CAT_COLORS[1], False),
    ('الكهربائيات',  total_vars[2],   'white', '#0D3A4A', CAT_COLORS[2], False),
    ('الإجمالي الكلي', grand_total_var, 'gold', '#0B2F3A', 'gold',       True),
]
for _i, (_lbl, _var, _fg, _ebg, _lclr, _bold) in enumerate(_tot_rows):
    Label(tot, text=_lbl, font=(mainFont, 10, 'bold'),
          bg=frameBg, fg=_lclr).grid(
        row=_i, column=1, sticky='e', padx=(4, 10), pady=3)
    Entry(tot, textvariable=_var, width=11, state=DISABLED,
          disabledforeground=_fg, disabledbackground=_ebg,
          font=(mainFont, 10, 'bold') if _bold else (mainFont, 10)).grid(
        row=_i, column=0, sticky='ew', padx=(8, 4), pady=3)

# ── Buttons: 3 columns × 3 rows, safely right of the totals sub-frame ──
# Column A (x=345)
styled_btn(F4, text='افراغ الحقول',     width=14, command=Clear).place(            x=345, y=8)
styled_btn(F4, text='تقرير المبيعات',   width=14, command=show_report).place(      x=345, y=50)
styled_btn(F4, text='اغلاق البرنامج',   width=14, command=root.quit,
           bg='#8B2020').place(                                                     x=345, y=92)
# Column B (x=510)
styled_btn(F4, text='تعديل الأسعار',    width=14, command=show_price_editor).place(x=510, y=8)
styled_btn(F4, text='عرض العملاء',      width=14, command=show_customer_db).place( x=510, y=50)
# Column C (x=675)
styled_btn(F4, text='الحساب',           width=14, command=total).place(            x=675, y=8)
styled_btn(F4, text='تصدير الفاتورة',   width=14, command=Print).place(            x=675, y=50)
styled_btn(F4, text='فاتورة الكترونية', width=14, command=Send).place(             x=675, y=92)

# ============ UI: Product Frames — grid layout (no fixed pixel overlaps) ============
FRAME_CONFIGS = [(1, 318, 650), (321, 318, 650), (641, 338, 600)]
for cat_idx, (cat_name, items) in enumerate(PRODUCTS):
    x, w, h = FRAME_CONFIGS[cat_idx]
    frame = Frame(root, bd=0, width=w, height=h, bg=frameBg)
    frame.place(x=x, y=35)
    frame.grid_propagate(False)

    frame.grid_columnconfigure(0, minsize=62)
    frame.grid_columnconfigure(1, minsize=68)
    frame.grid_columnconfigure(2, weight=1)

    Frame(frame, bg=CAT_COLORS[cat_idx], height=3).grid(
        row=0, column=0, columnspan=3, sticky='ew')
    Label(frame, text=cat_name, font=(mainFont, 14, 'bold'),
          bg=frameBg, fg=CAT_COLORS[cat_idx]).grid(
        row=1, column=0, columnspan=3, pady=(5, 6))

    for i, (ar_name, _, price) in enumerate(items):
        Entry(frame, textvariable=quantities[cat_idx][i], width=6,
              justify='center', font=(mainFont, 10)).grid(
            row=i + 2, column=0, padx=(6, 2), pady=2, sticky='ew')
        Label(frame, text=f'${price:,}', font=(mainFont, 8, 'italic'),
              bg=frameBg, fg='#8FC4D8').grid(
            row=i + 2, column=1, sticky='w')
        Label(frame, text=ar_name, font=(mainFont, 11),
              bg=frameBg, fg='white').grid(
            row=i + 2, column=2, padx=(2, 8), sticky='w')

root.mainloop()
