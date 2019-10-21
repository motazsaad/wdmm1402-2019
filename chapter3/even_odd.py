'''
اكتب برنامج لطباعة الارقام الفردية والزوجية من 1 الى 10
'''
for n in range(1, 11):
    if n % 2 == 0:
        print(n, 'even')
    else:
        print(n, 'odd')
