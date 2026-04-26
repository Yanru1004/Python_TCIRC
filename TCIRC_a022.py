#a022 上學去吧！

#取得現在時間

h,m = list(map(int,input().split(' ')))

if  (7*60+30) <= h*60+m < (17*60):
    print('At School')

else:
    print('Off School')