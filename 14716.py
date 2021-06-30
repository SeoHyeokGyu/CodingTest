# 백준14716: 현수막

from collections import deque

m, n = map(int, input().split())

s = [list(map(int, input().split())) for _ in range(m)]
visited = [[False for _ in range(n)] for _ in range(m)]

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, 1, -1, -1, 1, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    visited[x][y] = True

    while queue:
        now = queue.popleft()

        for i in range(8):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    if s[nx][ny] == 1:
                        queue.append([nx, ny])


cnt = 0

for i in range(m):
    for j in range(n):
        if not visited[i][j] and s[i][j] == 1:
            cnt += 1
            bfs(i, j)

print(cnt)
