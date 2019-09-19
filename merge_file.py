# -*- coding: utf-8 -*-

import pandas as pd
import os

#merge file name
Folder_Path = r'D:\kaggle\data\46-75'
SaveFile_Path = r'D:\kaggle\data924'
SaveFile_Name = r'data46-75.csv'

df = pd.read_csv(Folder_Path+'\\'+'data-46.csv')
df.to_csv(SaveFile_Path+'\\'+SaveFile_Name, encoding="utf_8_sig", index=False)

for i in range(47,76):
    df = pd.read_csv(Folder_Path+'\\'+'data-'+str(i)+'.csv')
    df.to_csv(SaveFile_Path+'\\'+SaveFile_Name,encoding="utf_8_sig",index=False, header=False,mode='a+')
