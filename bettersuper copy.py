import tkinter as tk
from tkinter import *
from tkinter import messagebox
import math, os, random
import tempfile
import io
from datetime import datetime
import sqlite3

db = sqlite3.connect("Super.db")
try:
    cr = db.cursor()
    cr.execute("CREATE TABLE if not exists Customer(customer_name TEXT, customer_phone INTGER, customer_bill INTGER, customer_address TEXT)")
    cr.execute("select * from Customer")
    cr.execute("select customer_name from Customer")
    cr.execute("select customer_phone from Customer")
    cr.execute("select customer_bill from Customer")
except sqlite3.Error:
    print("Error Reading Data")
# ============ Fonts and Colors =============
mainFont = 'tajawal'
mainColor = '#0B2F3A' 
frameBg = '#0B4C5F'

root = Tk()
root = root
root.geometry('1000x800+30+10')
root.title('Supermarket')
root.resizable(False,False)
root.iconbitmap('D:/Omar/Codezilla/Images/iice.ico')
title = Label(  root,text='ادارة المشتاريات',fg='white',bg=mainColor, font=('tajawal',15))
title.pack(fill=X)
root.iconbitmap('../Downloads/311804053_3448602958752567_1147801703367297556_n.jpg')


#====================================================
ricePrice = 5
bor8lPrice = 10
fasoliaPrice = 15
adsPrice = 2
makronaPrice = 4
freekPrice = 5
homsPrice = 18
foolPrice = 4
ta3myaPrice = 4
bznganPrice = 10
potatoesPrice = 5
termasPricehelw = 15
beslaPrice = 4
qolqasPrice = 8
bamyaPrice = 3
LobyaPrice = 5
TermasPrice = 5
basalaPrice = 4
adsa7marPrice = 10
ads5derPrice = 12
admamyPrice = 5
#== Lwazem Prices
masfaPrice = 20
platePrice = 20
cupPrice = 5
knifePrice = 10
forkPrice = 5
tangaraPrice = 20
spoonPrice = 10
chargerPrice = 40
basketPrice = 15
sanyaPrice = 50
w3aa5aletPrice = 15
bottleOpenerPrice = 10
maqsharaPrice = 25
m7fzaPrice = 20
akyasPrice = 10
garbigbasketPrice = 20
cupsPrice = 15
containerPrice = 20
lo7ttqte3Price = 10
hafaraPrice = 30
kabshaPrice = 25
# === Kharba Prices ======
tvPrice = 10000
washerPrice = 15000
fridgePrice = 20000
microwavePrice = 1000
khalatPrice = 1000
mqlaPrice = 2000
radioPrice = 500
playstationPrice = 15000
waterfilter = 3000
ironPrice = 1000
coolerPrice = 1000
marwhaPriceard = 400
conditionerPrice = 10000
fornPrice = 1000
maqnasaPrice = 500
s5aanPrice = 3000
moshtrakPrice = 500
monitor = 5000
marwhaPrice = 200




total_boqliat = IntVar() 
tax_cos = IntVar()
total_lwazem = IntVar()
total_khraba = IntVar()
grandTotal = IntVar()
# ========================= Boqliat q1 to q21 =================


q1 = IntVar()
q2 = IntVar()
q3 = IntVar()
q4 = IntVar()
q5 = IntVar()
q6 = IntVar()
q7 = IntVar()
q8 = IntVar()
q9 = IntVar()
q10 = IntVar()
q11 = IntVar()
q12 = IntVar()
q13 = IntVar()
q14 = IntVar()
q15 = IntVar()
q16 = IntVar()
q17 = IntVar()
q18 = IntVar()
q19 = IntVar()
q20 = IntVar()
q21 = IntVar()
#==============lwazm qq1 to qq21 ==============
qq1 = IntVar()
qq2 = IntVar()
qq3 = IntVar()
qq4 = IntVar()
qq5 = IntVar()
qq6 = IntVar()
qq7 = IntVar()
qq8 = IntVar()
qq9 = IntVar()
qq10 = IntVar()
qq11 = IntVar()
qq12 = IntVar()
qq13 = IntVar()
qq14 = IntVar()
qq15 = IntVar()
qq16 = IntVar()
qq17 = IntVar()
qq18 = IntVar()
qq19 = IntVar()
qq20 = IntVar()
qq21 = IntVar()
#============== Kharba qqq1 to qqq21 ==============
qqq1 = IntVar()
qqq2 = IntVar()
qqq3 = IntVar()
qqq4 = IntVar()
qqq5 = IntVar()
qqq6 = IntVar()
qqq7 = IntVar()
qqq8 = IntVar()
qqq9 = IntVar()
qqq10 = IntVar()
qqq11 = IntVar()
qqq12 = IntVar()
qqq13 = IntVar()
qqq14 = IntVar()
qqq15 = IntVar()
qqq16 = IntVar()
qqq17 = IntVar()
qqq18 = IntVar()
qqq19 = IntVar()
qqq20 = IntVar()
qqq21 = IntVar()

total_boqliat.set('$'+str(0))
total_lwazem.set('$'+str(0))
total_khraba.set('$'+str(0))
# =========================== Fuctions ================================
#================ Total functions ====================
def total():
    # welcome()
    bill()
#===================boqliat ===============
    total_boqliat_prices = (
    ( q1.get() *ricePrice) +
    ( q2.get() *bor8lPrice) +
    ( q3.get() *fasoliaPrice) +
    ( q4.get() *adsPrice) +
    ( q5.get() *makronaPrice) +
    ( q6.get() *freekPrice) +
    ( q7.get() *homsPrice) +
    ( q8.get() *foolPrice) +
    ( q9.get() *ta3myaPrice) +
    ( q10.get() *bznganPrice) +
    ( q11.get() *potatoesPrice) +
    ( q12.get() *termasPricehelw) +
    ( q13.get() *basalaPrice) +
    ( q14.get() *qolqasPrice) +
    ( q15.get() *bamyaPrice) +
    ( q16.get() *TermasPrice) +
    ( q17.get() *LobyaPrice) +
    ( q18.get() *basalaPrice) +
    ( q19.get() *adsa7marPrice) +
    ( q20.get() *ads5derPrice) +
    ( q21.get() *admamyPrice) 
)

    total_boqliat.set("$"+str( total_boqliat_prices))
    tax_cos.set("$"+str(round( total_boqliat_prices*0.05)))
#======================== Lwazem ==================
    global total_lwazem_prices
    total_lwazem_prices = (
    ( qq1.get() *masfaPrice) +
    ( qq2.get() *platePrice) +
    ( qq3.get() *cupPrice) +
    ( qq4.get() *knifePrice) +
    ( qq5.get() *forkPrice) +
    ( qq6.get() *tangaraPrice) +
    ( qq7.get() *spoonPrice) +
    ( qq8.get() *chargerPrice) +
    ( qq9.get() *basketPrice) +
    ( qq10.get() *sanyaPrice) +
    ( qq11.get() *w3aa5aletPrice) +
    ( qq12.get() *bottleOpenerPrice) +
    ( qq13.get() *maqsharaPrice) +
    ( qq14.get() *m7fzaPrice) +
    ( qq15.get() *akyasPrice) +
    ( qq16.get() *garbigbasketPrice) +
    ( qq17.get() *cupsPrice) +
    ( qq18.get() *containerPrice) +
    ( qq19.get() *lo7ttqte3Price) +
    ( qq20.get() *hafaraPrice) +
    ( qq21.get() *kabshaPrice) 
)
    total_lwazem.set("$"+str( total_lwazem_prices))
    tax_cos.set("$"+str(round( total_lwazem_prices*0.05)))
#=====================Kharaba==========================
    global total_khraba_prices
    total_khraba_prices = (
    ( qqq1.get() *tvPrice) +
    ( qqq2.get() *washerPrice) +
    ( qqq3.get() *fridgePrice) +
    ( qqq4.get() *microwavePrice) +
    ( qqq5.get() *khalatPrice) +
    ( qqq6.get() *mqlaPrice) +
    ( qqq7.get() *radioPrice) +
    ( qqq8.get() *playstationPrice) +
    ( qqq9.get() *waterfilter) +
    ( qqq10.get() *ironPrice) +
    ( qqq11.get() *coolerPrice) +
    ( qqq12.get() *marwhaPriceard) +
    ( qqq13.get() *conditionerPrice) +
    ( qqq14.get() *fornPrice) +
    ( qqq15.get() *maqnasaPrice) +
    ( qqq16.get() *s5aanPrice) +
    ( qqq17.get() *moshtrakPrice) +
    ( qqq18.get() *monitor) +
    ( qqq19.get() *marwhaPrice)
)
    total_khraba.set("$"+str( total_khraba_prices))
    tax_cos.set("$"+str(round( total_khraba_prices*0.05)))
#======= Customer Data =============
customername = StringVar()
customerphone = StringVar()
customerfatora = StringVar()
customeraddress = StringVar()
customermail = StringVar()

x = random.randint(1000,9999)
customerfatora.set(str(x))
#======= متغيرات الحساب الكلي =========
bacoliat = total_boqliat
adoat = total_lwazem
kahraba = total_khraba
totalall = grandTotal
#================================ Data Base Functions ================================
# def Database_Add():
#     textarea.config(state=NORMAL)
#     try:
#         EntFatora.config(state=NORMAL)
#         cr.execute(f"insert into Customer(customer_name,customer_phone,customer_bill,customer_address) values('{EntName.get()}','{EntPhone.get()}','{EntFatora.get()}','{addressValue.get()}')")
#         db.commit()
#         messagebox.showinfo('ADDED', 'Customer Info Added')
#         EntFatora.config(state=DISABLED)
#     except sqlite3.OperationalError:
#         print(sqlite3.OperationalError)
#     textarea.config(state=DISABLED)
# def Database_Search():
#     EntFatora.config(state=NORMAL)
#     cr.execute("select customer_name from Customer")
#     cr.execute("select customer_phone from Customer")
#     cr.execute("select customer_bill from Customer")
#     cr.execute(f"select * from Customer where customer_name = '{EntName.get()}' and customer_phone = ('{EntPhone.get()}')")
#     results = cr.fetchone()
#     print(results)
#     if results != None:
#         messagebox.showinfo('Found',f'{results}')
#     else:
#         messagebox.showerror("Not Found", "Customer Not Found")
#     EntFatora.config(state=DISABLED)
# # #======= Customer Data ========
# # F1 = Frame(root, bd=2, width=338, height=300, bg='#0B4C5F')
# # F1.place(x=990,y=35)
# # tit = Label(F1, text='بيانات المشتري', font=('tajawal',13,'bold'),bg='#0B4C5F',fg='tomato')
# # tit.place(x=120,y=-2)
# # hisName = Label(F1, text='الاسم ', font=('tajawal',10), bg='#0B4C5F',fg='white')
# # hisName.place(x=242,y=15)
# # hisPhone = Label(F1, text='رقم الهاتف ', font=('tajawal',10), bg='#0B4C5F',fg='white')
# # hisPhone.place(x=230,y=45)
# # billNum = Label(F1, text='رقم الفاتورة', font=('tajawal',10), bg='#0B4C5F',fg='white')
# # billNum.place(x=230,y=75)
# # email = Label(F1, text=' البريد الالكتروني', font=('tajawal',10), bg='#0B4C5F',fg='white')
# # email.place(x=220,y=100)
# # address = Label(F1,text='العنوان',font=('tajawal',10), bg='#0B4C5F',fg='white')
# # address.place(x=235,y=125)
# # addressValue = Entry(F1,textvariable=customeraddress,justify=CENTER)
# # addressValue.place(x=20,y=120)
# # EntName = Entry(F1,textvariable=customername,justify='center')
# # EntName.place(x=20,y=20)
# # EntPhone = Entry(F1,textvariable= customerphone,justify='center')
# # EntPhone.place(x=20,y=45)
# # Entmail = Entry(F1,textvariable= customermail,justify='center')
# # Entmail.place(x=20,y=96)
# # EntFatora = Entry(F1,textvariable= customerfatora,justify='center',state=DISABLED)
# # EntFatora.place(x=20,y=73)
# # btnCustomer = Button(F1,text='بحث',font=('tajawal',12),width=10,height=2,bg='white',borderwidth=0,command=Database_Search)
# # btnCustomer.place(x=30,y=160)
# # btnAdd = Button(F1,text='اضافة',font=('tajawal',12),width=10,height=2,bg='white',borderwidth=0,command=Database_Add)
# # btnAdd.place(x=150,y=160)
# # #===== Bill =======
# # F3 = Frame(root,bd=2,bg='#E3E4DB',width=350,height=450)
# # F3.place(x=985,y=240)
# # scroll_y = Scrollbar(F3,orient=VERTICAL)
# # textarea = Text(F3,bg='#E3E4DB',width=35,height=26,font=mainFont,yscrollcommand=scroll_y.set)
# # scroll_y.pack(side=LEFT,fill=Y)
# # scroll_y.config(command=textarea.yview)
# # textarea.pack(fill=BOTH,expand=1)
# # textarea.config(state=DISABLED)

# =========== Welcome ==============
# def welcome():
#     textarea.config(state=NORMAL)
#     textarea.delete('1.0', END)
#     textarea.insert(END,"\t Supermarket says Hello!")
#     textarea.insert(END,"\n ======================================")
#     textarea.insert(END,f"\n\tB.Num: {customerfatora.get()}\t")
#     textarea.insert(END,f"\n\tNAME: {customername.get()}")
#     textarea.insert(END,f"\n\tPHONE: {customerphone.get()}")
#     textarea.insert(END,f"\n\tADRESS: {customeraddress.get()}")
#     textarea.insert(END,f"\n\tEMAIL: {customermail.get()}")
#     textarea.insert(END,"\n======================================")
#     textarea.insert(END,f"\n Items  \t   Number \t   Price")
#     textarea.insert(END,"\n======================================")

def bill():
    global textarea
    total_boqliat_prices = (
    ( q1.get() *ricePrice) +
    ( q2.get() *bor8lPrice) +
    ( q3.get() *fasoliaPrice) +
    ( q4.get() *adsPrice) +
    ( q5.get() *makronaPrice) +
    ( q6.get() *freekPrice) +
    ( q7.get() *homsPrice) +
    ( q8.get() *foolPrice) +
    ( q9.get() *ta3myaPrice) +
    ( q10.get() *bznganPrice) +
    ( q11.get() *potatoesPrice) +
    ( q12.get() *termasPricehelw) +
    ( q13.get() *basalaPrice) +
    ( q14.get() *qolqasPrice) +
    ( q15.get() *bamyaPrice) +
    ( q16.get() *TermasPrice) +
    ( q17.get() *LobyaPrice) +
    ( q18.get() *basalaPrice) +
    ( q19.get() *adsa7marPrice) +
    ( q20.get() *ads5derPrice) +
    ( q21.get() *admamyPrice) 
)
    total_lwazem_prices = (
    ( qq1.get() *masfaPrice) +
    ( qq2.get() *platePrice) +
    ( qq3.get() *cupPrice) +
    ( qq4.get() *knifePrice) +
    ( qq5.get() *forkPrice) +
    ( qq6.get() *tangaraPrice) +
    ( qq7.get() *spoonPrice) +
    ( qq8.get() *chargerPrice) +
    ( qq9.get() *basketPrice) +
    ( qq10.get() *sanyaPrice) +
    ( qq11.get() *w3aa5aletPrice) +
    ( qq12.get() *bottleOpenerPrice) +
    ( qq13.get() *maqsharaPrice) +
    ( qq14.get() *m7fzaPrice) +
    ( qq15.get() *akyasPrice) +
    ( qq16.get() *garbigbasketPrice) +
    ( qq17.get() *cupsPrice) +
    ( qq18.get() *containerPrice) +
    ( qq19.get() *lo7ttqte3Price) +
    ( qq20.get() *hafaraPrice) +
    ( qq21.get() *kabshaPrice) 
)
    total_khraba_prices = (
    ( qqq1.get() *tvPrice) +
    ( qqq2.get() *washerPrice) +
    ( qqq3.get() *fridgePrice) +
    ( qqq4.get() *microwavePrice) +
    ( qqq5.get() *khalatPrice) +
    ( qqq6.get() *mqlaPrice) +
    ( qqq7.get() *radioPrice) +
    ( qqq8.get() *playstationPrice) +
    ( qqq9.get() *waterfilter) +
    ( qqq10.get() *ironPrice) +
    ( qqq11.get() *coolerPrice) +
    ( qqq12.get() *marwhaPriceard) +
    ( qqq13.get() *conditionerPrice) +
    ( qqq14.get() *fornPrice) +
    ( qqq15.get() *maqnasaPrice) +
    ( qqq16.get() *s5aanPrice) +
    ( qqq17.get() *moshtrakPrice) +
    ( qqq18.get() *monitor) +
    ( qqq19.get() *marwhaPrice)
)
    for i in range(1):
        textarea.config(state=NORMAL)
        if q1.get() != 0:
            textarea.insert(END,f"\nRice\t {q1.get()}\t {q1.get() *ricePrice}")
        if q2.get() != 0:
            textarea.insert(END,f"\nBorkhl\t {q2.get()}\t {q2.get() *bor8lPrice} ")
        if q3.get() != 0:
            textarea.insert(END,f"\nFasolia\t {q3.get()}\t {q3.get() *fasoliaPrice} ")
        if q4.get() != 0:
            textarea.insert(END,f"\n3ds\t {q4.get()}\t {q4.get() *adsPrice} ")
        if q5.get() != 0:
            textarea.insert(END,f"\nMaqarona\t {q5.get()}\t {q5.get() *makronaPrice} ")
        if q6.get() != 0:
            textarea.insert(END,f"\nFeryq\t {q6.get()}\t {q6.get() *freekPrice} ")
        if q7.get() != 0:
            textarea.insert(END,f"\nHoms\t {q7.get()}\t {q7.get() *homsPrice} ")
        if q8.get() != 0:
            textarea.insert(END,f"\nBeans\t {q8.get()}\t {q8.get() *foolPrice} ")
        if q9.get() != 0:
            textarea.insert(END,f"\nTa3meya\t {q9.get()}\t {q9.get() *ta3myaPrice} ")
        if q10.get() != 0:
            textarea.insert(END,f"\nBazengan\t {q10.get()}\t {q10.get() *bznganPrice} ")
        if q11.get() != 0:
            textarea.insert(END,f"\nPotatoes\t {q11.get()}\t {q11.get() *potatoesPrice} ")
        if q12.get() != 0:
            textarea.insert(END,f"\nTermas7elw\t {q12.get()}\t {q12.get() *termasPricehelw} ")
        if q13.get() != 0:
            textarea.insert(END,f"\nBesla\t {q13.get()}\t {q13.get() *beslaPrice} ")
        if q14.get() != 0:
            textarea.insert(END,f"\nQolqas\t {q14.get()}\t {q14.get() *qolqasPrice} ")
        if q15.get() != 0:
            textarea.insert(END,f"\nBamya\t {q15.get()}\t {q15.get() *bamyaPrice} ")
        if q16.get() != 0:
            textarea.insert(END,f"\nTermas\t {q16.get()}\t {q16.get() *TermasPrice} ")
        if q17.get() != 0:
            textarea.insert(END,f"\nLobya\t {q17.get()}\t {q17.get() *LobyaPrice} ")
        if q18.get() != 0:
            textarea.insert(END,f"\n Besala\t {q18.get()}\t {q18.get() *beslaPrice} ")
        if q19.get() != 0:
            textarea.insert(END,f"\n3ds Ah7mar \t {q19.get()}\t {q19.get() *adsa7marPrice} ")
        if q20.get() != 0:
            textarea.insert(END,f"\n3ds A5der\t {q20.get()}\t {q20.get() *ads5derPrice} ")
        if q21.get() != 0:
            textarea.insert(END,f"\nAdmamy\t {q21.get()}\t {q21.get() *admamyPrice} ")
        #===== Lawazem =====
        if qq1.get() != 0:
            textarea.insert(END,f"\nMasfa\t {qq1.get()}\t {qq1.get() *masfaPrice}")
        if qq2.get() != 0:
            textarea.insert(END,f"\nSahn\t {qq2.get()}\t {qq2.get() *platePrice}")
        if qq3.get() != 0:
            textarea.insert(END,f"\nKas\t {qq3.get()}\t {qq3.get() *cupPrice}")
        if qq4.get() != 0:
            textarea.insert(END,f"\nKnife\t {qq4.get()}\t {qq1.get() *knifePrice}")
        if qq5.get() != 0:
            textarea.insert(END,f"\nFork\t {qq5.get()}\t {qq5.get() *forkPrice}")
        if qq6.get() != 0:
            textarea.insert(END,f"\nTangara\t {qq6.get()}\t {qq6.get() *tangaraPrice}")
        if qq7.get() != 0:
            textarea.insert(END,f"\nSpoon\t {qq7.get()}\t {qq7.get() *spoonPrice}")
        if qq8.get() != 0:
            textarea.insert(END,f"\nShahn\t {qq8.get()}\t {qq8.get() *chargerPrice}")
        if qq9.get() != 0:
            textarea.insert(END,f"\nBasket\t {qq9.get()}\t {qq9.get() *basketPrice}")
        if qq10.get() != 0:
            textarea.insert(END,f"\nSanya\t {qq10.get()}\t {qq10.get() *sanyaPrice}")
        if qq11.get() != 0:
            textarea.insert(END,f"\nW3a 5alt\t {qq11.get()}\t {qq11.get() *w3aa5aletPrice}")
        if qq12.get() != 0:
            textarea.insert(END,f"\nBottle Opner\t {qq12.get()}\t {qq12.get() *bottleOpenerPrice}")
        if qq13.get() != 0:
            textarea.insert(END,f"\nMakshra\t {qq13.get()}\t {qq13.get() *maqsharaPrice}")
        if qq14.get() != 0:
            textarea.insert(END,f"\nMahfza\t {qq14.get()}\t {qq14.get() *m7fzaPrice}")
        if qq15.get() != 0:
            textarea.insert(END,f"\nAkyas\t {qq15.get()}\t {qq15.get() *akyasPrice}")
        if qq16.get() != 0:
            textarea.insert(END,f"\nBasket\t {qq16.get()}\t {qq16.get() *garbigbasketPrice}")
        if qq17.get() != 0:
            textarea.insert(END,f"\nCups\t {qq17.get()}\t {qq17.get() *cupsPrice}")
        if qq18.get() != 0:
            textarea.insert(END,f"\n3lba\t {qq18.get()}\t {qq18.get() *containerPrice}")
        if qq19.get() != 0:
            textarea.insert(END,f"\nCutting Plate\t {qq19.get()}\t {qq19.get() *lo7ttqte3Price}")
        if qq20.get() != 0:
            textarea.insert(END,f"\nHfaar\t {qq20.get()}\t {qq20.get() *hafaraPrice}")
        if qq21.get() != 0:
            textarea.insert(END,f"\nKabsha\t {qq21.get()}\t {qq21.get() *kabshaPrice}")
        #==== Kahraba ====
        if qqq1.get() != 0:
            textarea.insert(END,f"\nT.V.\t{qqq1.get()}\t{qqq1.get() * tvPrice}")
        if qqq2.get() != 0:
            textarea.insert(END,f"\nWasher\t{qqq2.get()}\t{qqq2.get() * washerPrice}")
        if qqq3.get() != 0:
            textarea.insert(END,f"\nFridge\t{qqq3.get()}\t{qqq3.get() * fridgePrice}")
        if qqq4.get() != 0:
            textarea.insert(END,f"\nMicrowave\t{qqq4.get()}\t{qqq4.get() * microwavePrice}")
        if qqq5.get() != 0:
            textarea.insert(END,f"\n5lat\t{qqq5.get()}\t{qqq5.get() * khalatPrice}")
        if qqq6.get() != 0:
            textarea.insert(END,f"\nElectric Pan\t{qqq6.get()}\t{qqq6.get() * mqlaPrice}")
        if qqq7.get() != 0:
            textarea.insert(END,f"\nRadio\t{qqq7.get()}\t{qqq7.get() * radioPrice}")
        if qqq8.get() != 0:
            textarea.insert(END,f"\nPlaystation\t{qqq8.get()}\t{qqq8.get() * playstationPrice}")
        if qqq9.get() != 0:
            textarea.insert(END,f"\nWater Filter\t{qqq9.get()}\t{qqq9.get() * waterfilter}")
        if qqq10.get() != 0:
            textarea.insert(END,f"\nIron\t{qqq10.get()}\t{qqq10.get() * ironPrice}")
        if qqq11.get() != 0:
            textarea.insert(END,f"\nCooler\t{qqq11.get()}\t{qqq11.get() * coolerPrice}")
        if qqq12.get() != 0:
            textarea.insert(END,f"\nFan\t{qqq12.get()}\t{qqq12.get() * marwhaPriceard}")
        if qqq13.get() != 0:
            textarea.insert(END,f"\nGround Fan\t{qqq13.get()}\t{qqq13.get() * conditionerPrice}")
        if qqq14.get() != 0:
            textarea.insert(END,f"\nAir Conditioner\t{qqq14.get()}\t{qqq14.get() * fornPrice}")
        if qqq15.get() != 0:
            textarea.insert(END,f"\nOven\t{qqq15.get()}\t{qqq15.get() * maqnasaPrice}")
        if qqq16.get() != 0:
            textarea.insert(END,f"\nMaknesa\t{qqq16.get()}\t{qqq16.get() * s5aanPrice}")
        if qqq17.get() != 0:
            textarea.insert(END,f"\nHeater\t{qqq17.get()}\t{qqq17.get() * moshtrakPrice}")
        if qqq18.get() != 0:
            textarea.insert(END,f"\nMoshtrak\t{qqq18.get()}\t{qqq18.get() * monitor}")
        if qqq19.get() != 0:
            textarea.insert(END,f"\nMonitor\t{qqq19.get()}\t{qqq19.get() * marwhaPrice}")

        textarea.insert(END,f"\nTotal\t{str(total_boqliat_prices + total_lwazem_prices + total_khraba_prices)}" + "$")
    textarea.config(state=DISABLED)
#===================== Clearing Function ===========================
def Clear():
    q1.set(0)
    q2.set(0)
    q3.set(0)
    q4.set(0)
    q5.set(0)
    q6.set(0)
    q7.set(0)
    q8.set(0)
    q9.set(0)
    q10.set(0)
    q11.set(0)
    q12.set(0)
    q13.set(0)
    q14.set(0)
    q15.set(0)
    q16.set(0)
    q17.set(0)
    q18.set(0)
    q19.set(0)
    q20.set(0)
    q21.set(0)
    #=== Lwazem
    qq1.set(0)
    qq2.set(0)
    qq3.set(0)
    qq4.set(0)
    qq5.set(0)
    qq6.set(0)
    qq7.set(0)
    qq8.set(0)
    qq9.set(0)
    qq10.set(0)
    qq11.set(0)
    qq12.set(0)
    qq13.set(0)
    qq14.set(0)
    qq15.set(0)
    qq16.set(0)
    qq17.set(0)
    qq18.set(0)
    qq19.set(0)
    qq20.set(0)
    qq21.set(0)
    #=== Kharba ====
    qqq1.set(0)
    qqq2.set(0)
    qqq3.set(0)
    qqq4.set(0)
    qqq5.set(0)
    qqq6.set(0)
    qqq7.set(0)
    qqq8.set(0)
    qqq9.set(0)
    qqq10.set(0)
    qqq11.set(0)
    qqq12.set(0)
    qqq13.set(0)
    qqq14.set(0)
    qqq15.set(0)
    qqq16.set(0)
    qqq17.set(0)
    qqq18.set(0)
    qqq19.set(0)
    qqq20.set(0)
    qqq21.set(0)
    #=== Totals =====
    total_boqliat.set('$'+str(0))
    total_khraba.set('$'+str(0))
    total_lwazem.set('$'+str(0))
    customername.set('')
    customerphone.set('')
    customeraddress.set('')
    customermail.set('')
    #==== Bill ======
    textarea.config(state=NORMAL)
    textarea.delete(1.0,END)
    textarea.config(state=DISABLED)
    #===== Generate Bill =========
    x = random.randint(1000,9999)
    customerfatora.set(str(x))
#================== Saving Fatora ===================================
def Print():
    allprintedfatora = open("Fatora1.txt","a+",encoding="utf-8")
    printFatora = open("Fatora.txt","w",encoding="utf-8")
    textarea.config(state=NORMAL)
    printedfatoraValue = str(f'\n\n{textarea.get(1.0,END)}')
    allprintedfatora.write(str(printedfatoraValue))
    # printfatoraValue = str(f'\n\n{textarea.get(1.0,END)}')
    printFatora.write(str(printedfatoraValue))
    now = datetime.now()
    allprintedfatora.write(now.strftime("\n======== %Y-%m-%d %H:%M:%S\t ============"))
    printFatora.write(now.strftime("\n======== %Y-%m-%d %H:%M:%S\t ============"))
    # file_path = './Fatora.txt'

    # os.startfile(file_path,'print')
    print(now.strftime("%Y-%m-%d %H:%M:%S"))
    #========================== Mailing Function ======================================#
def Send():
    from mailtest import sendEmail
    from mailtest import smtplib
    try:
        sendEmail(customermail.get())
        messagebox.showinfo('Sent','Recipt Sent')
    except smtplib.SMTPRecipientsRefused:
        messagebox.showerror("Error", "Write an email")

    def Greet():
        messagebox.showinfo("Recipt Sent")
    Greet()
#======================================================================================== Price ======================================================================
F4 = Frame(root, bd=2, width=800, height=120,bg='#0B4C5F')
F4.place(x=640,y=678)
hesab = Button(F4,text='الحساب',width=7,height=1,borderwidth=0,font='tajawal',bg='#DBA901',command=total)
hesab.place(x=240,y=90)
# fatora = Button(F4, text='تصدير الفاتورة', width=15, height=1,borderwidth=0, font= mainFont, bg='#DBA901',command=(Print))
# fatora.place(x=520, y=55)
# fatora = Button(F4, text=' فاتورة الكترونية', width=15, height=1,borderwidth=0, font= mainFont, bg='#DBA901',command=(Send))
# fatora.place(x=440, y=90)
clear = Button(F4, text='افراغ الحقول', width=13,borderwidth=0, height=1, font=mainFont,bg='#DBA901',command=Clear)
clear.place(x=360, y=10)
exite = Button(F4, text='اغلاق البرنامج', width=13, height=1,borderwidth=0, font=mainFont,bg='#DBA901',command=quit)
exite.place(x=360, y=55)
lbol = Label(F4, text='الحساب الكلي للبقوليات' ,font=(mainFont,10,'bold'),bg=frameBg, fg='gold')
lbol.place(x=235,y=10)
lbol2 = Label(F4, text='حساب اللوازم المنزلية' ,font=(mainFont,10,'bold'),bg=frameBg, fg='gold')
lbol2.place(x=235,y=40)
lbol3 = Label(F4, text='حساب ادوات الكهرباء' ,font=(mainFont,10,'bold'),bg=frameBg, fg='gold')
lbol3.place(x=235,y=70)
ento1 = Entry(F4,textvariable=bacoliat, width=24,state=DISABLED)
ento1.place(x=2,y=12)
ento2 = Entry(F4, textvariable=adoat, width=24,state=DISABLED)
ento2.place(x=2,y=42)
ento3 = Entry(F4, textvariable=kahraba, width=24,state=DISABLED)
ento3.place(x=2,y=72)
#============= Items1 =======
FF1 = Frame(root,bd=2, width=318,height=800,bg=frameBg)
FF1.place(x=1,y=35)
t = Label(FF1, text='البقوليات', font=(mainFont,15,'bold'), bg=frameBg, fg='gold')
t.place(x=122,y=0)
bq1 = Label(FF1, text='الرز', font=(mainFont,11), bg=frameBg, fg='white')
bq1.place(x=250,y=50)
bq2 = Label(FF1, text='البرغل', font=(mainFont,11), bg=frameBg, fg='white')
bq2.place(x=235,y=80)
bq3 = Label(FF1, text='قاسوليا', font=(mainFont,11), bg=frameBg, fg='white')
bq3.place(x=225,y=110)
bq4 = Label(FF1, text='عدس', font=(mainFont,11), bg=frameBg, fg='white')
bq4.place(x=228,y=140)
bq5 = Label(FF1, text='معكرونة', font=(mainFont,11), bg=frameBg, fg='white')
bq5.place(x=220,y=170)
bq6 = Label(FF1, text='فريكة', font=(mainFont,11), bg=frameBg, fg='white')
bq6.place(x=232,y=200)
bq7 = Label(FF1, text='حمص', font=(mainFont,11), bg=frameBg, fg='white')
bq7.place(x=226,y=230)
bq8 = Label(FF1, text='فول', font=(mainFont,11), bg=frameBg, fg='white')
bq8.place(x=236,y=260)
bq9 = Label(FF1, text='طعمية', font=(mainFont,11), bg=frameBg, fg='white')
bq9.place(x=220,y=290)
bq10 = Label(FF1, text='بذنجان', font=(mainFont,11), bg=frameBg, fg='white')
bq10.place(x=225,y=320)
bq11 = Label(FF1, text='بطاطس', font=(mainFont,11), bg=frameBg, fg='white')
bq11.place(x=210,y=350)
bq12 = Label(FF1, text='ترمس حلو', font=(mainFont,11), bg=frameBg, fg='white')
bq12.place(x=205,y=380)
bq13 = Label(FF1, text='بسلة', font=(mainFont,11), bg=frameBg, fg='white')
bq13.place(x=225,y=410)
bq14 = Label(FF1, text='قلقاس', font=(mainFont,11), bg=frameBg, fg='white')
bq14.place(x=215,y=440)
bq15 = Label(FF1, text='بميا', font=(mainFont,11), bg=frameBg, fg='white')
bq15.place(x=230,y=470)
bq16 = Label(FF1, text='الترمس', font=(mainFont,11), bg=frameBg, fg='white')
bq16.place(x=210,y=500)
bq17 = Label(FF1, text='اللوبيا', font=(mainFont,11), bg=frameBg, fg='white')
bq17.place(x=218,y=530)
bq18 = Label(FF1, text='البازلاء', font=(mainFont,11), bg=frameBg, fg='white')
bq18.place(x=218,y=560)
bq19 = Label(FF1, text='عدس احمر', font=(mainFont,11), bg=frameBg, fg='white')
bq19.place(x=195,y=590)
bq20 = Label(FF1, text='عدس اخضر', font=(mainFont,11), bg=frameBg, fg='white')
bq20.place(x=195,y=620)
bq21 = Label(FF1, text='الادمامي', font=(mainFont,11), bg=frameBg, fg='white')
bq21.place(x=210,y=650)


bqent = Entry(FF1, textvariable= q1,width=14)
bqent.place(x=70,y=50)
bqent1 = Entry(FF1,textvariable= q2, width=14)
bqent1.place(x=70,y=80)
bqent2 = Entry(FF1,textvariable= q3,width=14)
bqent2.place(x=70,y=110)
bqent3 = Entry(FF1,textvariable= q4,width=14)
bqent3.place(x=70,y=140)
bqent4 = Entry(FF1,textvariable= q5,width=14)
bqent4.place(x=70,y=170)
bqent5 = Entry(FF1,textvariable= q6,width=14)
bqent5.place(x=70,y=200)
bqent6 = Entry(FF1,textvariable= q7,width=14)
bqent6.place(x=70,y=230)
bqent7 = Entry(FF1,textvariable= q8,width=14)
bqent7.place(x=70,y=260)
bqent8 = Entry(FF1,textvariable= q9,width=14)
bqent8.place(x=70,y=290)
bqent9 = Entry(FF1,textvariable= q10,width=14)
bqent9.place(x=70,y=320)
bqent10 = Entry(FF1,textvariable= q11,width=14)
bqent10.place(x=70,y=350)
bqent11 = Entry(FF1,textvariable= q12, width=14)
bqent11.place(x=70,y=380)
bqent12 = Entry(FF1,textvariable= q13,width=14)
bqent12.place(x=70,y=410)
bqent13 = Entry(FF1,textvariable= q14, width=14)
bqent13.place(x=70,y=440)
bqent14 = Entry(FF1,textvariable= q15,width=14)
bqent14.place(x=70,y=470)
bqent15 = Entry(FF1,textvariable= q16,width=14)
bqent15.place(x=70,y=500)
bqent16 = Entry(FF1,textvariable= q17,width=14)
bqent16.place(x=70,y=530)
bqent17 = Entry(FF1,textvariable= q18,width=14)
bqent17.place(x=70,y=560)
bqent18 = Entry(FF1,textvariable= q19,width=14)
bqent18.place(x=70,y=590)
bqent19 = Entry(FF1,textvariable= q20,width=14)
bqent19.place(x=70,y=620)
bqent20 = Entry(FF1,textvariable= q21,width=14)
bqent20.place(x=70,y=650)
#--- items[2] ======
FF2 = Frame(root,bd=2, width=318,height=800,bg=frameBg)
FF2.place(x=321,y=35)
h = Label(FF2, text='اللوازم المنزلية', font=(mainFont,15,'bold'), bg=frameBg, fg='gold')
h.place(x=122,y=0)
bq1 = Label(FF2, text='مصفاة', font=(mainFont,11), bg=frameBg, fg='white')
bq1.place(x=240,y=50)
bq2 = Label(FF2, text='صحن', font=(mainFont,11), bg=frameBg, fg='white')
bq2.place(x=245,y=80)
bq3 = Label(FF2, text='كأس', font=(mainFont,11), bg=frameBg, fg='white')
bq3.place(x=245,y=110)
bq4 = Label(FF2, text='سكين', font=(mainFont,11), bg=frameBg, fg='white')
bq4.place(x=240,y=140)
bq5 = Label(FF2, text='شوك', font=(mainFont,11), bg=frameBg, fg='white')
bq5.place(x=240,y=170)
bq6 = Label(FF2, text='طنجرة', font=(mainFont,11), bg=frameBg, fg='white')
bq6.place(x=235,y=200)
bq7 = Label(FF2, text='ملعقة', font=(mainFont,11), bg=frameBg, fg='white')
bq7.place(x=236,y=230)
bq8 = Label(FF2, text='شاحن', font=(mainFont,11), bg=frameBg, fg='white')
bq8.place(x=236,y=260)
bq9 = Label(FF2, text='سلة', font=(mainFont,11), bg=frameBg, fg='white')
bq9.place(x=245,y=290)
bq10 = Label(FF2, text='صينية', font=(mainFont,11), bg=frameBg, fg='white')
bq10.place(x=240,y=320)
bq11 = Label(FF2, text='وعاء الخلط', font=(mainFont,11), bg=frameBg, fg='white')
bq11.place(x=215,y=350)
bq12 = Label(FF2, text='فتاحة العلب', font=(mainFont,11), bg=frameBg, fg='white')
bq12.place(x=215,y=380)
bq13 = Label(FF2, text='مقشرة', font=(mainFont,11), bg=frameBg, fg='white')
bq13.place(x=235,y=410)
bq14 = Label(FF2, text='محفظة', font=(mainFont,11), bg=frameBg, fg='white')
bq14.place(x=235,y=440)
bq15 = Label(FF2, text='اكياس', font=(mainFont,11), bg=frameBg, fg='white')
bq15.place(x=235,y=470)
bq16 = Label(FF2, text='سلة قمامة', font=(mainFont,11), bg=frameBg, fg='white')
bq16.place(x=215,y=500)
bq17 = Label(FF2, text='اكواب', font=(mainFont,11), bg=frameBg, fg='white')
bq17.place(x=238,y=530)
bq18 = Label(FF2, text='علب', font=(mainFont,11), bg=frameBg, fg='white')
bq18.place(x=240,y=560)
bq19 = Label(FF2, text='لوحة التقطيع', font=(mainFont,11), bg=frameBg, fg='white')
bq19.place(x=205,y=590)
bq20 = Label(FF2, text='حفارة', font=(mainFont,11), bg=frameBg, fg='white')
bq20.place(x=235,y=620)
bq21 = Label(FF2, text='كبشة', font=(mainFont,11), bg=frameBg, fg='white')
bq21.place(x=230,y=650)


bqent = Entry(FF2,textvariable= qq1,width=14)
bqent.place(x=70,y=50)
bqent1 = Entry(FF2,textvariable= qq2,width=14)
bqent1.place(x=70,y=80)
bqent2 = Entry(FF2,textvariable= qq3,width=14)
bqent2.place(x=70,y=110)
bqent3 = Entry(FF2,textvariable= qq4,width=14)
bqent3.place(x=70,y=140)
bqent4 = Entry(FF2,textvariable= qq5,width=14)
bqent4.place(x=70,y=170)
bqent5 = Entry(FF2,textvariable= qq6,width=14)
bqent5.place(x=70,y=200)
bqent6 = Entry(FF2,textvariable= qq7,width=14)
bqent6.place(x=70,y=230)
bqent7 = Entry(FF2,textvariable= qq8,width=14)
bqent7.place(x=70,y=260)
bqent8 = Entry(FF2,textvariable= qq9,width=14)
bqent8.place(x=70,y=290)
bqent9 = Entry(FF2,textvariable= qq10, width=14)
bqent9.place(x=70,y=320)
bqent10 = Entry(FF2,textvariable= qq11, width=14)
bqent10.place(x=70,y=350)
bqent11 = Entry(FF2,textvariable= qq12,width=14)
bqent11.place(x=70,y=380)
bqent12 = Entry(FF2,textvariable= qq13,width=14)
bqent12.place(x=70,y=410)
bqent13 = Entry(FF2,textvariable= qq14,width=14)
bqent13.place(x=70,y=440)
bqent14 = Entry(FF2,textvariable= qq15,width=14)
bqent14.place(x=70,y=470)
bqent15 = Entry(FF2,textvariable= qq16,width=14)
bqent15.place(x=70,y=500)
bqent16 = Entry(FF2,textvariable= qq17,width=14)
bqent16.place(x=70,y=530)
bqent17 = Entry(FF2,textvariable= qq18,width=14)
bqent17.place(x=70,y=560)
bqent18 = Entry(FF2,textvariable= qq19,width=14)
bqent18.place(x=70,y=590)
bqent19 = Entry(FF2,textvariable= qq20,width=14)
bqent19.place(x=70,y=620)
bqent20 = Entry(FF2,textvariable= qq21,width=14)
bqent20.place(x=70,y=650)

# ==== Items 3 ==========
FF3 = Frame(root,bd=2, width=338,height=640,bg=frameBg)
FF3.place(x=641,y=35)
h = Label(FF3, text='أدوات كهربائية', font=(mainFont,15,'bold'), bg=frameBg, fg='gold')
h.place(x=122,y=0)
bq1 = Label(FF3, text='تلفزيون', font=(mainFont,11), bg=frameBg, fg='white')
bq1.place(x=240,y=50)
bq2 = Label(FF3, text='غسالة', font=(mainFont,11), bg=frameBg, fg='white')
bq2.place(x=245,y=80)
bq3 = Label(FF3, text='ثلاجة', font=(mainFont,11), bg=frameBg, fg='white')
bq3.place(x=250,y=110)
bq4 = Label(FF3, text='مكرويف', font=(mainFont,11), bg=frameBg, fg='white')
bq4.place(x=240,y=140)
bq5 = Label(FF3, text='خلاط', font=(mainFont,11), bg=frameBg, fg='white')
bq5.place(x=250,y=170)
bq6 = Label(FF3, text='مقلاة كهربائية', font=(mainFont,11), bg=frameBg, fg='white')
bq6.place(x=215,y=200)
bq7 = Label(FF3, text='راديو', font=(mainFont,11), bg=frameBg, fg='white')
bq7.place(x=256,y=230)
bq8 = Label(FF3, text='بلاي ستيشن', font=(mainFont,11), bg=frameBg, fg='white')
bq8.place(x=216,y=260)
bq9 = Label(FF3, text='فلتر ماء', font=(mainFont,11), bg=frameBg, fg='white')
bq9.place(x=245,y=290)
bq10 = Label(FF3, text='مكواة', font=(mainFont,11), bg=frameBg, fg='white')
bq10.place(x=250,y=320)
bq11 = Label(FF3, text='مبرد', font=(mainFont,11), bg=frameBg, fg='white')
bq11.place(x=258,y=350)
bq12 = Label(FF3, text='مروحة ارضية', font=(mainFont,11), bg=frameBg, fg='white')
bq12.place(x=225,y=380)
bq13 = Label(FF3, text='تكييف', font=(mainFont,11), bg=frameBg, fg='white')
bq13.place(x=255,y=410)
bq14 = Label(FF3, text='فرن غاز', font=(mainFont,11), bg=frameBg, fg='white')
bq14.place(x=255,y=440)
bq15 = Label(FF3, text='مكنسة', font=(mainFont,11), bg=frameBg, fg='white')
bq15.place(x=255,y=470)
bq16 = Label(FF3, text='سخان', font=(mainFont,11), bg=frameBg, fg='white')
bq16.place(x=255,y=500)
bq17 = Label(FF3, text='مشترك كهربائي', font=(mainFont,11), bg=frameBg, fg='white')
bq17.place(x=218,y=530)
bq18 = Label(FF3, text='شاشة كمبيوتر', font=(mainFont,11), bg=frameBg, fg='white')
bq18.place(x=225,y=560)
bq19 = Label(FF3, text='مروحة سقف', font=(mainFont,11), bg=frameBg, fg='white')
bq19.place(x=225,y=590)

bqent = Entry(FF3,textvariable= qqq1,width=14)
bqent.place(x=70,y=50)
bqent1 = Entry(FF3,textvariable= qqq2,width=14)
bqent1.place(x=70,y=80)
bqent2 = Entry(FF3,textvariable= qqq3,width=14)
bqent2.place(x=70,y=110)
bqent3 = Entry(FF3,textvariable= qqq4,width=14)
bqent3.place(x=70,y=140)
bqent4 = Entry(FF3,textvariable= qqq5,width=14)
bqent4.place(x=70,y=170)
bqent5 = Entry(FF3,textvariable= qqq6,width=14)
bqent5.place(x=70,y=200)
bqent6 = Entry(FF3,textvariable= qqq7,width=14)
bqent6.place(x=70,y=230)
bqent7 = Entry(FF3,textvariable= qqq8,width=14)
bqent7.place(x=70,y=260)
bqent8 = Entry(FF3,textvariable= qqq9,width=14)
bqent8.place(x=70,y=290)
bqent9 = Entry(FF3,textvariable= qqq10,width=14)
bqent9.place(x=70,y=320)
bqent10 = Entry(FF3,textvariable= qqq11,width=14)
bqent10.place(x=70,y=350)
bqent11 = Entry(FF3,textvariable= qqq12,width=14)
bqent11.place(x=70,y=380)
bqent12 = Entry(FF3,textvariable= qqq13,width=14)
bqent12.place(x=70,y=410)
bqent13 = Entry(FF3,textvariable= qqq14,width=14)
bqent13.place(x=70,y=440)
bqent14 = Entry(FF3,textvariable= qqq15,width=14)
bqent14.place(x=70,y=470)
bqent15 = Entry(FF3,textvariable= qqq16,width=14)
bqent15.place(x=70,y=500)
bqent16 = Entry(FF3,textvariable= qqq17,width=14)
bqent16.place(x=70,y=530)
bqent17 = Entry(FF3,textvariable= qqq18,width=14)
bqent17.place(x=70,y=560)
bqent18 = Entry(FF3,textvariable= qqq19,width=14)
bqent18.place(x=70,y=590)

# db.close()
root.mainloop()

