'''
اكتب برنامج لعد المسافات في نص
المطلوب الحل بطريقتين
'''

my_str = input('enter a string: ')
print('solution 1')
count = 0
for ch in my_str:
    if ch.isspace():  # if ch == ' ':
        count += 1
print(count)
print('----------------------------')
print('solution 2')
print(my_str.count(' '))
