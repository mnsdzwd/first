# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 08:49:21 2022

@author: Administrator
"""

import pdfplumber
import numpy as np
import pandas as pd



# In[]
with pdfplumber.open('F:/01东荣/01东荣/10系统实施/06销售/2月份/EE220090.pdf') as pdf:
    po1 = []

    for page in pdf.pages:
        for table in page.extract_tables():
            for x in table:
                po1.append(x)
    print(po1)   
  





