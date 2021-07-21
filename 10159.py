# 백준10159: 저울
from collections import deque

n = int(input())
m = int(input())

s = [[0] * (n + 1) for _ in range(n + 1)]


def bfs(t):
    queue = deque()
    visited = [False] * (n + 1)

    queue.append(t)
    while queue:
        now = queue.popleft()

        if not visited[now]:
            visited[now] = True
            if now != t and s[t][now] == 0:
                s[t][now] = 1
                s[now][t] = -1

            for i in range(1, n + 1):
                if (s[now][i] == 1) and (not visited[i]):
                    queue.append(i)


for _ in range(m):
    x, y = map(int, input().strip().split())
    s[x][y] = 1
    s[y][x] = -1

for target in range(1, n + 1):
    bfs(target)

for i in range(1, n + 1):
    cnt = 0
    for j in range(1, n + 1):
        if j != i and s[i][j] == 0:
            cnt += 1
    print(cnt)
