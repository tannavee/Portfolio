a = [10, 2, 5, 4, 100]
b = [5, 10, 20, 20, 25]
normList = []

for i in range(len(a)):
        normList.append((a[i]/b[i]) * 100)

print(normList)
