'''
اكتب دالة تأخذ نص وتقوم بتبديل الكلمات باحرف كبيرة (كل الاحرف) لتصبح صغيرة والعكس
'''


def switch_case(my_str):
    result = ''
    words = my_str.split()
    for word in words:
        if word.isupper():
            result += word.lower() + ' '
        elif word.islower():
            result += word.upper() + ' '
        else:
            result += word + ' '
    return result


print(switch_case('hello AHMED'))
print(switch_case('Welcome to PYTHON'))
