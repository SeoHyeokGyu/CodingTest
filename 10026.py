# 백준10026: 적록색약
from collections import deque
n = int(input())
s = []
for i in range(n):
    s.append(list(map(str, input())))

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0
cntt = 0

def bfs(i, j, v, arr):
    #queue = [[i, j]]
    #arr[i][j] = 0
    queue = deque()
    queue.append((i,j))
    while queue:
        #a, b = queue[0][0], queue[0][1]
        #del queue[0]
        now = queue.popleft()
        for k in range(4):
            #x = a + dx[k]
            #y = b + dy[k]
            x = now[0] + dx[k]
            y = now[1] + dy[k]
            if 0 <= x < n and 0 <= y < n and arr[x][y] == v:
                #queue.append([x, y])
                queue.append((x,y))
                arr[x][y] = 0


copy = [[0] * n for i in range(n)]


for i in range(n):
    for j in range(n):
        if s[i][j] == "R" or s[i][j] == "G":
            copy[i][j] = 1
        else:
            copy[i][j] = 2
for i in range(n):
    for j in range(n):
        if s[i][j] != 0:
            bfs(i, j, s[i][j], s)
            cnt += 1
        if copy[i][j] != 0:
            bfs(i, j, copy[i][j], copy)
            cntt += 1
print(cnt, cntt)
