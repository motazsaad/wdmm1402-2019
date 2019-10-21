'''
اكتب برنامج لاجراء العمليات الحسابية (آلة حاسبة) باستخدام دالة eval
'''
try:
    result = eval(input('plz enter an expression: '))
    print('result:', result)
except ZeroDivisionError:
    print('can not divide by zero')
except Exception:
    print('unsupported operation')
