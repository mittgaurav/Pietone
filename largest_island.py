# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 15:01:38 2019

@author: gaurav
"""

area = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

visited = [[0 for _ in range(len(area[0]))] for _ in range(len(area))]


def count(i, j):
    """count max of
    continuous 1"""
    if i < 0 or i >= len(area) or j < 0 or j >= len(area[i]):
        return 0

    if visited[i][j]:  # already
        return 0

    visited[i][j] = True
    if not area[i][j]:  # zero
        return 0

    return (1 + count(i, j+1) + count(i, j-1) +
            count(i+1, j) + count(i-1, j))  # 4 direction


res = 0
for i in range(len(area)):
    for j in range(len(area[i])):
        res = max(res, count(i, j))

print(res)


area = [[0, 0, 1, 2, 2, 0, 3],
        [0, 1, 1, 2, 3, 3, 3],
        [2, 2, 2, 2, 4, 4, 3],
        [0, 2, 1, 2, 4, 2, 1],
        [4, 0, 1, 1, 3, 3, 3],
        [2, 0, 0, 2, 3, 0, 3],
        [1, 0, 1, 1, 3, 0, 3],
        [1, 1, 0, 2, 3, 3, 3]]

visited = [[0 for _ in range(len(area[0]))] for _ in range(len(area))]


def count_nation(i, j, val):
    """for multiple options,
    give the largest nation"""
    if i < 0 or i >= len(area) or j < 0 or j >= len(area[i]):
        return 0

    if visited[i][j]:  # already
        return 0

    # can add to current nation?
    if area[i][j] != val:
        return 0

    visited[i][j] = True
    return (1 + count_nation(i, j+1, val) + count_nation(i, j-1, val) +
            count_nation(i+1, j, val) + count_nation(i-1, j, val))


res = 0
for i in range(len(area)):
    for j in range(len(area[i])):
        res = max(res, count_nation(i, j, area[i][j]))

print(res)


def count_islands(arr):
    # using BFS
    from collections import deque
    q = deque()
    visited = [[0 for _ in range(len(arr[0]))] for _ in range(len(arr))]
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if visited[i][j] or not arr[i][j]: continue
            q.append((i, j))
            while q:
                x, y = q.popleft()
                if visited[x][y]: continue
                visited[x][y] = 1
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    if 0 <= x+dx < len(arr) and 0 <= y+dy < len(arr[0]):
                        if not visited[x+dx][y+dy] and arr[x+dx][y+dy]:
                            q.append((x+dx, y+dy))
            count += 1
    return count


def max_island(arr):
    """
    Traverse the matrix checking if this node
    is start of a new island. If yes, use BFS
    to continue till this island is available.
    When the island is exhausted; i.e., queue
    is empty, continue search for next island.
    """
    from collections import deque
    q = deque()
    visited = [[0 for _ in range(len(arr[0]))] for _ in range(len(arr))]
    mx = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            this = 0
            if visited[i][j] or not arr[i][j]: continue
            q.append((i, j))
            while q:
                x, y = q.popleft()
                if visited[x][y]: continue
                visited[x][y] = 1
                this += 1
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    # four directions from current location.
                    # Don't go less or more than array size
                    if 0 <= x+dx < len(arr) and 0 <= y+dy < len(arr[0]):
                        if not visited[x+dx][y+dy] and arr[x+dx][y+dy]:
                            q.append((x+dx, y+dy))
            mx = max(mx, this)
    return mx


print(f"max_island: {max_island(area)}, count_islands:{count_islands(area)}")
area = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
print(f"max_island: {max_island(area)}, count_islands:{count_islands(area)}")
area =  [[1, 0, 1, 1, 0, 0, 0],
         [1, 0, 1, 0, 1, 0, 0],
         [0, 1, 0, 0, 0, 1, 1]]
print(f"max_island: {max_island(area)}, count_islands:{count_islands(area)}")


def paths(i, j, n):
    """given a rectangular/square board,
    tell how many ways can we traverse.
    This only allows going down or right"""
    if i == n - 1 and j == n - 1:
        return 1

    def f1():
        if i < n - 1 and j < n - 1:
            return paths(i + 1, j, n) + paths(i, j + 1, n)
        if i == n - 1 and j < n - 1:
            return paths(i, j + 1, n)
        if i < n - 1 and j == n - 1:
            return paths(i+1, j, n)

    def f2():
        """less code but slower
        because of recursion"""
        if i > n or j > n:
            return 0
        return paths(i + 1, j, n) + paths(i, j + 1, n)

    return f1()


print(paths.__name__)
print(2, paths(0, 0, 2))
print(3, paths(0, 0, 3))
print(7, paths(0, 0, 7))
print(10, paths(0, 0, 10))

scores = None


def path_all_direction(i, j, n):
    """given a rectangular/square board,
    tell how many ways can we traverse.
    We can go in any direction"""
#    if scores[i][j] != -1:  # memoization
#        return scores[i][j]

    if i == n-1 and j == n-1:
        return 1

    visited[i][j] = True

    def allowed(ii, jj):
        if ii < 0 or ii >= n:
            return False
        if jj < 0 or jj >= n:
            return False

        return True

    res = 0
    if allowed(i+1, j) and not visited[i+1][j]:
        res += path_all_direction(i+1, j, n)
    if allowed(i, j+1) and not visited[i][j+1]:
        res += path_all_direction(i, j+1, n)
    if allowed(i-1, j) and not visited[i-1][j]:
        res += path_all_direction(i-1, j, n)
    if allowed(i, j-1) and not visited[i][j-1]:
        res += path_all_direction(i, j-1, n)

    visited[i][j] = False
    scores[i][j] = res
    return res


print(path_all_direction.__name__)
N = 4
scores = [[-1 for _ in range(N)] for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]
print(path_all_direction(0, 0, N))
