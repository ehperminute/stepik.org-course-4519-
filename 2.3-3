Васю назначили завхозом в туристической группе и он подошёл к подготовке ответственно, составив справочник продуктов с указанием калорийности на 100 грамм, а также содержание белков, жиров и углеводов на 100 грамм продукта. Ему не удалось найти всю информацию, поэтому некоторые ячейки остались незаполненными (можно считать их значение равным нулю). Также он использовал какой-то странный офисный пакет и разделял целую и дробную часть чисел запятой. Таблица доступна по ссылке https://stepik.org/media/attachments/lesson/245290/trekking3.xlsx

Вася составил раскладку по продуктам на весь поход (она на листе "Раскладка") с указанием номера дня, названия продукта и его количества в граммах. Для каждого дня посчитайте 4 числа: суммарную калорийность и граммы белков, жиров и углеводов. Числа округлите до целых вниз и введите через пробел. Информация о каждом дне должна выводиться в отдельной строке.

import xlrd3

wb = xlrd3.open_workbook('trekking3.xlsx')
sh = wb.sheet_by_index(0)
nutrition = {prod.value: (cal.value, prot.value, fat.value, carb.value)\
         for prod, cal, prot, fat, carb in\
         zip(sh.col(0)[1:], sh.col(1)[1:], sh.col(2)[1:], sh.col(3)[1:], sh.col(4)[1:])}
ration = wb.sheet_by_index(1)
i = 1
for day in range(1, len(set([i.value for i in ration.col(0)[1:]])) + 1):
    cal, prot, fat, carbs =  0, 0, 0, 0
    while i < len(ration.col(0)) and day == int(ration.col(0)[i].value):        
        pr, mass = ration.col(1)[i], ration.col(2)[i]
        cal += float(nutrition[pr.value][0] or 0) * float(mass.value / 100)
        prot += float(nutrition[pr.value][1] or 0) * float(mass.value / 100)
        fat += float(nutrition[pr.value][2] or 0) * float(mass.value / 100)
        carbs += float(nutrition[pr.value][3] or 0) * float(mass.value / 100)
        i += 1
    print(*map(int, [cal, prot, fat, carbs]), sep = ' ', end='')
    print()
