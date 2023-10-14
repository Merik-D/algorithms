def binary_search_solution(N, W, H):
    left = 1
    right = max(W, H) * N

    while left < right:
        mid = (left + right)//2

        if mid//H * mid//W >= N:
            right = mid
        else:
            left = mid + 1
    return left

print(binary_search_solution(4, 1, 1))
print(binary_search_solution(10, 2, 3))
print(binary_search_solution(11, 3, 1))
print(binary_search_solution(2, 1000000000, 999999999))