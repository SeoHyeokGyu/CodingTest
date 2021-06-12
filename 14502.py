# 백준14502: 연구소
import copy
from itertools import combinations

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

graph = []

n, m = map(int, input().split())

for _ in range(n):
    graph.append(list(map(int, input().split())))


def dfs(x, y):
    graph_[x][y] = 2

    for step in range(4):
        nx = x + dx[step]
        ny = y + dy[step]

        if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
            continue
        if graph_[nx][ny] != 0:
            continue
        else:
            dfs(nx, ny)


virus = []
zeros = []

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            virus.append([i, j])
        elif graph[i][j] == 0:
            zeros.append([i, j])

zeros_combination = combinations(zeros, 3)

safety_zones = []
for com in zeros_combination:
    graph_ = copy.deepcopy(graph)

    graph_[com[0][0]][com[0][1]] = 1
    graph_[com[1][0]][com[1][1]] = 1
    graph_[com[2][0]][com[2][1]] = 1

    for v in virus:
        dfs(v[0], v[1])

    safety_zone = 0
    for row in range(n):
        for col in range(m):
            if graph_[row][col] == 0:
                safety_zone += 1
    safety_zones.append(safety_zone)

print(max(safety_zones))
