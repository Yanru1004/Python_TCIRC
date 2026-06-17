#b029 爺爺口袋的紙條

#讀入筆數及長度

n,k = map(int,input().split())

for i in range(n):
    
    list_1 = sorted(map(int,input().split()))
    list_2 = sorted(map(int,input().split()))
    
    result = sum([list_1[x]*list_2[x] for x in range(k)])

    print(result)