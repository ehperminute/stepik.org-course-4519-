Васю назначили завхозом в туристической группе и он подошёл к подготовке ответственно, составив справочник продуктов с указанием калорийности на 100 грамм, а также содержание белков, жиров и углеводов на 100 грамм продукта. Ему не удалось найти всю информацию, поэтому некоторые ячейки остались незаполненными (можно считать их значение равным нулю). Также он использовал какой-то странный офисный пакет и разделял целую и дробную часть чисел запятой. Таблица доступна по ссылке https://stepik.org/media/attachments/lesson/245290/trekking2.xlsx 
Вася составил раскладку по продуктам на один день (она на листе "Раскладка") с указанием названия продукта и его количества в граммах. Посчитайте 4 числа: суммарную калорийность и граммы белков, жиров и углеводов. Числа округлите до целых вниз и введите через пробел.

import xlrd3
wb = xlrd3.open_workbook('trekking2.xlsx')
sh = wb.sheet_by_index(0)
nutrition = {prod.value: (cal.value, prot.value, fat.value, carb.value)\
         for prod, cal, prot, fat, carb in\
         zip(sh.col(0), sh.col(1), sh.col(2), sh.col(3), sh.col(4))}
def zero_if_empty(x):
    try: 
        return float(x)
    except: 
        return 0
ration = wb.sheet_by_index(1)
cal, prot, fat, carbs =  0, 0, 0, 0
for pr, mass in (zip(ration.col(0)[1:], ration.col(1)[1:])):
    cal += zero_if_empty(nutrition[pr.value][0]) * float(mass.value / 100)
    prot += zero_if_empty(nutrition[pr.value][1]) * float(mass.value / 100)
    fat += zero_if_empty(nutrition[pr.value][2]) * float(mass.value / 100)
    carbs += zero_if_empty(nutrition[pr.value][3]) * float(mass.value / 100)
[print(int(i), end=' ') for i in [cal, prot, fat, carbs]]
