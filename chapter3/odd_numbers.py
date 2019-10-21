'''
اكتب برنامج لطبعة الارقام الفردية
مع ترك المجال للمستخدم لادخال البداية والنهاية
'''
start = int(input('enter start number: '))
stop = int(input('enter stop number: '))

for num in range(start, stop):
    if num % 2 != 0:
        print(num)
