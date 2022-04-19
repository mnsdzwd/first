# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 20:30:15 2022

@author: Administrator
"""
import pdfplumber
#import numpy as np
import pandas as pd


# In[]
with pdfplumber.open('d:/01东荣/01东荣/10系统实施/06销售/EE220017订单样本.pdf') as pdf:
    po1 = []
    po2 = []
    po3 = []
    po4 = []
    po5 = []
    po6 = []
    po7 = []
          
    for page in pdf.pages:
        for table in page.extract_tables():
            for x in table:
                if x[0] == '交货日期：':
                    po1.append(x)
                if x[0] == '制单日期：':
                    po2.append(x)
                if x[0] == '序号：':
                    po3.append(x)
                if x[0] == '客户编号：':
                    po4.append(x)
                if x[0] == '数量：':
                    po5.append(x)
                if x[0] == '参考编号：':
                    po6.append(x)
                      
    print(po1)   
    print(po2) 
    print(po3)
    print(po4) 
    print(po5) 
    print(po6)
    print(po7)              
                

# In[]
df1= pd.DataFrame(po1)
print(df1)
df2= pd.DataFrame(po2)
print(df2)
df3=pd.DataFrame(po3)
print(df3)
df4= pd.DataFrame(po4)
print(df4)
df5= pd.DataFrame(po5)
print(df5)
df6= pd.DataFrame(po6)
print(df6)


# In[]
df = pd.read_excel('d:/01东荣/01东荣/10系统实施/06销售/SAL_SaleOrder_订单引入模板.xlsx',sheet_name=1)
print(df)

line = len(po3)

for i in range(line):
    df.at[i+1,"FDate"]=po2[2][1]
    df.at[i+1,"FMaterialId#Name"]=po3[i][3]
    df.at[i+1,"FCustId"]='CUST0001'
    df.at[i+1,"FCustId#Name"]='漳州东荣进出口有限公司'
    df.at[i+1,"FUnitID"]=po5[i][3]
    df.at[i+1,"FDeliveryDate"]=po1[i][1]
    df.at[i+1,"FSalerId"]='DRGM323_GW000141_1'
    df.at[i+1,"FSalerId#Name"]=po2[i][3]

df.to_excel('d:/01东荣/01东荣/10系统实施/06销售/SAL_SaleOrder_订单引入模板2.xlsx',sheet_name="销售订单#基本信息(FBillHead)",index=False)



# In[]
print(po3[1][3])

# In[]
