'''
اكتب دالة لحساب مستحقات الفريلانسر بحيث
تمرر سعر الساعة وعدد الساعات
ملاحظة / اذا كان عدد الساعات اكثر من 40 ساعة
يحاسب الفريلانسر بمقدار 1.5 من سعر الساعة للساعات الزيادة
'''


def calc_payment(rate, hours):
    if hours <= 40:
        return hours * rate
    else:
        return 40 * rate + (hours - 40) * rate * 1.5


print(calc_payment(10, 35))
print(calc_payment(10, 40))
print(calc_payment(10, 41))
print(calc_payment(10, 45))
