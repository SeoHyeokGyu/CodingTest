# 백준16948: 데스 나이트
from collections import deque

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]




def bfs(n, r1, c1, r2, c2):
    board = [[-1 for _ in range(n)] for _ in range(n)]
    visited = [[False for _ in range(n)] for _ in range(n)]

    board[r1][c1] = 0
    visited[r1][c1] = True

    queue = deque()
    queue.append((r1, c1))
    cnt = 0

    while queue:
        cnt+=1

        for _ in range(len(queue)):
            front = queue.popleft()

            for i in range(6):
                nx = front[0] + dx[i]
                ny = front[1] + dy[i]
                if nx == r2 and ny == c2:
                    return cnt

                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    return -1

n = int(input())
x1, y1, x2, y2 = map(int, input().split())

print(bfs(n, x1, y1, x2, y2))
