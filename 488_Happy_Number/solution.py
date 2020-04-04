class Solution:
    """
    @param n: An integer
    @return: true if this is a happy number or false
    """
    def isHappy(self, n):
        if n == 0:
            return False
        
        visited = set([n])
        while n != 1:
            n = self.getNextNumber(n)
            if n in visited:
                return False
            visited.add(n)
            
        return True
        
    def getNextNumber(self, n):
        total = 0
        while n != 0:
            digit = n % 10
            total += digit ** 2
            n //= 10
        return total