#a005. 獨角蟲進化計算器

#讀入糖果及獨角蟲數量

kakuna = 0
candy,weedle = list(map(int,input().split(' ')))

while candy >= 12 or weedle > 0:
    if candy >= 12 and weedle >0:

        #進化1隻獨角蟲
        candy -= 12
        weedle -= 1
        kakuna += 1

        #進化及傳送鐵殼蛹獎勵
        candy += 2
    
    elif candy <12 and weedle >0:
        #傳送獨角蟲換糖果
        weedle -= 1
        candy += 1
    
    else:
        break

print(kakuna)
