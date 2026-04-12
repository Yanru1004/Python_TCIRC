#a003. 提款卡密碼

while True:
    try:
        text = input()
        pre_text = None
        pw = ''
        for s in text:
            if pre_text == None:
                pre_text = s
            else:
                pw += str(abs(ord(pre_text)-ord(s)))
                pre_text = s

        print(pw)
        
    except:
        break