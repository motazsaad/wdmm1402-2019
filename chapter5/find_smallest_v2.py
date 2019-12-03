'''
اكتب برنامج لايجاد اصغر رقم في قائمة
'''
l1 = [3, 6, 8, 90, 12, 43, 20, 100, 65, 23, 98, 12, 1, 89, 65]
smallest = None
for number in l1:
    if smallest is None:  # true in 1st iteration
        smallest = number
    if number < smallest:
        smallest = number
print(smallest)

smallest = l1[0]
for number in l1:
    if number < smallest:
        smallest = number
print(smallest)