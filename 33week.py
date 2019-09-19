import numpy as np
import pandas as pd
from datetime import datetime

def time_slot(date, hour,weekday):
    if weekday == 1:
        if ('0000' <= hour < '0100'):
            return 29  # week need -1
        elif ('0100' <= hour < '0900'):
            return 2
        elif ('0900' <= hour < '1700'):
            return 3
        elif ('1700' <= hour < '2100'):
            return 4
        elif ('2100' <= hour < '2400'):
            return 5
    elif weekday == 2:  # tuesday
        if ('0000' <= hour < '0100'):
            return 5
        elif ('0100' <= hour < '0900'):
            return 6
        elif ('0900' <= hour < '1700'):
            return 7
        elif ('1700' <= hour < '2100'):
            return 8
        elif ('2100' <= hour < '2400'):
            return 9
    elif weekday == 3:
        if ('0000' <= hour < '0100'):
            return 9
        elif ('0100' <= hour < '0900'):
            return 10
        elif ('0900' <= hour < '1700'):
            return 11
        elif ('1700' <= hour < '2100'):
            return 12
        elif ('2100' <= hour < '2400'):
            return 13
    elif weekday == 4:
        if ('0000' <= hour < '0100'):
            return 13
        elif ('0100' <= hour < '0900'):
            return 14
        elif ('0900' <= hour < '1700'):
            return 15
        elif ('1700' <= hour < '2100'):
            return 16
        elif ('2100' <= hour < '2400'):
            return 17
    elif weekday == 5:
        if ('0000' <= hour < '0100'):
            return 17
        elif ('0100' <= hour < '0900'):
            return 18
        elif ('0900' <= hour < '1700'):
            return 19
        elif ('1700' <= hour < '2100'):
            return 20
        elif ('2100' <= hour < '2400'):
            return 21
    elif weekday == 6:
        if ('0000' <= hour < '0100'):
            return 21
        elif ('0100' <= hour < '0900'):
            return 22
        elif ('0900' <= hour < '1700'):
            return 23
        elif ('1700' <= hour < '2100'):
            return 24
        elif ('2100' <= hour < '2400'):
            return 25
    elif weekday == 7:
        if ('0000' <= hour < '0100'):
            return 25
        elif ('0100' <= hour < '0900'):
            return 26
        elif ('0900' <= hour < '1700'):
            return 27
        elif ('1700' <= hour < '2100'):
            return 28
        elif ('2100' <= hour < '2400'):
            return 29

Folder_Path = r'D:\kaggle\public'
data = pd.read_csv(Folder_Path + '\\' + 'data-069.csv')
first = 86371  # first user id
last = 87619  # last user id
result = np.zeros(
    (33 * (last - first + 1), 30))  # 33*user(last_user_id- first_user_id+1), user_id, week, and 28 time_slot

col = ['user_id', 'week']
for i in range(28):
    name = 'time_slot_' + str(i)
    col.append(name)

i = 1
user_id = first
for j in range(len(result)):
    result[j][1] = i - 1
    result[j][0] = user_id
    i = i + 1
    if i % 34 == 0:
        i = 1
        user_id = user_id + 1

for i in range(len(data)):
    event = data.at[i, 'event_time']
    event_time = event[11:13] + event[14:16]
    day = datetime(int(event[0:4]), int(event[5:7]), int(event[8:10]), int(event[11:13]), int(event[14:16]), int(event[17:19]))
    year, week, weekday = day.isocalendar()  # in order to know date in which week
    user_id = data.at[i, 'user_id']
    position = int(user_id) - first  # minus first user id

    if (week == 33) | (week == 34):  # 2017/08/14 01:00:00 - 2017/08/21 01:00:00 doesn't count
        continue
    if week == 52:  # 2017/01/01 would be the 52th week in 2016
        week = 0
    slot = time_slot(day, event_time, weekday)
    if slot == 29:
        week -= 1
    result[position * 33 + week][slot] = 1

file = pd.DataFrame(columns=col, data=result, dtype=int)
Folder_Path = r'D:\kaggle\data924'
file.to_csv(Folder_Path + '\\' + 'data-69.csv', index=False)