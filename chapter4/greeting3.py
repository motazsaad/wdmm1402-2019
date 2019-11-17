'''
اكتب دالة تأخذ اسم الشخص ولغته
وتقوم بارجاع رسالة ترحيبية باسمه
اللغات المدعومة فقط العربية والفرنسية و الانجليزية
اذا اللغة المدخلة غير مدعومة يرجع رسالة ترحيبية بالانجليزية
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


print(greeting(input('your name: '), input('enter lang code: ')))
print(greeting('Ali', 'fr'))
