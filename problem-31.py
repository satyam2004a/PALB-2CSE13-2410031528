def row_with_max_ones(arr):
    max_row = -1
    max_count = 0

    for i in range(len(arr)):
        count = sum(arr[i])
        if count > max_count:
            max_count = count
            max_row = i

    return max_row


# Example
arr = [
    [0, 1, 1, 1],
    [0, 0, 1, 1],
    [1, 1, 1, 1],
    [0, 0, 0, 0]
]

print(row_with_max_ones(arr))  # 2