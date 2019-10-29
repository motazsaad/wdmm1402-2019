def sum_2numbers(n1, n2):  # n1, n2 : arguments / parameters
    print(n1 + n2)


def welcome():
    name = input('what is your name? ')
    print('hello', name)


def greeting(name):
    print('hello', name)


welcome()
greeting('Ali')
greeting('Sameer')
name = input('please enter your name: ')
greeting(name)

print()
print('hello')  # argument
sum_2numbers(3, 4)
x = int(input('enter x: '))
y = int(input('enter y: '))
sum_2numbers(x, y)
