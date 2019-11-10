'''

اكتب برنامج لادخال عدد المدخلات وجمع هذه المدخلات
'''


def calc_payment(num_entry):
    total = 0
    for i in range(num_entry):
        number = int(input('enter price: '))
        total = total + number
    return total


num_entry = int(input('enter # of entries: '))
total = calc_payment(num_entry)
print('payment before discount:', total)
discount = float(input('enter discount: '))
total = total - total * discount
print('payment after discount:', total)
