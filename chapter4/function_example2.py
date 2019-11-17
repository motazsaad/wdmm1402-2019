'''
اكتب دالة تمرر لها كود اللغة وتقوم بطباعة ترحيب بتلك اللغة
اللغات المطلوبة
ar مرحبا
en hello
fr bonjour
es hola
tr merhaba
ru priviat
اذا اللغة لم تكن موجودة ، اطبع ترحيب بالانجليزية
'''


def greeting(lang_code):
    if lang_code == 'ar':
        print('مرحبا')
    elif lang_code == 'fr':
        print('bonjour')
    elif lang_code == 'es':
        print('hola')
    elif lang_code == 'tr':
        print('merhaba')
    elif lang_code == 'en':
        print('hello')
    elif lang_code == 'ru':
        print('priviat')
    else:
        print('your language is not supported, so hello')


greeting(input('enter lang code: '))
