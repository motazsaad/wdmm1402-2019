'''
اكتب برنامج لادخال رقم
وطباعة اذا ما كان الرقم موجب أو سالب أو صفر
'''

num = int(input('please enter a number: '))
if num > 0:
    print('positive')
elif num < 0:
    print('negative')
else:
    print('equal to zero')
