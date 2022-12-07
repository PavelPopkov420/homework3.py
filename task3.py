Вводим с клаиватуры строку. Необходимо вывести строку, где развернём подстроку между первой и последней буквой "о"
# из исходной строки. Если она только одна или её нет - то сообщить, что буква "о" - одна или не встречается.

stroka = input('Введите строку: ')
s_low = stroka.lower()

i_min = 0
i_max = 0

for i in range(len(stroka)):
    if s_low[i] == 'о':
        i_min = i
        break
for i in range(len(stroka)-1, -1, -1):
    if s_low[i] == 'о':
        i_max = i
        break
if i_min > 0 or i_max > 0:
    O_revers = (stroka[:i_min] + stroka[i_max:i_min:-1] + stroka[i_max:])
    print(f'Перевернутый результат: {O_revers}')
else:
    print('Буква О отсутвует')