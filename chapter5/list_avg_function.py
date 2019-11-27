'''
اكتب دالة تأخذ قائمة وترجع المتوسط
'''


def list_avg(l1):
    count = 0
    total = 0
    for num in l1:
        count = count + 1
        total = total + num
    return total / count


print(list_avg([3, 6, 8, 90, 12, 43, 7, 65]))
print(list_avg([12, 5, 7, 98, 89]))
