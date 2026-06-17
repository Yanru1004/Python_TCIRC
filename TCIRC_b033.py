#b033 晚餐ㄘ什麼？？

#讀取選項數

n,m = map(int,input().split())

set_n,set_m = set(),set()

#存入清單
for i in range(n):
    set_n.add(input())

for i in range(m):
    set_m.add(input())

#取交集

result = sorted(list(set_n.intersection(set_m)))
print(len(result))
print('\n'.join(result))