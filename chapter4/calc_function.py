'''
اكتب برنامج لمحاكاة الالة الحاسبة
بحيث تجري عمليات الجمع والضرب والقسمة والطرح على رقمين عشرريين
ملاحظة : يتوجب عليك استخدام الدوال للعمليات الحسابية والادخال
'''

'''
فوائد الدوال:
1 اعادة استخدام الكود
2 تبسيط وتنظيم الكود
'''


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mult(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


def calc(n1, op, n2):
    if op == '+':
        return add(n1, n2)
    elif op == '-':
        return sub(n1, n2)
    elif op == '*':
        return mult(n1, n2)
    elif op == '/':
        return div(n1, n2)
    else:
        return 'unsupported operator'


n1 = float(input('enter n1: '))
op = input('enter operator: ')
n2 = float(input('enter n2: '))
print(calc(n1, op, n2))
print(calc(7, '+', 12))
print(calc(7, '*', 3))
print(calc(1.5, '*', 3))
r = calc(1.4, '+', 0.1)
z = r + 10
print(z)
