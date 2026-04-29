#a039 小明的作業

#讀取三邊長並排序。

score = 0

for i in range(5):
    a,b,c = sorted(list(map(int,input().split(' '))))
    
    if a+ b > c:
        score += 1
print(score)