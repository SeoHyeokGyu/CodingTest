# 백준2178: 미로 탐색

n, m = map(int, input().split())
s = []
queue = []
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(n):
    s.append(list(input()))

queue = [[0, 0]]

s[0][0] = 1

while queue:
    x, y = queue[0][0], queue[0][1]
    del queue[0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and s[nx][ny] == "1":
            queue.append([nx, ny])
            s[nx][ny] = s[x][y] + 1

print(s[n - 1][m - 1])
