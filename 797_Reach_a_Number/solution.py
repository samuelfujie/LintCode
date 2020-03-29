class Solution:
    """
    @param target: the destination
    @return: the minimum number of steps
    """
    def reachNumber(self, target):
        target = abs(target)
        n = 0
        
        while target > 0:
            n += 1
            target -= n
            
        diff = abs(target)
        if diff % 2 == 0:
            return n
        if (diff + n + 1) % 2 == 0:
            return n + 1
        return n + 2