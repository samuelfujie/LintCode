class Solution:
    """
    @param maze: the map of maze
    @param start: the start points
    @param endd: the end points
    @return: Return the minimal steps
    """
    def getAns(self, maze, start, end):
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        row, col = len(maze), len(maze[0])
        visited = set([(x, y) for x, y in start])
        end_set = set([(x, y) for x, y in end])
        
        from collections import deque
        queue = deque([(x, y) for x, y in start])
        step = 0
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                visited.add((x, y))
                
                if (x, y) in end_set:
                    return step
                
                for dx, dy in DIRECTIONS:
                    nx, ny = x + dx, y + dy
                    if nx in range(0, row) and ny in range(0, col) and (nx, ny) not in visited and maze[nx][ny] == 0:
                        queue.append((nx, ny))
                        
            step += 1
        
        return step