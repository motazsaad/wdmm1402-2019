'''
اكتب برنامج لجمع الارقام التي اكبر من 20 في قائمة
'''

l1 = [3, 6, 8, 90, 12, 43, 7, 65, 23, 98, 89, 65]
total = 0
for num in l1:
    if num > 20:
        total = total + num
print('total', total)
