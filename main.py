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
3) Все маршруты от 0x0 до mxn
"""
from random import randint


def create_matrix(matrix: list, row: int, col: int) -> list:
    """Cоздание матрицы"""
    for i in range(0, row):
        temp_list = [randint(0, 9) for i in range(0, col)]
        matrix.append(temp_list)
    return matrix


def show_matrix(matrix: list):
    """Демонстрация матрицы в консоле"""
    for i in range(0, len(matrix)):
        print(matrix[i])


def search_route(matrix, start, end) -> list:
    """Поиск минимального пути"""
    row, col = len(matrix), len(matrix[0])

    # Инициализируем массив temp значением inf и установите значение начальной точки
    temp = [[float("inf")] * col for _ in range(row)]
    temp[start[0]][start[1]] = matrix[start[0]][start[1]]

    # Итерация по сетке и обновление минимальной суммы для каждой ячейки
    for i in range(row):
        for j in range(col):
            if i > 0 and matrix[i][j] != "#":
                temp[i][j] = min(temp[i][j], temp[i - 1][j] + matrix[i][j])
            if j > 0 and matrix[i][j] != "#":
                temp[i][j] = min(temp[i][j], temp[i][j - 1] + matrix[i][j])

    # Инициализация списка маршрутов и обратный путь по сетке
    route = []
    route.append(end)
    i, j = end
    while i != start[0] or j != start[1]:
        if i > 0 and temp[i][j] == temp[i - 1][j] + matrix[i][j]:
            i -= 1
            route.append((i, j))
        else:
            j -= 1
            route.append((i, j))

    # Возвращаем маршрут в обратном порядке
    return route[::-1]


def count_route(matrix: list, route: list):
    """Подсчет времени движения и вывод данных в консоль"""
    sum_route = 0
    for i in range(len(route)):
        sum_route += matrix[route[i][0]][route[i][1]]
        print(matrix[route[i][0]][route[i][1]], end=" -> ")
    print(f"Весь путь занял: {sum_route} ед. времени")


if __name__ == "__main__":
    row = int(input())
    col = int(input())

    matrix = []
    start = (0, 0)
    end = (row - 1, col - 1)
    sum_route = 0

    create_matrix(matrix, row, col)
    show_matrix(matrix)
    route = search_route(matrix, start, end)
    count_route(matrix, route)
