class Solution:
    """
    @param length: the length of the array
    @param updates: update operations
    @return: the modified array after all k operations were executed
    """
    def getModifiedArray(self, length, updates):
        ops = [0] * (length + 1)
        for start, end, inc in updates:
            ops[start] += inc
            ops[end + 1] -= inc
        
        for i in range(1, length):
            ops[i] += ops[i - 1]
        
        return ops[:-1]