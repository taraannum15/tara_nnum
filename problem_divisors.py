x = int(input())
s = 0
for i in range(1, x + 1):
    if x % i == 0:
        s = s + i

print(s)
