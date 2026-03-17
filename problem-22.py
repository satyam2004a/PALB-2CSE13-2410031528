arr = [3, 4, 1, 9, 56, 7, 9, 12]
m = 5

arr.sort()
n = len(arr)
min_diff = float('inf')

for i in range(n - m + 1):
    diff = arr[i + m - 1] - arr[i]
    min_diff = min(min_diff, diff)

print("Minimum difference:", min_diff)