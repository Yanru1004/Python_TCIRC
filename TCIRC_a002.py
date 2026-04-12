#a002. 電話客服中心

#產生字母對照字典
letter = [10,11,12,13,14,15,16,17,34,18,19,20,21,22,35,23,24,25,26,27,28,29,32,30,31,33]
letter_num = dict()
for i in range(26):
    check = ((letter[i] //10) + (letter[i]%10)*9)%10
    letter_num.setdefault(check,'')
    letter_num[check] += chr(65+i)

#驗證開始
while True:
    try:
        data = input()
        calc_sum = 0
        for i in range(8):
            calc_sum += int(data[i]) * (8-i)
        
        code = (10-(calc_sum + int(data[8]))%10)%10
        
        print(letter_num[code])

    except:
        break