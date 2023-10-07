# вывод шахматной доски на экран
import pygame
import sys
# добавление многопоточности
from threading import *
from time import time, sleep

# ввод координат фигуры
id_1 = ''  # координаты первой клетки
id_2 = ''  # координаты второй клетки
flag = 0  # 1 - найдено решение как попасть из первой клетки на клетку два
abc = ' ABCDEFGH'

while flag != 1:  # проверяем на ошибку ввод координаты клетки
    id_1 = input("введите координаты первой клетки(пример:A2): ")
    for i in abc:
        for j in '12345678':
            if i == id_1[0] and j == id_1[1]:
                flag = 1
flag = 0
while flag != 1:  # проверяем на ошибку ввод координаты клетки
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
k = int([alfabet[i] for i in id][0])  # перезаписываем буквенные координаты в числа
m = int([alfabet[i] for i in id][1])  # перезаписываем буквенные координаты в числа

def one():
    # вывод шахматной доски на экран
    # Инициализация Pygame
    pygame.init()

    # Размеры окна
    WIDTH, HEIGHT = 400, 400

    # Цвета
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # Создание окна
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # Определение размера клеток
    cell_size = WIDTH // 8

    # Определение шахматной доски с разными цветами фонов
    chessboard = [[WHITE if (row + col) % 2 == 0 else BLACK for col in range(8)] for row in range(8)]

    # Определение позиций фигур (пример: король и ферзь)
    fist_position = (8 - l, k - 1)  # Позиция первой фигуры (строка, столбец)
    second_position = (8 - n, m - 1)  # Позиция второй фигуры (строка, столбец)

    # Основной цикл
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Отрисовка шахматной доски
        for row in range(8):
            for col in range(8):
                pygame.draw.rect(screen, chessboard[row][col], (col * cell_size, row * cell_size, cell_size, cell_size))

        # Отрисовка фигур (пример: король и ферзь)
        fist_x, fist_y = fist_position
        second_x, second_y = second_position

        # Отрисовка короля (пример: используем красный цвет)
        pygame.draw.circle(screen, (0, 0, 255),
                           (fist_y * cell_size + cell_size // 2, fist_x * cell_size + cell_size // 2), cell_size // 2)

        # Отрисовка ферзя (пример: используем синий цвет)
        pygame.draw.circle(screen, (255, 0, 0),
                           (second_y * cell_size + cell_size // 2, second_x * cell_size + cell_size // 2), cell_size // 2)

        pygame.display.flip()

    # Завершение работы Pygame
    pygame.quit()
    sys.exit()


def two():
    # основная программа
    if (k + l) % 2 == (m + n) % 2:
        print("выбранные клетки одного цвета")
    else:
        print("выбранные клетки разных цветов")

    figuur = 'NаN'  # проверка на ошибку ввода названия фигуры
    while figuur != 'ферзь' and figuur != 'ладья' and figuur != 'слон' and figuur != 'конь':
        figuur = input("введите название фигуры (пример: ферзь, ладья, слон или конь) на клетке " + str(id_1) + ": ")

    flag = 0  # проверяем угрожает ли фигура на клетке 1 фигуре на клетке 2
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

            # узнаем можно ли с клетки один одним ходом ладьи, ферзя или слона попасть на клетку 2
    if flag == 1:
        print("С клетки", id_1, "одним ходом", figuur, "может попасть на клетку", id_2)
    else:  # если нет, то узнать, как это можно сделать за два хода
        id_mid = ''
        flag = 0

        if figuur == 'слон':
            if (k + l) % 2 == (m + n) % 2:  # проверяем являются ли клетки одного цвета
                change = abs(abs(k - m) + abs(l - n)) // 2  # сдвиг клетки по горизонтали и вертикали

                # вычисляем подходящую клетку
                # 1 четверть
                if k - m <= 0 and l - n < 0 and flag == 0:
                    if k + change <= 8 and l + change <= 8:  # проверяем первый теоретический ход фигуры на существование
                        id_mid = abc[k + change] + str(l + change)
                        flag = 1
                    elif m - change > 0 and n - change > 0:  # проверяем второй теоретический ход фигуры на существование
                        id_mid = abc[m - change] + str(n - change)
                        flag = 1
                        # 2 четверть
                if k - m < 0 and l - n >= 0 and flag == 0:
                    if k + change <= 8 and l - change > 0:  # проверяем первый теоретический ход фигуры на существование
                        id_mid = abc[k + change] + str(l - change)
                        flag = 1
                    elif m - change > 0 and n + change <= 8:  # проверяем второй теоретический ход фигуры на существование
                        id_mid = abc[m - change] + str(n + change)
                        flag = 1
                        # 3 четверть
                if k - m >= 0 and l - n > 0 and flag == 0:
                    if k - change > 0 and l - change > 0:  # проверяем первый теоретический ход фигуры на существование
                        id_mid = abc[k - change] + str(l - change)
                        flag = 1
                    elif m + change <= 8 and n + change <= 8:  # проверяем второй теоретический ход фигуры на существование
                        id_mid = abc[m + change] + str(n + change)
                        flag = 1
                        # 4 четверть
                if k - m > 0 and l - n <= 0 and flag == 0:
                    if k - change > 0 and l + change <= 8:  # проверяем первый теоретический ход фигуры на существование
                        id_mid = abc[k - change] + str(l + change)
                        flag = 1
                    elif m + change <= 8 and n - change > 0:  # проверяем второй теоретический ход фигуры на существование
                        id_mid = abc[m + change] + str(n - change)
                        flag = 1
            else:
                print("выбранные клетки разных цветов, слон не может попасть на клетку: ", id_2)
                flag = 0

        if figuur == 'ладья':
            if k > m and l < n:  # проверяем возможные варианты
                id_mid = abc[max(k, m)] + str(max(l, n))
                flag = 1
            if k < m and l < n:  # проверяем возможные варианты
                id_mid = abc[min(k, m)] + str(max(l, n))
                flag = 1
            if k < m and l > n:  # проверяем возможные варианты
                id_mid = abc[max(k, m)] + str(max(l, n))
                flag = 1
            if k > m and l > n:  # проверяем возможные варианты
                id_mid = abc[max(k, m)] + str(min(l, n))
                flag = 1

        if figuur == 'ферзь':
            if (k + l) % 2 == (m + n) % 2:  # сдвиг клетки по горизонтали и вертикали
                change = abs(abs(k - m) + abs(l - n)) // 2  # сдвиг клетки по горизонтали и вертикали
                # подбираем подходящую клетку
                # 1 четверть
                if k - m <= 0 and l - n < 0 and flag == 0:
                    if k + change <= 8 and l + change <= 8:  # проверяем первый теоретический ход фигуры на существование
                        id_mid = abc[k + change] + str(l + change)
                        flag = 1
                    elif m - change > 0 and n - change > 0:  # проверяем второй теоретический ход фигуры на существование
                        id_mid = abc[m - change] + str(n - change)
                        flag = 1
                        # 2 четверть
                if k - m < 0 and l - n >= 0 and flag == 0:
                    if k + change <= 8 and l - change > 0:  # проверяем первый теоретический ход фигуры на существование
                        id_mid = abc[k + change] + str(l - change)
                        flag = 1
                    elif m - change > 0 and n + change <= 8:  # проверяем второй теоретический ход фигуры на существование
                        id_mid = abc[m - change] + str(n + change)
                        flag = 1
                        # 3 четверть
                if k - m >= 0 and l - n > 0 and flag == 0:
                    if k - change > 0 and l - change > 0:  # проверяем первый теоретический ход фигуры на существование
                        id_mid = abc[k - change] + str(l - change)
                        flag = 1
                    elif m + change <= 8 and n + change <= 8:  # проверяем второй теоретический ход фигуры на существование
                        id_mid = abc[m + change] + str(n + change)
                        flag = 1
                        # 4 четверть
                if k - m > 0 and l - n <= 0 and flag == 0:
                    if k - change > 0 and l + change <= 8:  # проверяем первый теоретический ход фигуры на существование
                        id_mid = abc[k - change] + str(l + change)
                        flag = 1
                    elif m + change <= 8 and n - change > 0:  # проверяем второй теоретический ход фигуры на существование
                        id_mid = abc[m + change] + str(n - change)
                        flag = 1
            else:
                if k > m and l < n:  # проверяем возможные варианты
                    id_mid = abc[max(k, m)] + str(max(l, n))
                    flag = 1
                if k < m and l < n:  # проверяем возможные варианты
                    id_mid = abc[min(k, m)] + str(max(l, n))
                    flag = 1
                if k < m and l > n:  # проверяем возможные варианты
                    id_mid = abc[max(k, m)] + str(max(l, n))
                    flag = 1
                if k > m and l > n:  # проверяем возможные варианты
                    id_mid = abc[max(k, m)] + str(min(l, n))
                    flag = 1

        l_new = k_new = 0
        if figuur == 'конь':
            if (k + l) % 2 == (m + n) % 2:  # выбранные клетки одного цвета
                sum = (
                    (-1, 2), (1, 2), (2, 1), (2, -1), (-1, -2), (1, -2), (-2, 1),
                    (-2, -1))  # возможные варианты ходов коня
                for i in range(8):
                    k_new = k + sum[i][0]
                    l_new = l + sum[i][1]
                    if abs(k_new - m) + abs(
                            l_new - n) == 3 and k_new > 0 and k_new <= 8 and l_new > 0 and l_new <= 8 and k_new != m and l_new != n:
                        flag = 1
                        break
                if flag == 1:
                    id_mid = abc[k_new] + str(l_new)
            else:
                print("конь не может попасть на клетку", id_2, "за 2 хода")

        if flag == 1:
            print("С клетки", id_1, "за два хода,", figuur, "может попасть на клетку", id_2, "пройдя через клетку",
                  id_mid)
# создаем два ассинхранных потока
t1 = Thread(target = one)
t2 = Thread(target = two)
# запускаем ассинхранные функции
t1.start()
t2.start()



