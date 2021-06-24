# 백준2589: 보물섬
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    c = [[0] * b for _ in range(a)]
    num = 0
    c[x][y] = 1
    while queue:
        now = queue.popleft()
        for k in range(4):
            nx = now[0] + dx[k]
            ny = now[1] + dy[k]
            if 0 <= nx < a and 0 <= ny < b:
                if s[nx][ny] == 'L' and c[nx][ny] == 0:
                    c[nx][ny] = c[now[0]][now[1]] + 1
                    num = max(num, c[nx][ny])
                    queue.append((nx, ny))
    return num-1


a, b = map(int, input().split())
s = [list(map(str, input())) for _ in range(a)]

cnt = 0
for i in range(a):
    for j in range(b):
        if s[i][j] == 'L':
            cnt = max(cnt, bfs(i, j))

print(cnt)
