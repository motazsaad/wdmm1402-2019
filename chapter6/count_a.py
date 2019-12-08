'''
اكتب برنامج لادخل نص، وعد عدد مرات تكرار الحرف a
'''
my_str = input('enter a string: ')
count_a = 0
for ch in my_str:
    if ch is 'a':
        count_a += 1
print(count_a)
