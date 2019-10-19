'''
اكتب برنامج لادخال رقمين x & y عمل التالي
في حال كان x اكبر، طباعة x اكبر من y
x is bigger than y
في حال كان y اكبر، طباعة y اكبر من x
y is bigger than x
في حال كان الرقمين متساوين اطبع x تساوي y
x is equal to y
'''
x = int(input('enter x: '))
y = int(input('enter y: '))
if x > y:
    print('x is bigger than y')
elif y > x:
    print('y is bigger than x')
else:
    print('x is equal to y')
