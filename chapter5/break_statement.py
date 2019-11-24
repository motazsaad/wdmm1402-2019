while True:  # indefinite
    line = input('> ')
    if line[0] == '#' or line[0] == ' ':
        continue  # go to line 1
    if line == 'done' or line == 'end':
        break  # to to line 8
    print(line)
print('done')

# infinite
while True:
    print('hello')
