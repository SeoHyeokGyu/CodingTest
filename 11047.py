# 백준11047: 동전 0


n, k = map(int, input().split())
coin = []
for i in range(n):
    coin.append(int(input()))

result = 0


while k > 0 :
    c = coin.pop()
    result += k // c
    k %= c

print(result)
