# 백준3184: 양

r, c = map(int, input().split())


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[0] * c for _ in range(r)]
queue = []
s = []

for _ in range(r):
    s.append(list(map(str, input())))


def bfs(x, y):
    global wolf, sheep
    visited[x][y] = 1

    queue.append([x, y])
    while queue:
        x, y = queue[0][0], queue[0][1]
        del queue[0]

        if s[x][y] == "v":
            wolf += 1

        elif s[x][y] == "o":
            sheep += 1

        for step in range(4):
            nx = x + dx[step]
            ny = y + dy[step]
            if 0 <= nx < r and 0 <= ny < c and s[nx][ny] != "#" and visited[nx][ny] == 0:
                queue.append([nx,ny])
                visited[nx][ny] = 1


total_wolf = 0
total_sheep = 0

for i in range(r):
    for j in range(c):
        if s[i][j] != "#" and visited[i][j] == 0:
            wolf = 0
            sheep = 0
            bfs(i, j)
            if wolf >= sheep:
                sheep = 0
            else:
                wolf = 0

            total_wolf += wolf
            total_sheep += sheep

print(total_sheep, total_wolf)
