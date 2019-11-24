black_list = ['hazem', 'khalid', 'bilal', 'emad']
for name in black_list:
    if name == 'khalid':
        print(name, 'be good')
    else:
        print(name, 'you are in the black list')

print('-------------------------------')
for i in range(len(black_list)):
    if i == 1:
        print(black_list[i], 'be good')
    else:
        print(black_list[i], 'you are in the black list')
