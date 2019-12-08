'''
اكتب برنامج لادخل نص والحرف المراد عده
ومن ثم طباعة تكرار هذا الحرف
'''
my_str = input('enter a string: ')
letter = input('enter a letter: ')
count = 0
for ch in my_str:
    if ch is letter:
        count += 1
print(count)
