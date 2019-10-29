'''
اكتب دالة لتمرير 3 ارقام وطباعة الاكبر
باستخدام المعاملات
'''


def get_largest(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        print(n1)
    elif n2 >= n1 and n2 >= n3:
        print(n2)
    else:
        print(n3)


get_largest(3, 7, 2)  # result 7
get_largest(int(input('n1: ')),
            int(input('n2: ')),
            int(input('n3: ')))
x = int(input('x: '))
y = int(input('y: '))
z = int(input('z: '))
get_largest(x, y, z)
get_largest(n1=12, n2=7, n3=12)
