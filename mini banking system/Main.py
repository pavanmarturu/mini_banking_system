 #--------------------------BANKING SYSTEM-------------------------#
 
#----------------------------IMPORTS-------------------------------#
from tkinter import*
import os
from PIL import ImageTk, Image
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='saiteja1232',
    database='banking'
)


# ------------------------------MAIN SCREEN----------------------------#
master=Tk()
master.title('BANKING')
 
#-----------------------------FUNCTIONS--------------------------------#
def finish_reg():
    name = temp_name.get()
    age = temp_age.get()
    gender = temp_gender.get()
    password = temp_password.get()
    SSN = temp_SSN.get()
    Mobile = temp_Mobile.get()
    mycursor=mydb.cursor()
    mycursor.execute('select * from customers')
    all_accounts=mycursor.fetchall()
 
    if name=="" or age=="" or password=="" or gender=="" or SSN=="" or Mobile=="":
        notif.config(fg="red", text="All fields required ")
        return
    count=0
    for x in all_accounts:
        count+=1
    for g in range(int(count)):
        if name==all_accounts[g][0]:
            notif.config(fg="red",text="Account already exists")
            return
        else:
             mycursor=mydb.cursor()
             sql='insert into customers(name,age,gender,password,balance,SSN,Mobile) values(%s,%s,%s,%s,%s,%s,%s)'
             val=(name,age,gender,password,0,SSN,Mobile)
             mycursor.execute(sql,val)
             mydb.commit()
             notif.config(fg="green", text="successfully created new Account")
          
def register():
    # -------------------VARIABLES--------------------------#
    global temp_name
    global temp_age
    global temp_gender
    global temp_password
    global temp_SSN
    global temp_Mobile
    global notif
    temp_name = StringVar()
    temp_age = StringVar()
    temp_gender = StringVar()
    temp_password = StringVar()
    temp_SSN = StringVar()
    temp_Mobile = StringVar()      
     # --------------------------REGISTER SCREEN-------------------------#
    register_screen=Toplevel(master)
    register_screen.title('Register')
     # ---------------------------LABELS----------------------------------#
    Label(register_screen, text="Please enter your details to register", font=('Calibri Bold',15),bg="blue", fg="white", relief="solid", bd=2).grid(row=0,sticky=N,pady=10)
    Label(register_screen, text="Name", font=('Calibri',15),bd=2).grid(row=1,sticky=W)
    Label(register_screen, text="Age", font=('Calibri',15),bd=2).grid(row=2,sticky=W)
    Label(register_screen, text="Gender", font=('Calibri',15),bd=2).grid(row=3,sticky=W)
    Label(register_screen, text="Password", font=('Calibri',15),bd=2).grid(row=4,sticky=W)
    Label(register_screen, text="SSN", font=('Calibri',15),bd=2).grid(row=5,sticky=W)
    Label(register_screen, text="Mobile", font=('Calibri',15),bd=2).grid(row=6,sticky=W)
    notif = Label(register_screen, font=('Calibri',15),bd=2)
    notif.grid(row = 7, sticky=N, pady=10)
     # ----------------------------ENTRY--------------------------#
    Entry(register_screen, textvariable=temp_name, relief="solid",bd=2).grid(row=1,column=0)
    Entry(register_screen, textvariable=temp_age, relief="solid",bd=2).grid(row=2,column=0)
    Entry(register_screen, textvariable=temp_gender, relief="solid",bd=2).grid(row=3, column=0)
    Entry(register_screen, textvariable=temp_password,show="*",relief="solid",bd=2).grid(row=4,column=0)
    Entry(register_screen, textvariable=temp_SSN,relief="solid",bd=2).grid(row=5,column=0)
    Entry(register_screen, textvariable=temp_Mobile,relief="solid",bd=2).grid(row=6,column=0)
    #---------------------------Buttons---------------------------#
    Button(register_screen, text="Register", command=finish_reg, font=('Calibri',15),relief="raised",fg="blue",bd=4).grid(row=8,sticky=N, pady=10)
 
def login_session():
    global login_name
    login_name = temp_login_name.get()
    login_password = temp_login_password.get()
 
    mycursor=mydb.cursor()
    mycursor.execute('select * from customers')
    all_accounts=mycursor.fetchall()
    count=0;
    for x in all_accounts:
        count+=1
    for g in range(int(count)):
        if login_name==all_accounts[g][0]:
            # ------------------------------ACCOUNT DASHBOARD----------------------------#
            if login_password ==all_accounts[g][3]:
                login_screen.destroy()
                account_dashboard = Toplevel(master)
                account_dashboard.title('Dashboard')
                 # -----------------------------LABEL-------------------------------------#
                Label(account_dashboard, text="Dashboard",font=('Calibri Bold',14), bg="blue", fg="white", relief="solid", bd=5).grid(row=0, sticky=N, pady=10)
                Label(account_dashboard, text="Welcome "+login_name, font=('Calibri Bold',14), bg="blue", fg="white", relief="solid", bd=5).grid(row=1, sticky=N, pady=5)
                 # -----------------------------BUTTONS------------------------------------#
                Button(account_dashboard, text="Personal Details", font=('Calibri',15), width=30, command=personal_details, relief="raised", fg="blue", bd=4).grid(row=2, sticky=N, padx=10,pady=5)
                Button(account_dashboard, text="Deposit", font=('Calibri',15), width=30, command=deposit, relief="raised", fg="blue", bd=4).grid(row=3, sticky=N, padx=10,pady=5)
                Button(account_dashboard, text="Withdraw", font=('Calibri',15), width=30, command=withdraw, relief="raised", fg="blue", bd=4).grid(row=4, sticky=N, padx=10)
                Label(account_dashboard).grid(row=5, sticky=N, pady=10)
                return
            else:
                login_notif.config(fg="red", text="Password is incorrect!!")
                return
        login_notif.config(fg="red", text="No account found!!")
            
def deposit():
     # --------------------------VARIABLES-----------------------------#
    global amount
    global deposit_notif
    global current_balance_label
    amount = StringVar()

    mycursor=mydb.cursor()
    mycursor.execute('select * from customers')
    all_accounts=mycursor.fetchall()
    count=0;
    for x in all_accounts:
        count+=1
    for g in range(int(count)):
        if login_name==all_accounts[g][0]:
            details_balance=str(all_accounts[g][4])
     # -------------------------------DEPOSIT SCREEN----------------------------#
    deposit_screen = Toplevel(master)
    deposit_screen.title('Deposit')
     # ---------------------------LABEL--------------------------------------#
    Label(deposit_screen, text="Deposit", font=('Calibri Bold',14), bg="blue", fg="white", relief="solid", bd=2).grid(row=0, sticky=N, pady=10)
    current_balance_label = Label(deposit_screen, text="Current Balance : $"+details_balance, font=('Calibri',14), bd=5)
    current_balance_label.grid(row=1, sticky=W)
    Label(deposit_screen, text= "Amount : ", font=('Calibri',14), bd=2).grid(row=2, sticky=W)
    deposit_notif = Label(deposit_screen, font=('Calibri',14), bd=2)
    deposit_notif.grid(row=4, sticky=N, pady=5)
    # ---------------------------ENTRY---------------------------------------#
    Entry(deposit_screen, textvariable=amount, relief="solid", bd=2).grid(row=2, column=1)
    # ---------------------------BUTTON--------------------------------------#
    Button(deposit_screen, text="Finish",  font=('Calibri',15), command=finish_deposit, fg="blue", bd=4).grid(row=3, sticky=W, pady=5)
 
    
def finish_deposit():
    if amount.get() == "":
        deposit_notif.config(text="Amount is required", fg="red")
        return
    if float(amount.get()) <=0:
        deposit_notif.config(text="Negative currency is not accepted", fg="red")
        return
 
    mycursor=mydb.cursor()
    mycursor.execute('select * from customers')
    all_accounts=mycursor.fetchall()
    count=0;
    for x in all_accounts:
        count+=1
    for g in range(int(count)):
        if login_name==all_accounts[g][0]:
            current_balance=str(all_accounts[g][4])

    updated_balance = current_balance
    updated_balance = float(updated_balance) + float(amount.get())
    mycursor=mydb.cursor()
    sql='UPDATE customers SET balance=%s where name=%s'
    val=(updated_balance,login_name)
    mycursor.execute(sql,val)
    mydb.commit()
 
    current_balance_label.config(text="Current Balance : $"+str(updated_balance),fg="green", bd=2)
    deposit_notif.config(text=  "Balance Updated", fg="green", bd=2)
 
    
def withdraw():
    # -------------------------VARIABLES---------------------------#
    global withdraw_amount
    global withdraw_notif
    global current_balance_label
    withdraw_amount = StringVar()
    mycursor=mydb.cursor()
    mycursor.execute('select * from customers')
    all_accounts=mycursor.fetchall()
    count=0;
    for x in all_accounts:
        count+=1
    for g in range(int(count)):
        if login_name==all_accounts[g][0]:
            details_balance=str(all_accounts[g][4])
    # --------------------------WITHDRAW SCREEN----------------------------------#
    withdraw_screen = Toplevel(master)
    withdraw_screen.title('WITHDRAW')
    # -----------------------------LABEL------------------------------#
    Label(withdraw_screen, text="WITHDRAW", font=('Calibri Bold',14), bg="blue", fg="white", relief="solid").grid(row=0, sticky=N, pady=10)
    current_balance_label = Label(withdraw_screen, text="Current Balance : $"+details_balance, font=('Calibri',14), bd=2)
    current_balance_label.grid(row=1, sticky=W)
    Label(withdraw_screen, text= "Amount : ", font=('Calibri',14), bd=2).grid(row=2, sticky=W)
    withdraw_notif = Label(withdraw_screen, font=('Calibri',14), bd=2)
    withdraw_notif.grid(row=4, sticky=N, pady=2)
     # ------------------------------ENTRY---------------------------------#
    Entry(withdraw_screen, textvariable=withdraw_amount, relief="solid", bd=2).grid(row=2, column=1)
     # ---------------------------------BUTTON-------------------------------------#
    Button(withdraw_screen, text="Finish",  font=('Calibri',15), command=finish_withdraw, fg="blue", bd=4).grid(row=3, sticky=W, pady=5)
 
    
def finish_withdraw():
    if withdraw_amount.get() == "":
        withdraw_notif.config(text="Amount is required", fg="red", bd=5)
        return
    if float(withdraw_amount.get()) <=0:
        withdraw_notif.config(text="Negative currency is not accepted", fg="red", bd=2)
        return
 
    mycursor=mydb.cursor()
    mycursor.execute('select * from customers')
    all_accounts=mycursor.fetchall()
    count=0;
    for x in all_accounts:
        count+=1
    for g in range(int(count)):
        if login_name==all_accounts[g][0]:
            current_balance=str(all_accounts[g][4])
 
    if float(withdraw_amount.get()) > float(current_balance):
        withdraw_notif.config(text="Insufficient Funds!", fg="red", bd=2)
        return
    
    updated_balance = current_balance
    updated_balance = float(updated_balance) - float(withdraw_amount.get())

    mycursor=mydb.cursor()
    sql='UPDATE customers SET balance=%s where name=%s'
    val=(updated_balance,login_name)
    mycursor.execute(sql,val)
    mydb.commit()
 
    current_balance_label.config(text="Current Balance : $"+(str(round(updated_balance))),fg="green", bd=5)
    withdraw_notif.config(text=  "Balance Updated", fg="green", bd=2)
 
    
def personal_details():
     #----------------------------VARIABLES-----------------------------------#
    mycursor=mydb.cursor()
    mycursor.execute('select * from customers')
    all_accounts=mycursor.fetchall()
    count=0;
    for x in all_accounts:
        count+=1
    for g in range(int(count)):
        if login_name==all_accounts[g][0]:
         details_name=all_accounts[g][0]
         details_age=str(all_accounts[g][1])
         details_gender =str(all_accounts[g][2])
         details_balance=str(all_accounts[g][4])
         details_SSN=str(all_accounts[g][5])
         details_Mobile=str(all_accounts[g][6])
         
        
     # -------------------------PERSONAL DETAILS SCREEN-----------------------------#
    personal_details_screen = Toplevel(master)
    personal_details_screen.title('Personal Details')
     # ------------------------------LABEL------------------------------------#
    Label(personal_details_screen, text="Personal Details", font=('Calibri Bold',14), bg="blue", fg="white", relief="solid", bd=2).grid(row=0, sticky=N, pady=10)
    Label(personal_details_screen, text="Name : "+details_name, font=('Calibri',14), relief="solid", bd=2).grid(row=1, sticky=W,pady=10)
    Label(personal_details_screen, text="Age : "+details_age, font=('Calibri',14), relief="solid", bd=2).grid(row=2, sticky=W,)
    Label(personal_details_screen, text="Gender : "+details_gender, font=('Calibri',14), relief="solid", bd=2).grid(row=3, sticky=W,pady=10)
    Label(personal_details_screen, text="Balance :$"+details_balance, font=('Calibri',14), relief="solid", bd=2).grid(row=4, sticky=W)
    Label(personal_details_screen, text="SSN : "+details_SSN, font=('Calibri',14), relief="solid", bd=2).grid(row=5, sticky=W)
    Label(personal_details_screen, text="Mobile : "+details_Mobile, font=('Calibri',14), relief="solid", bd=2).grid(row=6, sticky=W)
 
    
def login():
     # ----------------------------VARIABLES------------------------------------#
    global temp_login_name
    global temp_login_password
    global login_notif
    global login_screen
    temp_login_name = StringVar()
    temp_login_password = StringVar()
     # --------------------------------LOGIN SCREEN--------------------------------#
    login_screen = Toplevel(master)
    login_screen.title('Login')
     # --------------------------------LABELS----------------------------------#
    Label(login_screen, text= "Login to your account", font=('Calibri Bold',14),bg="blue", fg="white", relief="solid", bd=2).grid(row=0, sticky=N, pady=10)
    Label(login_screen, text= "Username", font=('Calibri',14), bd=2).grid(row=1, sticky=W)
    Label(login_screen, text= "Password", font=('Calibri',14), bd=2).grid(row=2, sticky=W)
    login_notif = Label(login_screen, font=('Calibri',14), bd=2)
    login_notif.grid(row=4, sticky=N)
     # ------------------------------ENTRY---------------------------------#
    Entry(login_screen, textvariable=temp_login_name, relief="solid", bd=2).grid(row=1, column=1, padx=5)
    Entry(login_screen, textvariable=temp_login_password, show='*', relief="solid", bd=2).grid(row=2, column=1, padx=5)
     # ---------------------------------BUTTON----------------------------#
    Button(login_screen, text="Login", command=login_session, width=15, font=('Calibri',15), relief="raised", fg="blue", bd=4).grid(row=3, sticky=N, pady=5)
 
# --------------------------------IMAGE IMPORT------------------------------#
img = Image.open('C:\\Users\\PAVAN SAITEJA\\OneDrive\\Desktop\\python\\bank.jfif')
img=img.resize((300,300))
img = ImageTk.PhotoImage(img)
 
# --------------------------------LABEL---------------------------------#
Label(master, text="XYZ BANK ", font=('Calibri Bold',14), bg="green", fg="black", relief="solid", bd=2).grid(row=0,sticky=N,pady=10)
Label(master, text=" MOST SECURE DIGITAL BANKING ", font=('Calibri Bold',14), bg="green", fg="black",relief="solid", bd=2).grid(row=1,sticky=N)
Label(master, image=img).grid(row=2, sticky=N, pady=15)
 
# -----------------------------BUTTON---------------------------------#
Button(master, text="REGISTER", font=('Calibri',15),width=20, command=register, relief="raised", fg="blue", bd=5).grid(row=3, sticky=N)
Button(master, text="LOGIN", font=('Calibri',15),width=20, command=login, relief="raised", fg="blue", bd=5).grid(row=4, sticky=N, pady=10)
 
master.mainloop()
