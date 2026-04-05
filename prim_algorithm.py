base_graph = [
    {"point": "A", "links": {"B": 3, "F": 2}},
    {"point": "B", "links": {"A": 3, "G": 6, "C": 3}},
    {"point": "C", "links": {"B": 3, "G": 1, "E": 2, "D": 3}},
    {"point": "D", "links": {"C": 3, "E": 5}},
    {"point": "E", "links": {"D": 5, "C": 2, "G": 3, "F": 4}},
    {"point": "F", "links": {"A": 2, "E": 4, "G": 3}},
    {"point": "G", "links": {"B": 6, "C": 1, "E": 3, "F": 3}},
]


def find_nearest_vertex(base_graph, vertexes, weights):
    current_nearest_vertex = None
    for vertex in vertexes:
        links = vertex.get("links")
        for key, value in links.items():
            if current_nearest_vertex is None:
                if (
                    f"{vertex.get('point')}{key}" not in weights
                    and f"{key}{vertex.get('point')}" not in weights
                ):
                    current_nearest_vertex = (vertex.get("point"), key, value)
            elif value < current_nearest_vertex[2]:
                if (
                    f"{vertex.get('point')}{key}" not in weights
                    and f"{key}{vertex.get('point')}" not in weights
                ):
                    current_nearest_vertex = (vertex.get("point"), key, value)
    if current_nearest_vertex is not None:
        for item in base_graph:
            if current_nearest_vertex[1] == item.get("point"):
                weights.append(f"{item.get('point')}{current_nearest_vertex[0]}")
                vertexes.append(item)
                return item


weights = []
vertexes = []
vertexes.append(base_graph[2])

while len(vertexes) < len(base_graph):
    find_nearest_vertex(base_graph, vertexes, weights)

print(weights)
print(vertexes)
