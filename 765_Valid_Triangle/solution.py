class Solution:
    """
    @param a: a integer represent the length of one edge
    @param b: a integer represent the length of one edge
    @param c: a integer represent the length of one edge
    @return: whether three edges can form a triangle
    """
    def isValidTriangle(self, a, b, c):
        return a + b > c and a + c > b and b + c > a