"""
Задача:
Карта дорог представлена матрицей m*n.
Где в ячейке i,j время проезда некоторого участка дороги. 
Водитель находится в клетке 0,0. Может двигаться "в матрице" либо на 1 клетку вниз, либо на 1 клетку вправо.  
Должен попасть в правый нижний угол (m, n).
Нужно перебрать все возможные маршруты и найти маршрут с наименьшей суммой клеток, через которые этот маршрут проходит (от 0,0 до m, n)

Условия: 
1) Матрица задается m n с клавиатуры
2) Данные в матрице задаются рандомно
"""

from numpy import matlib as mlib


def create_matrix(row: int, col: int) -> mlib.matrix:
    matrix = mlib.rand((row, col))
    return matrix


row, col = [int(x) for x in input("Введите размерность матрицы(m,n): ").split()]

matrix = create_matrix(row, col)

sum_move = 0
motion = []
move_row, move_col = 0, 0
print("-----------------------------------------------")
print(matrix)
Switch = True
while Switch:
    move = move_row, move_col

    if move_row + 1 < row:
        bottom_move = matrix[move_row + 1, move_col]
    else:
        bottom_move = None

    if move_col + 1 < col:
        right_move = matrix[move_row, move_col + 1]
    else:
        right_move = None

    match right_move or bottom_move:
        case None:
            Switch = False

        case _ if right_move is None:
            sum_move += bottom_move
            move_row += 1
            motion.append(matrix[move_row, move_col])

        case _ if bottom_move is None:
            sum_move += right_move
            move_col += 1
            motion.append(matrix[move_row, move_col])
        case _:
            if bottom_move > right_move:
                sum_move += right_move
                move_col += 1
                motion.append(matrix[move_row, move_col])
            else:
                sum_move += bottom_move
                move_row += 1
                motion.append(matrix[move_row, move_col])
print("-----------------------------------------------")
for move in motion:
    print(round(move, 5), end=" --> " if move else "")

print(f"Весь путь занял {round(sum_move, 5)} ед. времени")
