# Data-Science-Kaggle-competition
## Kaggle competition link：
* https://www.kaggle.com/c/ncu-course-game

## 程式說明
* 按照資料原本的user event time，判斷event_time是在哪一週的哪個time_slot發生的，總共有924個time_slot，如果該時段有發生事件，就將值設成1，把處理過後的data-001~data-045合成一個大檔案，當作X_train，處理過後的data-046~data-075合成另外一個檔案當作X_test，Y_train則是label-001~label-045，再將資料丟進model做訓練得出結果。嘗試過使用logistic regression，這樣訓練出來的結果是0.86左右，並且每次出來的結果都一樣，後來使用sequential model，然後有用Dropout，每次的測試結果都不一樣，結果介在0.85-0.87之間。
* 33week：判斷event_time發生在第幾周的第幾個time_slot，每個user有0~32週，每週28個slot，需要自己手動改檔名，還有第一個user_id跟最後一個user_id
* 924column：把33week處理完的資料轉成一個user一行共924個time_slot的形式
* sequential_model：用處理完的資料丟進sequential model訓練得出結果
