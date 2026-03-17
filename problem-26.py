arr = [111, 222, 333, 444, 555]

def is_palindrome(num):
    return str(num) == str(num)[::-1]

flag = True
for num in arr:
    if not is_palindrome(num):
        flag = False
        break

print(flag)