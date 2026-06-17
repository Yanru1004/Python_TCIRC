#b022 質數惡夢

#讀取正整數

M = int(input())

#創建串列
prime_number = [True for n in range(M+1)]

prime_number[0] = False
prime_number[1] = False

#清除除了2以外的偶數
for i in range(4,M+1,2):
    prime_number[i] = False

i = 3

while i*i <= M:
    #已確認質數
    if prime_number[i] == True:
        
        #清除i的倍數
        for n in range(i*i,M+1,i*2):            
            prime_number[n] = False
    i += 2

#輸出
result =[]
if prime_number[2]==True:
    result.append('2')

for pn in range(3,M+1,2):
    if prime_number[pn] == True:
         result.append(str(pn))

print(' '.join(result))
    

