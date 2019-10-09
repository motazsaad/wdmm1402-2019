try:
    mark = int(input('plz enter your mark: '))
    if mark < 60:
        print('fail')
    else:
        print('success')
except:
    print('input must be numeric')
