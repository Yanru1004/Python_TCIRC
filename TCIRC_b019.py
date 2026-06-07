#b019 寶可夢道館

#讀入對戰資訊

h,m,n = map(int,input().split())

if m > n: #傷害大於回復
    #第一回合
    turn = 1
    h -= m
    while h >0:
        #回復
        h += n
        #新回合
        turn += 1
        h -= m
    print(turn)

elif (m == n or m < n) and (h > m):
    print('lose')

elif (h < m):
    print('1')

else:
    print('error')
    