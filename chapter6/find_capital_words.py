'''
اكتب برنامج لايجاد الكلمات التي تبدأ بحرف كبير
'''

my_str = input('enter a string: ')
words = my_str.split()
for word in words:
    if word[0].isupper():
        print(word)
