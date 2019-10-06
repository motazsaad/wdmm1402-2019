'''
اكتب برنامج لطباعة مرحبا 7 مرات
عند المرة الاخيرة اطبع مع السلامة
عند المرة الاولى اطبع اهلا وسهلا
'''
for i in range(7):
    if i == 0:
        print('welcome')
    print(i, 'hello')
    if i == 6:
        print('goodbye')

# i = 0
# while i < 7:
#     print('hello')
#     i = i + 1
