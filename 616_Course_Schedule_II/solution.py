from collections import deque
class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, n, prerequisites):
        prerequisite = {}
        degree = [0] * n
        for p in prerequisites:
            prerequisite[p[1]] = prerequisite.get(p[1], []) + [p[0]]
            degree[p[0]] += 1
        
        q = deque([])
        for i in range(n):
            if degree[i] == 0:
                q.append(i)
        
        res = []
        while q:
            current_class = q.popleft()
            res.append(current_class)
           
            if len(res) == n:
                return res
            
            if current_class in prerequisite:
                for cls in prerequisite[current_class]:
                    degree[cls] -= 1
                    if degree[cls] == 0:
                        q.append(cls)
        return []