def build_graph(levels):
    graph = {}

    for i in range(len(levels) - 1):
        for j in range(len(levels[i])):
            current_vertex = (i, j)
            next_level = i + 1
            neighbors = [(next_level, j), (next_level, j + 1)]
            graph[current_vertex] = neighbors

    return graph


def max_experience(graph, levels):
    stack = [((0, 0), levels[0][0])]
    max_experience = 0

    while stack:
        current_vertex, current_experience = stack.pop()
        current_level, current_position = current_vertex
        if current_level == len(levels) - 1:
            max_experience = max(max_experience, current_experience)
        else:
            for neighbor_vertex in graph[current_vertex]:
                stack.append((neighbor_vertex, current_experience + levels[neighbor_vertex[0]][neighbor_vertex[1]]))

    return max_experience


def read_from_file(file_path):
    with open(file_path, 'r') as file:
        levels_count = int(file.readline().strip())
        levels = []
        for _ in range(levels_count):
            level_data = list(map(int, file.readline().split()))
            levels.append(level_data)
    return levels


def write_to_file(file_path, result):
    with open(file_path, 'w') as file:
        file.write(str(result))


if __name__ == "__main__":

    levels = read_from_file('../input.txt')
    print(levels)
    graph = build_graph(levels)
    result = max_experience(graph, levels)
    write_to_file('../output.txt', result)
