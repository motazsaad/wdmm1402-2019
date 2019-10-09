'''
اكتب برنامج لادخال رقمين بالاضافة للعملية الحاسبية
+ - * /
(اربع عمليات حسابية)
ومن ثم طباعة الناتج
'''
try:
    number1 = float(input('plz enter 1st number: '))
    op = input('plz enter operator: ')
    number2 = float(input('plz enter 2nd number: '))
    if op == '+':
        print(number1 + number2)
    elif op == '-':
        print(number1 - number2)
    elif op == '*':
        print(number1 * number2)
    elif op == '/':
        print(number1 / number2)
    else:
        print('operator not supported')
except ValueError:
    print('input must be numeric')
except ZeroDivisionError:
    print('can not divide by zero')
