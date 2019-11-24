def wash(n):
    while n > 0:
        print(n)
        print('Lather')
        print('Rinse')
        n = n - 1  # iteration variable
        print('----------------------')
    print('Dry off!')
    print(n)


wash(3)
wash(7)
