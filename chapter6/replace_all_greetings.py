'''
اكتب برنامج لازالة جميع الكلمات الترحيبية من نص
الكلمات الترحيبية hello hi welcome
'''
my_str = input('enter a string: ')
print('solution 1')
result = my_str.replace('hi', '').strip()
result = result.replace('hello', '').strip()
result = result.replace('welcome', '').strip()
print(result)

print('--------------------')
print('solution 2')
words = my_str.split()
result = ''
for word in words:
    if word == 'hi' or word == 'hello' or word == 'welcome':
        continue
    else:
        result += word + ' '
        # print(result)
print(result)
