import pandas as pd
import numpy as np
import mysql.connector as sql
import matplotlib.pyplot as pl
import time         
from sqlalchemy import create_engine
print('******                        Started on 8 August 2022                        ******')
print("                               Please wait for 2 seconds...")
time.sleep(2)
localtime=time.asctime(time.localtime(time.time()))
print("NOW IS------->      \U0001f600 \U0001f600 \U0001f600        ", localtime,"\U0001f600 \U0001f600 \U0001f600")
print("                               Please wait for 3 seconds...")
time.sleep(3)
red=input("Enter The Sql and Excel file name to be saved:")
head = []
n = int(input("Enter number of  column elements : "))
m=1
for i in range(0, n):
    ele = input(f"Enter the column {m} heads of Database:")
    if ele=='index':
        ele='sindex'
    m=m+1
    head.append(ele)      
print(head)
levelh=[]

ret = int(input("Enter number of rows you want to add : "))
ma=1
for j in range(0,n):
    lulu=head[j]
    subhead = []
    for i in range(0, ret):
        ele = input(f"enter {lulu} details of database of column{j+1}:")
        ma=ma+1
        subhead.append(ele)  
    levelh.append(subhead)
print(levelh)
d={}
for i in range(0,n):
    k=head[i]
    o=levelh[i]
    d[k]=o
    i=i+1
print(d)
dataframe=pd.DataFrame(d)
print(dataframe)

s=dataframe.to_csv(f"C:\\Users\\om\\Desktop\\{red}.csv")
print(s)
mydata=sql.connect(host='localhost',user='root',password='root',database='till_now')
# solo=input("Enter the desired Database Name:")
# mycursor = mydata.cursor()
# mycursor.execute("CREATE DATABASE",solo)
engine=create_engine('mysql+pymysql://root:root@localhost/python')
mydata=engine.connect()
df=dataframe.to_sql(f"{red}",mydata,if_exists='replace')

# pl.plot(todo,mnp,color='r',marker='o',markersize=4,markeredgecolor='k')
# pl.xlabel('Topics')
# pl.ylabel('Percent learned')
# pl.show()