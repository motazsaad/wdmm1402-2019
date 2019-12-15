'''
اكتب برنامج لازالة كل الارقام من نص
'''

my_str = input('enter a string: ')
words = my_str.split()
result = ''
for word in words:
    if word.isalpha():
        result += word + ' '
        # print(result)
print(result)
