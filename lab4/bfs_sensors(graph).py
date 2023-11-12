import sys

def is_valid(x, y, M, N):
    return M > x >= 0 and N > y >= 0

def bfs(graph, start, cols):
    visited = set()
    queue = [(start, 0, [start])]
    result = []
    while queue:
        (node, dist, path) = queue.pop(0)
        if node[1] == cols - 1:
            print(path)
            return dist
        if node not in visited:
            result.append(node)
            visited.add(node)
            for neighbor in graph.get(node, {}):
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    queue.append((neighbor, dist + 1, new_path))

    return None

def find_shortest_distance(file_path):
    dist = read_input(file_path)

    with open('output.txt', 'w') as file:
        if dist != sys.maxsize:
            file.write("The shortest safe path has a length of " + str(dist))
        else:
            file.write("No route is safe to reach destination")

def read_input(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()
        matrix = [list(map(int, row.strip("\n").split(" "))) for row in lines]
        graph = {}
        rows = len(matrix)
        cols = len(matrix[0])

        r = [-1, -1, -1, 0, 0, 1, 1, 1]
        c = [-1, 0, 1, -1, 1, -1, 0, 1]
        for i in range(rows):
            for j in range(cols):
                for k in range(len(r)):
                    if matrix[i][j] == 0 and is_valid(i + r[k], j + c[k], rows, cols) \
                            and matrix[i + r[k]][j + c[k]] == 1:
                        matrix[i + r[k]][j + c[k]] = sys.maxsize

        for i in range(rows):
            for j in range(cols):
                node = (i, j)
                neighbors = []

                if matrix[i][j] == sys.maxsize:
                    matrix[i][j] = 0
                if matrix[i][j] != 0 and i > 0 and matrix[i-1][j] != 0:
                    neighbors.append((i - 1, j))
                if matrix[i][j] != 0 and  i < rows - 1 and matrix[i+1][j] != 0:
                    neighbors.append((i + 1, j))
                if matrix[i][j] != 0 and  j > 0 and matrix[i][j-1] != 0:
                    neighbors.append((i, j - 1))
                if matrix[i][j] != 0 and  j < cols - 1 and matrix[i][j+1] != 0:
                    neighbors.append((i, j + 1))

                graph[node] = neighbors

        for node in graph:
            for neighbor in graph[node]:
                if neighbor in graph and node not in graph[neighbor]:
                    graph[node].remove(neighbor)

    start_col = 0
    start_vertex = None
    for i in range(rows):
        if matrix[i][start_col] == 1:
            start_vertex = (i, start_col)
            break

    end_vertex = None
    end_col = cols-1
    for i in range(rows):
        if matrix[i][end_col] == 1:
            end_vertex = (i, end_col)
            break

    if (start_vertex is None) or (end_vertex is None):
        print("No starting(ending) vertex found in the first(last) column.")
        return -1
    elif start_vertex[0] == end_vertex[0]:
        return cols-1

    return bfs(graph, start_vertex, cols)

if __name__ == '__main__':
    find_shortest_distance("input.txt")
