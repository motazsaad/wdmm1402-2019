'''
اكتب دالة لادخال عدد من الارقام وطباعة المجموع
ملاحظة: المستخدم سيقوم بادخل عدد الارقام وقيم الارقام
'''


def sum_numbers():
    number_of_values = int(input('enter number of values: '))
    total = 0
    for i in range(number_of_values):
        v = int(input('enter value: '))
        total = total + v
    print('total', total)


sum_numbers()
