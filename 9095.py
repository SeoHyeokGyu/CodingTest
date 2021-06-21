# 백준9095: 1,2,3 더하기

cnt = 0
ot = [0, 1, 2, 4]

for i in range(4, 11):
    ot.append(ot[i - 1] + ot[i - 2] + ot[i - 3])

n = int(input())
for i in range(n):
    t = int(input())
    print(ot[t])
