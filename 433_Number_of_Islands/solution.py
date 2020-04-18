from collections import deque


class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0

        row, col = len(grid), len(grid[0])
        count = 0
        visited = set([])
        DIRECT = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for x in range(row):
            for y in range(col):
                if grid[x][y] == 0:
                    continue
                if (x, y) in visited:
                    continue

                #bfs
                queue = deque([(x, y)])
                while queue:
                    i, j = queue.popleft()
                    visited.add((i, j))
                    for di, dj in DIRECT:
                        if i + di < 0 or i + di >= row or j + dj < 0 or j + dj >= col:
                            continue
                        if (i + di, j + dj) in visited:
                            continue
                        if grid[i + di][j + dj] == 1:
                            queue.append((i + di, j + dj))
                            visited.add((i + di, j + dj))
                count += 1

        return count
