my_str = input('enter a string: ')

print('loop on letters:')
for ch in my_str:
    print(ch)

print('--------------------------')
print('loop on words:')
for word in my_str.split():
    print(word)
