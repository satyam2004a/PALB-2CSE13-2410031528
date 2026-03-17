def search_matrix(matrix, target):
    if not matrix:
        return False

    m = len(matrix)
    n = len(matrix[0])

    left, right = 0, m * n - 1

    while left <= right:
        mid = (left + right) // 2
        row = mid // n
        col = mid % n

        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


# Example
matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]

print(search_matrix(matrix, 3))  # True
print(search_matrix(matrix, 13)) # False