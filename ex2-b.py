nb = [14,27,39,40,26,3984,284,20,5789,49]

max = nb[0]
min = nb[0]
moy = 0

for i in nb:
    if i > max:
        max = i
    if i < min:
        min = i

j = 0
i = 0
for x in nb:
    j += x
    i += 1
moy = j / i

print("Le maximum est :", max)
print("Le minimum est :", min)
print("La moyenne est :", moy)