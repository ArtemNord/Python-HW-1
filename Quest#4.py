# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

# X = randrange(-10, 10, 1)
# Y = randrange(-10, 10, 1)

# print(X)
# print(Y)

# if X == 0 or Y == 0:
#     print('Параметры не корректны')
# elif X > 0 and Y > 0:
#     print('1 четверть')
# elif X > 0 and Y < 0:
#     print('4 четверть')
# elif X < 0 and Y > 0:
#     print('2 четверть')
# elif X < 0 and Y < 0:
#     print('3 четверть')

from random import randrange


NumberQuarter = int(randrange(0, 6, 1))
print('Номер выбранной четверти:', NumberQuarter)

text0 = 'Диапозон координат'
text1 = ' до бесконечности'
text2 = ' до "отрицательной ;)" бесконечности'
PlusRan = list(range(1, 4, 1))
MinusRan = list(range(-1, -4, -1))

if NumberQuarter <= 0 or NumberQuarter > 4:
    print('Введите число от 1 до 4')
elif NumberQuarter == 1:
    print (text0, 'Х от', PlusRan, text1)
    print (text0, 'Y от', PlusRan, text1)
elif NumberQuarter == 2:
    print(text0, 'Х от', MinusRan, text2)
    print(text0, 'Y от', PlusRan, text1)
elif NumberQuarter == 3:
    print(text0, 'Х от', MinusRan, text2)
    print(text0, 'Y от', MinusRan, text2)
elif NumberQuarter == 4:
    print(text0, 'Х от', PlusRan, text1)
    print(text0, 'Y от', MinusRan, text2)