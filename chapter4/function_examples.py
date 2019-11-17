'''
اكتب دالة تأخذ رقم وتقوم بإراجاع القيمة المطلقة للرقم
'''


def myabs(num):
    if num >= 0:
        return num
    else:  # negative
        return num * -1


print(myabs(3))
print(myabs(3.7))
print(myabs(-19))
print(myabs(-2.9))
# n = float(input('enter a number'))
# print(myabs(n))
# input and call in the same line
print(myabs(float(input('enter a number: '))))
