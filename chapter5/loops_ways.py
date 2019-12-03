l1 = [3, 6, 8, 90, 12, 43, 20, 100, 65, 23, 98, 12, 1, 89, 65]

# method 1: using iteration variable
for number in l1:
    print(number)

print(l1)
print(*l1)

print('--------------------------')
# method 2: using index
for i in range(len(l1)):
    print('index:', i, 'value:', l1[i])

print(l1)
print(*l1)
