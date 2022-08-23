import math


def get_path(p, last_point, first_point):
    path = [last_point]
    while last_point != first_point:
        last_point = points_list[last_point][first_point]
        path.append(last_point)
    return path


relation_matrix = [[0, 2, math.inf, 3, 1, math.inf, math.inf, 10],
                   [2, 0, 4, math.inf, math.inf, math.inf, math.inf, math.inf],
                   [math.inf, 4, 0, math.inf, math.inf, math.inf, math.inf, 3],
                   [3, math.inf, math.inf, 0, math.inf, math.inf, math.inf, 8],
                   [1, math.inf, math.inf, math.inf, 0, 2, math.inf, math.inf],
                   [math.inf, math.inf, math.inf, math.inf, 2, 0, 3, math.inf],
                   [math.inf, math.inf, math.inf, math.inf, math.inf, 3, 0, 1],
                   [10, math.inf, 3, 8, math.inf, math.inf, 1, 0],
                   ]

points_quantity = len(relation_matrix)                       # число вершин в графе
points_list = [[_ for _ in range(points_quantity)] for _ in range(points_quantity)]    # начальный список предыдущих вершин для поиска кратчайших маршрутов

for k in range(points_quantity):
    for i in range(points_quantity):
        for j in range(points_quantity):
            d = relation_matrix[i][k] + relation_matrix[k][j]
            if relation_matrix[i][j] > d:
                relation_matrix[i][j] = d
                points_list[i][j] = k     # номер промежуточной вершины при движении от i к j

# нумерацця вершин начинается с нуля
start = 0
end = 7
print(get_path(points_list, end, start))
