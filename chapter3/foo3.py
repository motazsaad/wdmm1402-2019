'''
اكتب برنامج لعمل آلة حاسبة
المطلوب ادخار رقمين مع العملية (جمع أو طرح  + -  )
وطباعة الناتج

طور البرنامج باضافة عمليات الضرب والقسمة

'''
try:
    num1 = float(input('enter the 1st num: '))
    op = input('enter operator (+ or -) : ')
    num2 = float(input('enter the 2nd num: '))
    if op == '+':
        print(num1 + num2)
    elif op == '-':
        print(num1 - num2)
    elif op == '*':
        print(num1 * num2)
    elif op == '/':
        print(num1 / num2)
    else:
        print('operator not supported')
except ValueError:
    print('input must be numeric')
except ZeroDivisionError:
    print('can not divide by zero')
