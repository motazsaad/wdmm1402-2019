'''
اكتب برنامج لادخال علامة الطالب وطباعة تقديره وفقا لنظام الجامعة

'''
mark = int(input('please enter your mark: '))
if mark < 60:
    print('fail')
elif mark < 70:
    print('pass')
elif mark < 80:
    print('good')
elif mark < 90:
    print('very good')
else:
    print('excellent')
