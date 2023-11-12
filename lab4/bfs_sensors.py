import sys

row = [-1, 0, 0, 1]
col = [0, -1, 1, 0]

def is_safe(field, visited, x, y):
    return field[x][y] == 1 and not visited[x][y]

def is_valid(x, y, M, N):
    return M > x >= 0 and N > y >= 0

def bfs(field):
    (M, N) = (len(field), len(field[0]))
    visited = [[False for x in range(N)] for y in range(M)]
    queue = []

    for r in range(M):

        if field[r][0] == 1:
            queue.append((r, 0, 0))
            visited[r][0] = True

    while queue:
        (i, j, dist) = queue.pop(0)
        if j == N - 1:
            return write_in_file(dist)

        for k in range(len(row)):
            if (is_valid(i + row[k], j + col[k], M, N) and
                    is_safe(field, visited, i + row[k], j + col[k])):
                visited[i + row[k]][j + col[k]] = True
                queue.append((i + row[k], j + col[k], dist + 1))

    return write_in_file(sys.maxsize)

def read_from_file(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()
        mat = [list(map(int, row.strip("\n").split(" "))) for row in lines]

    return mat

def write_in_file(dist):
    with open('output.txt', 'w') as file:
        if dist != sys.maxsize:
            file.write("The shortest safe path has a length of " + str(dist))
        else:
            file.write("No route is safe to reach destination")

def find_shortest_distance(file_path):
    mat = read_from_file(file_path)
    print(mat)

    if not mat or not len(mat):
        return 0

    (M, N) = (len(mat), len(mat[0]))

    r = [-1, -1, -1, 0, 0, 1, 1, 1]
    c = [-1, 0, 1, -1, 1, -1, 0, 1]

    for i in range(M):
        for j in range(N):
            for k in range(len(r)):
                if mat[i][j] == 0 and is_valid(i + r[k], j + c[k], M, N) \
                        and mat[i + r[k]][j + c[k]] == 1:
                    mat[i + r[k]][j + c[k]] = sys.maxsize

    for i in range(M):
        for j in range(N):
            if mat[i][j] == sys.maxsize:
                mat[i][j] = 0

    return bfs(mat)

if __name__ == '__main__':
    find_shortest_distance("input.txt")