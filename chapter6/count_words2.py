'''
اكتب برنامج لطباعة الكلمات التي تبدأ بحرف  k و تنتهي ب e
'''

words = ['mug', 'maher', 'mango', 'apple', 'kanari',
         'book', 'pen', 'kate', 'laptop', 'Marcus']
print('solution 1')
for word in words:
    if word.startswith('k') and word.endswith('e'):
        print(word)
print('-------------')
print('solution 2')
for word in words:
    if word[0] is 'k' and word[-1] is 'e':
        print(word)
