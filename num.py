print('Введите действие: ')
sing = input()
assert 'sing' in ['+', '-', '*', '/'], 'Такого действия нет'
print('Введте первую цифру: ')
num1 = int(input())
print('Введите вторую цифру')
num2 = int(input())
try:
    if sing == '+':
        a = num1 + num2
        print(a)
    elif sing == '-':
        a = num1 - num2
    elif sing == '*':
        a = num1 * num2
    elif sing == '/':
        a = num1 / num2
        print(a)
except ZeroDivisionError:
    print('Деление на ноль невозможно')
