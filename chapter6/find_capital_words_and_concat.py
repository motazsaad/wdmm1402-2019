'''
اكتب برنامج لايجاد الكلمات التي تبدأ بحرف كبير وقم باضافة # قبل هذه الكلمة
'''

my_str = input('enter a string: ')
words = my_str.split()
result = ''
for word in words:
    if word[0].isupper():
        result += '#' + word + ' '
    else:
        result += word + ' '
print(result)
