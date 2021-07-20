# 백준13460: 구슬 탈출 2
from collections import deque

n, m = map(int, input().split())

s = []
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for i in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def move(nx, ny, dx, dy):
    cnt = 0
    while s[nx][ny] != 'O' and s[nx + dx][ny + dy] != '#':
        nx += dx
        ny += dy
        cnt += 1
    return nx, ny, cnt


def bfs(rx, ry, bx, by):
    queue = deque()
    queue.append([rx, ry, bx, by, 1])
    visited[rx][ry][bx][by] = True

    while queue:
        now = queue.popleft()
        if now[4] > 10:
            break

        for i in range(4):
            nrx, nry, rcnt = move(now[0], now[1], dx[i], dy[i])
            nbx, nby, bcnt = move(now[2], now[3], dx[i], dy[i])
            if s[nbx][nby] != 'O':
                if s[nrx][nry] == 'O':
                    print(now[4])
                    return
                if nrx == nbx and nry == nby:
                    if rcnt > bcnt:
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby] = True
                    queue.append([nrx, nry, nbx, nby, now[4] + 1])
    print(-1)


for i in range(n):
    t = list(input())
    s.append(t)
    for j in range(m):
        if t[j] == 'R':
            rx, ry = i, j
        if t[j] == 'B':
            bx, by = i, j

bfs(rx, ry, bx, by)
