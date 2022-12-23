import mysql.connector
a=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='saiteja1232'
    )
mycursor=a.cursor()
mycursor.execute('create database banking')


import mysql.connector
a=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='saiteja1232',
    database='banking'
)
mycursor=a.cursor()
mycursor.execute('create table customers(name varchar(255),age int,gender varchar(100),password varchar(100),balance int,SSN varchar(100),Mobile varchar(100))')


import mysql.connector
a=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='saiteja1232',
    database='banking'
)
mycursor=a.cursor()
sql='insert into customers(name,age,gender,password,balance,SSN,Mobile) VALUES(%s,%s,%s,%s,%s,%s,%s)'
insert=[
    ('demo1',22,'male',1234,0,1234345675,8070605012),
    ('demo2',21,'female','ram',0,'ab12234bg7',8979695929)
]
    
mycursor.executemany(sql,insert)
a.commit()