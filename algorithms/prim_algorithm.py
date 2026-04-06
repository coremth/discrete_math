"""
Алгоритм Прима

Задача достаточно проста:
Найти минимальную сумму всех ребер, чтобы они соединили все доступные
вершины.

Само решение подразумевает собой следующее:
1.  Берём произвольную вершину.
2.  Находим для нее ближайшего соседа, и соединяем их.
3.  Пока у нас остаются неприсоединенные вершины, мы продолжаем искать
    ближайшую НЕприсоединненную вершину, которая будет соседствовать
    с любой из уже присоединенных вершин.

Куча идеально подходит для решения этой задачи. Куча гарантирует, что
минимальный элемент всегда будет на ее вершине. Таким образом, мы всегда
можем обращаться к 0-му элементу и получать то, что мы так ищем.
Но как именно её заполнять? Процесс выглядит следующим образом:
1.  Берём произвольную вершину.
2.  Помещаем в кучу всех её ближайших соседей и вес их рёбер.
3.  Вытаскиваем 0-ой элемент из кучи (тот, который имеет наименьший
    вес).
4.  Полученный элемент записываем в список уже известных вершин.
5.  Если вершина уже присоединена, то просто игнорируем её.
6.  Теперь записываем оставшихся ближайших соседей и вес их рёбер
    относительно новой точки.
7.  Повторяем, начиная с шага два, пока количество присоединенных
    вершин не станет равно общему количеству вершин.
"""

import heapq

base_graph = [
    {"point": "A", "links": {"B": 3, "F": 2}},
    {"point": "B", "links": {"A": 3, "G": 6, "C": 3}},
    {"point": "C", "links": {"B": 3, "G": 1, "E": 2, "D": 3}},
    {"point": "D", "links": {"C": 3, "E": 5}},
    {"point": "E", "links": {"D": 5, "C": 2, "G": 3, "F": 4}},
    {"point": "F", "links": {"A": 2, "E": 4, "G": 3}},
    {"point": "G", "links": {"B": 6, "C": 1, "E": 3, "F": 3}},
]

graph_index = {node["point"]: node for node in base_graph}


def prim(graph_index, start_point):
    visited = {start_point}
    mst_edges = []

    heap = []
    for neighbor, weight in graph_index[start_point]["links"].items():
        heapq.heappush(heap, (weight, start_point, neighbor))

    while heap and len(visited) < len(graph_index):
        weight, from_v, to_v = heapq.heappop(heap)
        if to_v in visited:
            continue

        visited.add(to_v)
        mst_edges.append((weight, from_v, to_v))

        for neighbor, weight in graph_index[to_v]["links"].items():
            heapq.heappush(heap, (weight, to_v, neighbor))

    return mst_edges


mst = prim(graph_index, "C")
for edge in mst:
    print(f"{edge[1]} <-> {edge[2]}: {edge[0]}")
print(f"Sum weight: {sum(e[0] for e in mst)}")
