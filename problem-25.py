arr = [2, 1, 5, 6, 3]
k = 3

count = 0
for i in arr:
    if i <= k:
        count += 1

bad = 0
for i in range(count):
    if arr[i] > k:
        bad += 1

ans = bad
j = count

for i in range(len(arr) - count):
    if arr[i] > k:
        bad -= 1
    if arr[j] > k:
        bad += 1
    ans = min(ans, bad)
    j += 1

print("Minimum swaps:", ans)