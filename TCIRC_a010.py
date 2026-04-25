#a010 聖經密碼

while True:

    #讀取單字數及密碼間距數
    n,m = map(int,input().split(' '))

    if n==0 and m ==0:
        break

    #組合字串
    text_list = []

    for i in range(n):
        text_list.append(input())
    text = ''.join(text_list)    
    
    #解碼
    code = []
    code_index = list(map(int,input().split(' ')))
    
    for i in range(m):        
        code.append(text[code_index[i]-1])
    print(''.join(code))    
    
