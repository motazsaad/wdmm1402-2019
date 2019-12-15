'''
اكتب برنامج لايجاد وطباعة كل الارقام في نص معين
'''

s = input('enter a string: ')
words = s.split()
print(words)
for word in words:
    if word.isnumeric():
        print(word)
