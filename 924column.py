# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from datetime import datetime

Folder_Path = r'D:\kaggle\data'
data = pd.read_csv(Folder_Path + '\\' + 'data1-45.csv')
first = 0
last = 57158
result = np.zeros(((last-first+1), 33*28+1)) #user_id, each user has 33 weeks，one week has 28 time_slot

user_id = first  #first user_id
col = ['user_id']

for i in range(924):
    name = 'time_slot_' + str(i)
    col.append(name)

for i in range(last-first+1):
    result[i][0] = first + i

for i in range(len(data)):
        user_id = data.at[i, 'user_id']
        week = data.at[i, 'week']
        position = int(user_id) - first
        for j in range(28):
            name = 'time_slot_' + str(j)
            t = data.at[i, name]
            result[position][1+week*28+j] = t

file = pd.DataFrame(columns=col, data=result, dtype=int)
Folder_Path = r'D:\kaggle\data924'
file.to_csv(Folder_Path + '\\' + '34week_1-45.csv', index=False)