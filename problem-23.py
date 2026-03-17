arr = [1, 4, 45, 6, 0, 19]
x = 51

n = len(arr)
min_len = n + 1

for i in range(n):
    curr_sum = 0
    for j in range(i, n):
        curr_sum += arr[j]
        if curr_sum > x:
            min_len = min(min_len, j - i + 1)
            break

if min_len == n + 1:
    print(0)
else:
    print("Smallest subarray length:", min_len)