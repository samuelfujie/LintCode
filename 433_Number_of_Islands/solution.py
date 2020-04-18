from collections import deque

DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        if not grid or len(grid[0]) == 0:
            return 0

        row, col = len(grid), len(grid[0])
        count = 0
        visited = set([])

        for i in range(row):
            for j in range(col):
                if (i, j) in visited or grid[i][j] == 0:
                    continue
                if grid[i][j] == 1:
                    queue = deque([(i, j)])
                    visited.add((i, j))
                    while queue:
                        x, y = queue.popleft()
                        for dx, dy in DIRECTIONS:
                            nx, ny = x + dx, y + dy
                            if nx in range(0, row) and ny in range(0, col) and grid[nx][ny] == 1 and (nx, ny) not in visited:
                                queue.append((nx, ny))
                                visited.add((nx, ny))
                    count += 1

        return count
