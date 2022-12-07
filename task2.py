#3.11 Вводим с клавиатуры строку. Необходимо сказать, является ли эта строка дробным числом

stroka = input('Введите строку: ')

count_1 = 0
count_position = 0

for char in stroka:
    if char == '.' or char == ',':
        count_1 += 1
    if count_1 == 0:
        count_2 += 1
without = ''
if count_1 != 1:
    print('Введенная строка не является дробным числом')
else:
    if without == stroka[0:count_position] + stroka[count_position + 1:len(stroka)]:
        print(f'Строка {stroka} является дробным числом ')
    else:
        print(f'Строка {stroka} не дробное число')