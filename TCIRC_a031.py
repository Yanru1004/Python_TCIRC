#a031 山六九之旅

age = int(input())

price = 590*(age>=6) + 200*(age>=12) + 100*(age>=18)-491*(age>=60)

print(price)