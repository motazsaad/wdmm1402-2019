'''
اكتب برنامج لعد الكلمات بالاحرف الكبيرة
'''

my_str = input('enter a string: ')
words = my_str.split()
count = 0
for word in words:
    if word.isupper():
        count += 1
print(count)
