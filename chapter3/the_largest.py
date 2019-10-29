'''
اكتب برنامج لادخال 3 ارقام وطباعة الاكبر منها
'''
x = int(input('plz enter x: '))
y = int(input('plz enter y: '))
z = int(input('plz enter z: '))
# 3 2 1
# 4 1 3
if x >= y and x >= z:
    print(x)
elif y >= x and y >= z:
    print(y)
else:  # z >= x and z >= y:
    print(z)
