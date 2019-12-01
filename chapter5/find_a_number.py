'''
اكتب برنامج لادخال رقم والبحث عن هذا الرقم في دالة
النتيجة المطلوبة هي انه الرقم موجود او غير موجود
'''
l1 = [3, 6, 8, 90, 12, 43, 20, 100, 65, 23, 98, 12, 89, 65]
search_number = int(input('enter the num u want 2 search: '))
result = 'not found'
for number in l1:
    if number == search_number:
        result = 'found'
        break
print(result)
