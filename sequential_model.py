#coding=utf-8
import keras
import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, Dropout

Folder_Path = r'D:\kaggle\data924'
data = pd.read_csv(Folder_Path + '\\' + '34week_1-45.csv')
col = []  #for X column name
col_name = []  #for y column name
first = 57159  #y_test first user_id
for i in range(924):
    name = 'time_slot_' + str(i)
    col.append(name)

for i in range(28):
    name = 'time_slot_' + str(i)
    col_name.append(name)

X_train = data[col]
test_data = pd.read_csv(Folder_Path + '\\' + '34week_46-75.csv')
X_test = test_data[col]
Path = r'D:\kaggle'
data = pd.read_csv(Path + '\\' + 'label.csv')
Y_train = data[col_name]

#let result be float type
answer = pd.read_csv(Path + '\\' + 'sample.csv',index_col='user_id',dtype = {'time_slot_0': float,'time_slot_1': float,
                                                                             'time_slot_2': float,'time_slot_3': float,
                                                                             'time_slot_4': float,'time_slot_5': float,
                                                                             'time_slot_6': float,'time_slot_7': float,
                                                                             'time_slot_8': float,'time_slot_9': float,
                                                                             'time_slot_10': float,'time_slot_11': float,
                                                                             'time_slot_12': float,'time_slot_13': float,
                                                                             'time_slot_14': float,'time_slot_15': float,
                                                                             'time_slot_16': float,'time_slot_17': float,
                                                                             'time_slot_18': float,'time_slot_19': float,
                                                                             'time_slot_20': float,'time_slot_21': float,
                                                                             'time_slot_22': float,'time_slot_23': float,
                                                                             'time_slot_24': float,'time_slot_25': float,
                                                                             'time_slot_26': float,'time_slot_27': float})

model = Sequential()
model.add(Dense(28, input_dim=924, activation='relu'))
model.add(Dropout(0.25))
model.add(Dense(28, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(28, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam')

print("train start")
model.fit(X_train, Y_train, epochs=32, verbose=0)

print("test start")
result = model.predict_proba(X_test)

for i in range(28):
    name = 'time_slot_' + str(i)
    for j in range(len(result)):
        answer.at[first+j,name] = result[j][i]

Folder_Path = r'D:\kaggle\data'
answer.to_csv(Folder_Path+'\\'+'result.csv',encoding="utf_8_sig",index = True)
