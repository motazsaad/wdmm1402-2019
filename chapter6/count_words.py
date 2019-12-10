'''
اكتب برنامج لطباعة الكلمات التي تبدأ بحرف   m او M
'''

words = ['mug', 'maher', 'mango', 'apple', 'kanari',
         'book', 'pen', 'laptop', 'Marcus']
print('solution 1')
for word in words:
    if word.startswith('m') or word.startswith('M'):
        print(word)
print('--------------------')
print('solution 2')
for word in words:
    if word.lower().startswith('m'):
        print(word)
