#b051 金字塔

brick = int(input())

n = 1

while brick >= n:
    brick -= n
    n += 1

print(n-1)