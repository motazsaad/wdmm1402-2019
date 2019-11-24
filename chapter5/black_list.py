black_list = ['Mohannad', 'Ahmed', 'Hazem', 'Salah', 'Bashar']
for name in black_list:
    if name == 'Ahmed':
        print(name, 'be good')
    else:
        print(name, 'you are in the black list')

print('------------------------------')
for i in range(len(black_list)):
    print(i, black_list[i])
