'''
اكتب برنامج لعد عدد العناصر في قائمة
'''

black_list = ['Mohannad', 'Ahmed', 'Hazem', 'Salah', 'bashar', 'Mosa', 'Shaker', 'Shehada', 'Shehab', 'Mahmoud']
# step 1: define a variable with inital value
count = 0
# step 2: enter loop
for name in black_list:
    count = count + 1
# step 3: print result
print('count:', count)
