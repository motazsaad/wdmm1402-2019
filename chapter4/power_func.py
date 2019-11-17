'''
اكتب دالة تمرر لها رقمين
وتقوم بإرجاع الرقم الاول مرفوع للقوى للرقم الثاني
'''


def mypower(x, y):
    return x ** y


print(mypower(2, 3))
print(mypower(3, 2))
print(mypower(3, 3))
print(mypower(int(input('enter x: ')), int(input('enter y: '))))
a = int(input('enter a: '))
b = int(input('enter b: '))
print(mypower(a, b))
