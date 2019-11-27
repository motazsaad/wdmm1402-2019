'''
اكتب برنامج لايجاد اصغر رقم في قائمة
اعتبر اسم القائمة لديك l1
'''

l1 = [9, 41, 12, 3, 74, 15, -103, -340, 7, 54790, 13]
# step 1: define a variable with initial value
smallest_so_far = l1[0]
# step 2: enter loop
for num in l1:
    if num < smallest_so_far:
        smallest_so_far = num
# step 3: print result
# print('smallest:', smallest_so_far)
print(smallest_so_far)
