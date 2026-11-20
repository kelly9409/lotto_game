import pandas as pd
""" 
df = pd.read_csv('lotto.csv', encoding='utf-8-sig')
print(df.shape)            # (행 수, 열 수)
print(df.head(3))          # 처음 3줄
print(df['당첨번호1'].head(5).tolist())
"""

votes = ['짜장', '짬뽕', '짜장', '볶음밥', '짜장', '짬뽕']
 
count = {}
for menu in ['짜장', '짬뽕', '볶음밥']:
    count[menu] = 0           # ① 0으로 준비
for v in votes:
    count[v] += 1             # ② 나올 때마다 +1
 
print(count)
print(count['짜장'], sum(count.values()))
