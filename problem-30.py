import bisect

def matrix_median(matrix):
    r = len(matrix)
    c = len(matrix[0])

    low = min(row[0] for row in matrix)
    high = max(row[-1] for row in matrix)

    desired = (r * c + 1) // 2

    while low < high:
        mid = (low + high) // 2
        count = 0

        for row in matrix:
            count += bisect.bisect_right(row, mid)

        if count < desired:
            low = mid + 1
        else:
            high = mid

    return low


# Example
matrix = [
    [1, 3, 5],
    [2, 6, 9],
    [3, 6, 9]
]

print(matrix_median(matrix))  # 5