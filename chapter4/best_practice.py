'''
اكتب دالة لتمرير رقمين وارجاع المجموع
write a function to take two number arguments
 and return the sum
'''


# bad practice: use input and print inside the function
def sum_v1():
    a = int(input('enter a: '))
    b = int(input('enter b: '))
    print(a + b)


# sum_v1()

# best practice: pass arguments and return result
def sum_v2(a, b):
    return (a + b)


r = sum_v2(3, 5)
print('result:', r)
print('result + 1:', r + 1)
