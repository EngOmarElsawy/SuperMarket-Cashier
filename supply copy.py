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
root.resizable(False,False)
root.iconbitmap('D:/Omar/Codezilla/Images/iice.ico')
title = Label(  root,text='ادارة المخزون',fg='white',bg=mainColor, font=('tajawal',15))
title.pack(fill=X)
# root.iconbitmap('../Downloads/311804053_3448602958752567_1147801703367297556_n')

# Create the root window


# Create the table
table = ttk.Treeview(root, columns=('col1', 'col2', 'col3', 'col4', 'col5', 'col6'), show='headings',height=40)


# Add 19 rows to every column
itemList2 = ['الرز', 'البرغل', 'قاسوليا', 'عدس', 'معكرونة', 'فريكة', 'حمص', 'فول', 'طعمية', 'بذنجان', 'بطاطس', 'ترمس حلو', 'بسلة', 'قلقاس', 'بميا', 'الترمس', 'اللوبيا', 'البازلاء', 'عدس احمر', 'عدس اخضر', 'الادمامي']
itemsList1 = ['تلفزيون', 'غسالة', 'ثلاجة', 'مكرويف', 'خلاط', 'مقلاة كهربائية', 'راديو', 'بلاي ستيشن', 'فلتر ماء', 'مكواة', 'مبرد', 'مروحة ارضية', 'تكييف', 'فرن غاز', 'مكنسة', 'سخان', 'مشترك كهربائي', 'شاشة كمبيوتر', 'مروحة سقف']
itemList3 = ['مصفاة', 'صحن', 'كأس', 'سكين', 'شوك', 'طنجرة', 'ملعقة', 'شاحن', 'سلة', 'صينية', 'وعاء الخلط', 'فتاحة العلب', 'مقشرة', 'محفظة', 'اكياس', 'سلة قمامة', 'اكواب', 'علب', 'لوحة التقطيع', 'حفارة', 'كبشة']

for i in range(len(itemsList1)):
    table.insert("", "end", values=('\t'))
    table.insert("", "end", values=(itemsList1[i],i+1,itemList2[i],i+1,itemList3[i],i+1))
for i in range(6):    
    table.column(f'col{i+1}',anchor='e',)
    table.tag_configure(f'col{i+1}',background='gray',foreground='white')
    table.column(f'col{i+1}', width=200, stretch=False,anchor='center')
    # table.tag_configure(f'col{i+1}',)

table.heading('col1', text='الادوات الكهربائية',anchor='e')
table.heading('col2', text='الكمية',anchor='e')
table.heading('col3', text='اللوازم المنزلية',anchor='e')
table.heading('col4', text='الكمية',anchor='e')
table.heading('col5', text='اللوازم المنزلية',anchor='e')
table.heading('col6', text='الكمية',anchor="e")
table.pack(pady=25)

# # Create the text area
# text_area = tk.Text(root, height=3, font=('tajawal',18))
# text_area.pack()

# # Create the "Add Item" button
# add_item_button = tk.Button(root,bg=mainColor ,text="Add Item", command=add_item)
# add_item_button.pack(pady=10)


root.mainloop()