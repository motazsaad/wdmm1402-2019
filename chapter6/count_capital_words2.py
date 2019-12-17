'''
اكتب برنامج لعد الكلمات التي تبدأ بحرف كبير
'''

my_str = input('enter a string: ')
words = my_str.split()
count = 0
for word in words:
    if word[0].isupper():
        count += 1
print(count)
