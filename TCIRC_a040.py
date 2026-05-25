#a040 文文的求婚

#讀取年份範圍

a,b = list(map(int,input().split(' ')))

count = 0

for year in range(a,b+1):
    if year %4 == 0 and year%100 != 0 or year%400 == 0:
        count += 1

print(count)

