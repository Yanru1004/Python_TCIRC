#b027 找出學霸

n,*score = map(int,input().split())

result = [-1,-1,-1,101]

for i in range(n):
    if score[i] > result[1]:
        result[:2] = i+1,score[i]
    
    if score[i] < result[3]:
        result[2:] = i+1,score[i]


print(' '.join(map(str,result)))
