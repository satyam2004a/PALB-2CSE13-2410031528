def median_of_array(arr):
    arr.sort()
    n = len(arr)

    if n % 2 == 1:
        return arr[n // 2]
    else:
        return (arr[n // 2 - 1] + arr[n // 2]) / 2


# Example
print(median_of_array([90, 100, 78, 89, 67]))  # 89