id_1 = ''
id_2 = ''
flag = 0
abc = ' ABCDEFGH'

while flag != 1:
    id_1 = input("введите координаты первой клетки(пример:A2): ")
    for i in abc:
        for j in '12345678':
            if i == id_1[0] and j == id_1[1]:
                flag = 1
flag = 0
while flag != 1:
    id_2 = input("введите координаты второй клетки(пример:B1): ")
    for i in abc:
        for j in '12345678':
            if i == id_2[0] and j == id_2[1]:
                flag = 1

id = id_1[0] + id_2[0]
l = int(id_1[1])
n = int(id_2[1])

# проверяем являются ли поля (k, I) и (m, n) одного цвета.
alfabet = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}
k = int([alfabet[i] for i in id][0])
m = int([alfabet[i] for i in id][1])

if (k + l) % 2 == (m + n) % 2:
    print("выбранные клетки одного цвета")
else:
    print("выбранные клетки разных цветов")

figuur = 'NаN'
while figuur != 'ферзь' and figuur != 'ладья' and figuur != 'слон' and figuur != 'конь':
    figuur = input("введите название фигуры (пример: ферзь, ладья, слон или конь) на клетке " + str(id_1) + ": ")

flag = 0
if figuur == 'конь':
    if abs(k - m) + abs(l - n) == 3 and k != m and l != n:
        print("Конь угрожает фигуре на клетке", id_2)
        flag = 1
    else:
        print(figuur, "неугрожает фигуре на клетке", id_2)
elif figuur == 'ладья':
    if k == m or l == n:
        print("Ладья угрожает фигуре на клетке", id_2)
        flag = 1
    else:
        print(figuur, "неугрожает фигуре на клетке", id_2)
elif figuur == 'слон':
    if abs(k - m) == abs(l - n):
        print("Слон угрожает фигуре на клетке", id_2)
        flag = 1
    else:
        print(figuur, "неугрожает фигуре на клетке", id_2)
elif figuur == 'ферзь':
    if k == m or l == n or abs(k - m) == abs(l - n):
        print("Ферзь угрожает фигуре на клетке", id_2)
        flag = 1
    else:
        print(figuur, "неугрожает фигуре на клетке", id_2)


if flag == 1:
    print("С клетки", id_1, "одним ходом", figuur, "может попасть на клетку", id_2)
else:
    id_mid = ''
    flag = 0

    if figuur == 'слон':
        if (k + l) % 2 == (m + n) % 2:
            change = abs(abs(k - m) + abs(l - n)) // 2

                                                     # вычисляем подходящую клетку
                                                             # 1 четверть
            if k - m <= 0 and l - n < 0 and flag == 0:
                if k + change <= 8 and l + change <= 8:
                    id_mid = abc[k + change] + str(l + change)
                    flag = 1
                elif m - change > 0 and n - change > 0:
                    id_mid = abc[m - change] + str(n - change)
                    flag = 1
                    # 2 четверть
            if k - m < 0 and l - n >= 0 and flag == 0:
                if k + change <= 8 and l - change > 0:
                    id_mid = abc[k + change] + str(l - change)
                    flag = 1
                elif m - change > 0 and n + change <= 8:
                    id_mid = abc[m - change] + str(n + change)
                    flag = 1
                    # 3 четверть
            if k - m >= 0 and l - n > 0 and flag == 0:
                if k - change > 0 and l - change > 0:
                    id_mid = abc[k - change] + str(l - change)
                    flag = 1
                elif m + change <= 8 and n + change <= 8:
                    id_mid = abc[m + change] + str(n + change)
                    flag = 1
                    # 4 четверть
            if k - m > 0 and l - n <= 0 and flag == 0:
                if k - change > 0 and l + change <= 8:
                    id_mid = abc[k - change] + str(l + change)
                    flag = 1
                elif m + change <= 8 and n - change > 0:
                    id_mid = abc[m + change] + str(n - change)
                    flag = 1
        else:
            print("выбранные клетки разных цветов, слон не может попасть на клетку: ", id_2)
            flag = 0

    if figuur == 'ладья':
        if k > m and l < n:
            id_mid = abc[max(k, m)] + str(max(l, n))
            flag = 1
        if k < m and l < n:
            id_mid = abc[min(k, m)] + str(max(l, n))
            flag = 1
        if k < m and l > n:
            id_mid = abc[max(k, m)] + str(max(l, n))
            flag = 1
        if k > m and l > n:
            id_mid = abc[max(k, m)] + str(min(l, n))
            flag = 1

    if figuur == 'ферзь':
        if (k + l) % 2 == (m + n) % 2:
            change = abs(abs(k - m) + abs(l - n)) // 2
                                        # подбираем подходящую клетку
                                                # 1 четверть
            if k - m <= 0 and l - n < 0 and flag == 0:
                if k + change <= 8 and l + change <= 8:
                    id_mid = abc[k + change] + str(l + change)
                    flag = 1
                elif m - change > 0 and n - change > 0:
                    id_mid = abc[m - change] + str(n - change)
                    flag = 1
                                               # 2 четверть
            if k - m < 0 and l - n >= 0 and flag == 0:
                if k + change <= 8 and l - change > 0:
                    id_mid = abc[k + change] + str(l - change)
                    flag = 1
                elif m - change > 0 and n + change <= 8:
                    id_mid = abc[m - change] + str(n + change)
                    flag = 1
                                              # 3 четверть
            if k - m >= 0 and l - n > 0 and flag == 0:
                if k - change > 0 and l - change > 0:
                    id_mid = abc[k - change] + str(l - change)
                    flag = 1
                elif m + change <= 8 and n + change <= 8:
                    id_mid = abc[m + change] + str(n + change)
                    flag = 1
                                             # 4 четверть
            if k - m > 0 and l - n <= 0 and flag == 0:
                if k - change > 0 and l + change <= 8:
                    id_mid = abc[k - change] + str(l + change)
                    flag = 1
                elif m + change <= 8 and n - change > 0:
                    id_mid = abc[m + change] + str(n - change)
                    flag = 1
        else:
            if k > m and l < n:
                id_mid = abc[max(k, m)] + str(max(l, n))
                flag = 1
            if k < m and l < n:
                id_mid = abc[min(k, m)] + str(max(l, n))
                flag = 1
            if k < m and l > n:
                id_mid = abc[max(k, m)] + str(max(l, n))
                flag = 1
            if k > m and l > n:
                id_mid = abc[max(k, m)] + str(min(l, n))
                flag = 1


    if flag == 1:
        print("С клетки", id_1, "за два хода,", figuur, "может попасть на клетку", id_2, "пройдя через клетку", id_mid)