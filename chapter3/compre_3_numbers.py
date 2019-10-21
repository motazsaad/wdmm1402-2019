'''
اكتب برنامج لادخال 3 ارقام وطبعة الرقم الاكبر منهم
'''
x = int(input('plz enter x: '))
y = int(input('plz enter y: '))
z = int(input('plz enter z: '))
if x >= y and x >= z:
    print(x)
elif y >= x and y >= z:
    print(y)
elif z >= x and z >= y:
    print(z)
