'''
اكتب برنامج لاخال كلمتين وطباعة الكلمتين حسب الترتيب الابجدي
'''

word1 = input('enter a word: ')
word2 = input('enter a word: ')

if word1 > word2:
    print(word2, word1)
elif word1 < word2:
    print(word1, word2)
else:
    print(word1, '=', word2)
