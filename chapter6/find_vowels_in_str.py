'''
اكتب برنامج لعد الاحرف المتحركة في نص
a e i o u
'''

my_str = input('enter a string: ')
vowels = 'aeiou'
count = 0
for letter in my_str:
    if letter.lower() in vowels:
        count += 1
print(count)
