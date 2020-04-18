class Solution:
    """
    @param s: the given string
    @return: whether this string is valid
    """
    def checkValidString(self, s):
        if s is None:
            return False

        low = high = 0
        for char in s:
            if char == '(':
                low += 1
                high += 1
            if char == '*':
                low -= 1
                high += 1
            if char == ')':
                low -= 1
                high -= 1
            if high < 0:
                return False
            low = max(low, 0)

        return low == 0
