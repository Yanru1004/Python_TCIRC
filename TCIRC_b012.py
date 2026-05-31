#b012 不及格的危機

#讀取 考試成績及次數

x,y,z = map(int,input().strip().split(' '))

score = ((x*y)+z)/(x+1)

if score >= 60:
    print('PASS')
else:
    print('FAIL')
    