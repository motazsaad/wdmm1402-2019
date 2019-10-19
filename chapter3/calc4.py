print('welcome to my calculator')
try:
    num1 = float(input('enter 1st num: '))
    op = input('enter operator: ')
    num2 = float(input('enter 2nd num: '))
    if op == '+':
        print(num1 + num2)
    elif op == '-':
        print(num1 - num2)
    elif op == '*':
        print(num1 * num2)
    elif op == '/':
        print(num1 / num2)
    elif op == '**':
        print(num1 ** num2)
    else:
        print('operator not supported')
except ValueError:
    print('input must be numeric')
except ZeroDivisionError:
    print('can not divide by zero')
print('goodbye :) have a nice day')
