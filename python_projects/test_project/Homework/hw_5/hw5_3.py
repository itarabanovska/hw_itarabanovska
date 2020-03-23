while True:
    try:
        year = int(input('Enter smth:'))
        if year % 4 == 0:
            print('A leap year.')
        else:
            print('Not a leap year.')
        break

    except ValueError:
        print('Enter a number!')





