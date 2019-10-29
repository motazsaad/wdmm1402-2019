'''
اكتب دالة لادخال 3 ارقام وطباعة الاكبر
بدون معاملات
'''


def largest():
    n1 = int(input('enter n1: '))
    n2 = int(input('enter n2: '))
    n3 = int(input('enter n3: '))
    if n1 >= n2 and n1 >= n3:
        print(n1)
    elif n2 >= n1 and n2 >= n3:
        print(n2)
    else:
        print(n3)


largest()
largest()
largest()
