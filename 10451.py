# 백준10451: 순열 사이클

t = int(input())


def dfs(start):
    visited[start] = 1
    next = s[start]
    if not visited[next]:
        dfs(next)


for _ in range(t):
    n = int(input())
    s = [0] + list(map(int, input().split()))
    answer = 0
    visited = [1] + [0] * n
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
            answer += 1

    print(answer)
