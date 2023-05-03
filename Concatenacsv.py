#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from pathlib import Path
import os

folder = Path("C:/Users/thiago.silva/Documents/juntar csv")
frame = pd.DataFrame()
list_of_data = []

for file in os.listdir(folder):
    if file.endswith('.csv'):
        frame = pd.read_csv(str(folder)+"\\"+file)
        list_of_data.append(frame)

frame = pd.concat(list_of_data)

name = 'ABRIL_2023.csv'

frame.to_csv(name, index=False) 
print("completo")
    
   
    
    
 


# In[ ]:




