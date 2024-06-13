# import sqlite3

# db =  sqlite3.connect("stock.db")
# try:
#     cr = db.cursor()
#     cr.execute("CREATE TABLE if not exists Food (Electricty TEXT, quantity2 INTGER, Inventory TEXT, quantity3 INTGER)")
#     cr.execute("select * from Food")
#     results = cr.fetchall()
#     # for i in range(len(results)):
#     #     if results[0][1] > 0.2:
#     #         print(str(results[i][0]) + " is stable")
#     #     else:
#     #         import smtplib
#     #         from email.mime.text import MIMEText

#     #         # Email content
#     #         subject = "Cargo about to finish"
#     #         body = f"Dear recipient,\n\nThis is to notify you that the {results[i][0]} is about to finish. Please take necessary action as soon as possible.\n\nBest regards,\nThe Supermarket System"

#     #         # Email addresses
#     #         sender_email = "omarelsawy160@gmail.com"
#     #         recipient_email = "omar.future.123@gmail.com"

#     #         # Email server settings
#     #         smtp_server = "smtp.gmail.com"
#     #         smtp_port = 587
#     #         smtp_username = "omarelsawy160@gmail.com"
#     #         smtp_password = "qxnsyaxbqeatgtxs"

#     #         # Create the email message
#     #         msg = MIMEText(body)
#     #         msg['Subject'] = subject
#     #         msg['From'] = sender_email
#     #         msg['To'] = recipient_email

#     #         # Connect to the SMTP server and send the email
#     #         with smtplib.SMTP(smtp_server, smtp_port) as server:
#     #             server.starttls()
#     #             server.login(smtp_username, smtp_password)
#     #             server.sendmail(sender_email, recipient_email, msg.as_string())
#     #         print("Mail Sent")

# except sqlite3.Error:
#     print("error")
import sqlite3

# connect to the database (create it if it doesn't exist)
conn = sqlite3.connect('mydatabase.db')

# create a cursor
cursor = conn.cursor()

# create a Foods table with the specified columns
cursor.execute('''CREATE TABLE IF NOT EXISTS Foods (
                    Nutrition TEXT,
                    quantity1 INTEGER,
                    price1 REAL,
                    Electricity TEXT,
                    quantity2 INTEGER,
                    price2 REAL,
                    Inventory TEXT,
                    quantity3 INTEGER,
                    price3 REAL)''')

# add 19 items for each column
for i in range(1, 20):
    cursor.execute("INSERT INTO Foods VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", 
                   ('Nutrition ' + str(i), i*2, i*2.5, 'Electricity ' + str(i), i*3, i*3.5, 'Inventory ' + str(i), i*4, i*4.5))

# commit changes and close the connection
conn.commit()
conn.close()
