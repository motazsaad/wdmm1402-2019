'''
اكتب دالة لتمرير 3 ارقام وطباعة الرقم الاكبر
باستخدام المعاملات with arguments
'''


def largest(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        print(n1)
    elif n2 >= n1 and n2 >= n3:
        print(n2)
    else:
        print(n3)


largest(3, 5, 9)
x = 3
y = 10
z = x - y
largest(x, y, z)
a = int(input('enter a: '))
b = int(input('enter b: '))
c = int(input('enter c: '))
largest(a, b, c)
