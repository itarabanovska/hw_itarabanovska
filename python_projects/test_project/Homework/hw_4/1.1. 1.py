number1 = int(input('Enter first number: '))
sign = input('Enter "+", "-", "*", "/", "**" or " "√": ')
number2 = int(input('Enter second number: '))

from math import sqrt

if sign in ('+', '-', '*', '/', '**', '√'):
    if sign == '+':
        print(number1 + number2)
    if sign == '-':
        print(number1 + number2)
    if sign == '*':
        print(number1 * number2)
    if sign == '/':
        print(number1 / number2)
    if sign == '**':
        print(number1 ** number2)
    if sign == '√':
        print(number1**(1/number2))

else:
    print('Error')