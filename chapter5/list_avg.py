'''
اكتب برنامج لايجاد متوسط قائمة
'''
l1 = [3, 6, 8, 90, 12, 43, 7, 65]
count = 0
total = 0
for num in l1:
    count = count + 1
    total = total + num
print(total / count)
