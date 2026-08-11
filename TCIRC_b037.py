#b037 破譯密碼

count = {}
text = (input().lower())

for s in text:
    if ord('a') <= ord(s) <= ord('z'):
        count.setdefault(s,0)
        count[s] += 1
    else:
        pass

for i in range(ord('a'),ord('z')+1):
    if chr(i) in count:
        print(f"'{chr(i)}': {count[chr(i)]}")