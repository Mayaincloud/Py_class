# 1. Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

n = float(input('Введите число: '))
len_n = len(str(n)) 
m = n * 10 ** (len_n - 2)
sum = 0
while m > 0:
    sum = sum + m % 10
    m = m // 10
print('Сумма всех цифр числа ', n, ' - ', int (sum))