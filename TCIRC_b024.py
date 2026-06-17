#b024 貪睡的鬧鐘

#讀取開始及結束時間

start,end = map(int,input().split())

t = (start//100)*60 + start % 100

end_t = (end//100)*60 + end % 100

while t < end_t:

    print(f'{t//60:02d}{t%60:02d}')
    
    t+= 5

print(f'{end:04d}')
