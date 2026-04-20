#a009. 沒有手機的下課時間(猜數字)

#讀入答案
answers = input()

#猜測次數
guess_n = int(input())

#判斷函式
def check_ans(answers,guess):
    a,b = 0,0

    for i in range(4):
        if guess[i] == answers[i]:
            a += 1

        elif guess[i] in answers:
            b += 1
    return f'{a}A{b}B'

#判斷開始
for i in range(guess_n):
    guess = input()

    print(check_ans(answers,guess))
    
