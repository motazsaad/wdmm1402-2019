'''
اكتب دالة تمرر لها اسم الشخص وكود لغته
وتقوم بإرجاع ترحيب بلغته
'''


def greeting(name, lang_code):
    if lang_code == 'ar':
        return 'مرحبا ' + name
    elif lang_code == 'en':
        return 'hello ' + name
    elif lang_code == 'fr':
        return 'bonjour ' + name
    else:
        return 'hello ' + name


print(greeting(input('name: '), input('lang: ')))
