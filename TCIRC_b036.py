#b036 物種豐富度

area_A = set()
area_B = set()

while (s := input()) != '0':
    area_A.add(s)

while (s := input()) != '0':
    area_B.add(s)

if len(area_A) > len(area_B):
    print("A")
elif len(area_A) < len(area_B):
    print("B")
else:
    print("Equal")