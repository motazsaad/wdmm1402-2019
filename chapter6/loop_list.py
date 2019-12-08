'''
اكتب برنامج  لادخال نص وطباعة كل حرف في سطر
'''

my_str = input('enter a string: ')
# for ch in my_str:
#     print(ch)

for i in range(len(my_str)):
    print(i, my_str[i])
