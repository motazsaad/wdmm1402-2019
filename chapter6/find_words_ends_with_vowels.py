'''
اكتب برنامج لايجاد الكلمات التي تنتهي بحرف متحرك
a e i o u
'''

my_str = input('enter a string: ')
words = my_str.split()
print('solution 1')
vowels = 'aeiou'
for word in words:
    if word[-1] in vowels:
        print(word)

print('-----------------------')
print('solution 2')
for word in words:
    if word.endswith('a') or word.endswith('e') or word.endswith('i') or word.endswith('o') or word.endswith('u'):
        print(word)

print('-----------------------')
print('solution 2')
for word in words:
    if word[-1] == 'a' or word[-1] == 'e' or word[-1] == 'i' or word[-1] == 'o' or word[-1] == 'u':
        print(word)
