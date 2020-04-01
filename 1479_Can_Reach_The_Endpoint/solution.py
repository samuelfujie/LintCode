from collections import deque
class Solution:
    """
    @param map: the map
    @return: can you reach the endpoint
    """
    def reachEndpoint(self, map):
        if not map or map[0] == 0:
            return False
        m, n = len(map), len(map[0])
        
        queue = deque([(0, 0)])
        visited = set([])
        while queue:
            x, y = queue.popleft()
            
            if map[x][y] == 9:
                return True
            visited.add((x, y))
            
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = dx + x, dy + y
                if nx in range(0, m) and ny in range(0, n) and (nx, ny) not in visited:
                    if map[nx][ny] != 0:
                        queue.append((nx, ny))
        return False