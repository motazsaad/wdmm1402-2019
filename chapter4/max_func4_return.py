'''
اكتب دالة لتمرير 3 ارقام وارجاع الرقم الاكبر
'''


def get_largest(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        # print(n1)
        return n1
    elif n2 >= n1 and n2 >= n3:
        # print(n2)
        return n2
    else:
        # print(n3)
        return n3


l1 = get_largest(3, 7, 2)  # result 7
print(l1)
l2 = l1 + 3
print(l2)
