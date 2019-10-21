'''
اكتب برنامج لطباعة الارقام الفردية من صفر الى 10
'''

for i in range(10):
    print(i, 'result of mod', i % 2)
    if i % 2 != 0:  # odd
        print('odd number:', i)
