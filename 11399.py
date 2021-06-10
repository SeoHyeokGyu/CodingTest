# 백준11399: ATM

number = int(input())
time = list(map(int, input().split()))

result = 0
total = 0
time.sort()
for j in range(number+1):
    for i in range(j):
        result = time[i] + result
    total = total + result
    result = 0

print(total)

