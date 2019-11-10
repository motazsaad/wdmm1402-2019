'''
اكتب برنامج لادخال عدد الارقام المطلوب ادخالها
 ومن ثم طباعة المجموع
'''


def calc_payment(input_num):
    total = 0
    for i in range(input_number):
        number = int(input('plz enter number: '))
        total = total + number
    return total


input_number = int(input('enter number of entries: '))
total = calc_payment(input_number)
print('you must pay (before discount): ', total)
discount = float(input('enter discount: '))
total = total - total * discount
print('you must pay (after discount): ', total)
