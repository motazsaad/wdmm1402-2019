'''
اكتب برنامج لايجاد اكبر رقم في قائمة
'''

l1 = [9, 41, 12, 3, 74, 15, -103, 340, 7, 54790, 13]
# step 1: define a variable with initial value
largest_so_far = l1[0]
# step 2: enter loop
for num in l1:
    if num > largest_so_far:
        largest_so_far = num
# step 3: print result
print('largest:', largest_so_far)
