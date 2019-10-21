'''
اكتب برنامج لادخال رقمين وطباعة اذا ما كان
الرقم الاول اكبر من الرقم الثاني أو اصغر أو يساويه
'''
x = int(input('plz enter x: '))
y = int(input('plz enter y: '))

if x > y:
    print('x is bigger than y')
elif x < y:
    print('x is smaller than y')
else:
    print('x is equal to y')
