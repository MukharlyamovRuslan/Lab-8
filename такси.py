#Создал списки для последующего ввода данных о расстоянии и тарифах подключил библиотеку num2words
from num2words import num2words
dis = []
pri = []
summa = []
dis2 = []
pri2 = []
all_index_pri = []
amount = int(input('Введите количество сотрудников компании (от 1 до 1000 включительно): '))
#Проверка на ошибку
while amount < 1 or amount > 1000:
    print('Ошибка!!!')
    amount = int(input('Введите количество сотрудников компании (от 1 до 1000 включительно): '))
#Создал цикл для ввода данных о расстоянии до дома каждого сотрудника
for i in range(amount):
    distance = int(input('Введите расстояние в км для ' + str(i+1) + ' сотрудника (от 1 до 1000 включительно): '))
    while distance < 1 or distance > 1000:
        print('Ошибка!!!')
        distance = int(input('Введите расстояние в км для ' + str(i) + 'сотрудника (от 1 до 1000 включительно): '))
    dis.append(distance)
    dis2.append(distance)
#Создал цикл для ввода тарифов на такси
for j in range(0, amount):
    price = int(input('Введите тариф для ' + str(j+1) + ' такси (от 1 до 10000 включительно): '))
    while price < 1 or price > 10000:
        print('Ошибка!!!')
        price = int(input('Введите тариф для ' + str(j+1) + ' такси (от 1 до 10000 включительно): '))
    pri.append(price)
    pri2.append(price)
#Отсортировал списки, список с расстояниями по возрастанию, а список
#с тарифами по убывания
dis2.sort()
pri2.sort(reverse = True)
#Создал цикл для нахождения стоимости выгодных поездок
for a in range(0, amount):
    itog = dis2[a] * pri2[a]
    summa.append(itog)
summa.append(sum(summa))
#Создал цикл, в котором исключается выбор одного и того же такси нескрлькими сотрудниками
for ind_pri2 in pri2:
    index_pri = pri.index(ind_pri2)
    pri[index_pri] = 0
    all_index_pri.append(index_pri + 1)
#Выбор правильного окончания слова "рубль"
rub = ''

rub_2_to_4 = [2, 3, 4]

if summa[-1] % 100 <= 20 and summa[-1] % 100 >= 5:
    rub = ' рублей'
elif summa[-1] % 10 == 1 or summa[-1] % 100 == 1 or summa[-1] % 1000 == 1:
    rub = ' рубль'
elif summa[-1] % 10 in rub_2_to_4 or summa[-1] % 100 in rub_2_to_4 or summa[-1] % 1000 in rub_2_to_4:
    rub = ' рубля'
else:
    rub = ' рублей'

print('1. ' + str(all_index_pri))
print('2. ' + str(summa[-1]))
print('3. ' + num2words(summa[-1], lang='ru') + rub)