'''
اكتب برنامج لادخال علامة الطالب وطباعة تقديره وفقا لنظام الجامعة

'''
mark = int(input('please enter your mark: '))
if mark < 0:
    print('out of range')
elif mark < 60:
    print('fail')
elif mark < 70:
    print('pass')
elif mark < 80:
    print('good')
elif mark < 90:
    print('very good')
elif mark <= 100:
    print('excellent')
else:
    print('out of range')
