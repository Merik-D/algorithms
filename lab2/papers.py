def find_min_board_size(N, W, H):
    min_side = min(W, H) * N
    for i in range(2, N + 1):
        cols = N // i
        rows = i

        if N % i != 0:
            if H > W:
                cols += 1
            else:
                rows += 1

        current_side = max(W * cols, H * rows)
        min_side = min(min_side, current_side)

    return min_side


print(find_min_board_size(4, 1, 1))
print(find_min_board_size(10, 2, 3))
print(find_min_board_size(11, 3, 1))
print(find_min_board_size(2, 1000000000, 999999999))