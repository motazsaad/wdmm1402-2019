'''
اكتب دالة لتمرير 3 ارقام وارجاع المتوسط
'''


def average(n1, n2, n3):
    return (n1 + n2 + n3) / 3


r = average(n1=3, n2=7, n3=10)
print('result:', r)
print('avg:', average(n1=15, n2=20, n3=25))
x = int(input('x: '))
y = int(input('y: '))
z = int(input('z: '))
print('avg:', average(n1=x, n2=y, n3=y))
