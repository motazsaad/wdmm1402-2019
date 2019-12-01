'''
اكتب برنامج لعد الارقام التي اكبر من 20 في قائمة
وكذلك عدد الارقام التي اقل من عشرين
وكذلك عدد الارقام التي تساوي عشرين
وعدد العناصر ككل في القائمة
'''

l1 = [3, 6, 8, 90, 12, 43, 20, 65, 23, 98, 89, 65]
count_larger_20 = 0
count_smaller_20 = 0
count_20 = 0
count = 0
for number in l1:
    count += 1
    if number > 20:
        # count_larger_20  = count_larger_20 + 1
        count_larger_20 += 1
    elif number < 20:
        count_smaller_20 += 1
    else:
        count_20 += 1
print('count larger 20:', count_larger_20)
print('count smaller 20:', count_smaller_20)
print('count 20:', count_20)
print('all count:', count)
print('all count:', count_smaller_20 + count_20 + count_larger_20)
