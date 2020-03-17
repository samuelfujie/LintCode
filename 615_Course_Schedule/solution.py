from collections import deque
class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def canFinish(self, numCourses, prerequisites):
        preCount = [0] * numCourses
        as_pre_of = {}
        for prerequisite in prerequisites:
            preCount[prerequisite[0]] += 1
            as_pre_of[prerequisite[1]] = as_pre_of.get(prerequisite[1], []) + [prerequisite[0]]
        
        queue = deque([])
        
        for index in range(len(preCount)):
            if preCount[index] == 0:
                queue.append(index)
        
        while queue:
            index = queue.popleft()
            if index in as_pre_of:
                for cls in as_pre_of[index]:
                    preCount[cls] -= 1
                    if preCount[cls] == 0:
                        queue.append(cls)
        
        return sum(preCount) == 0