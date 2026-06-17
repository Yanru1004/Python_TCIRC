#b030 健康檢查（Ⅰ）

#讀入測資

li = input().split()

result_1=[]
result_2=[]

for s in li:

    if s == '*':
        break
    elif s.isnumeric():
        result_1.append(s)
    
    elif s.isalpha():
        result_2.append(s)
    else:
        print('error')

if len(result_1) >= len(result_2):
    ans = result_1
elif len(result_1) < len(result_2):
    ans = result_2
else:
    print('error')

print(' '.join(ans))

