'''
اكتب دالة لتمرير اسم شخص والترحيب به
use arguments / parameters
'''


def welcome(name1, name2):
    print('hello', name1, name2)


welcome('ahmed', 'ali')
print('done')
welcome('ali', 'ahmed')
first_name = input('what is your first name: ')
last_name = input('what is your last name: ')
welcome(first_name, last_name)
