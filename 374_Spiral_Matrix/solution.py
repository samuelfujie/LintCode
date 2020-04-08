class Solution:
    """
    @param matrix: a matrix of m x n elements
    @return: an integer list
    """
    def spiralOrder(self, matrix):
        results = []
        if not matrix or matrix[0] == 0:
            return results
        
        m, n = len(matrix), len(matrix[0])
        
        top, bottom = 0, m - 1
        left, right = 0, n - 1
        
        direction = 0
        while True:
            if direction == 0:
                for i in range(left, right + 1):
                    results.append(matrix[top][i])
                top += 1
            if direction == 1:
                for i in range(top, bottom + 1):
                    results.append(matrix[i][right])
                right -= 1
            if direction == 2:
                for i in range(right, left - 1, -1):
                    results.append(matrix[bottom][i])
                bottom -= 1
            if direction == 3:
                for i in range(bottom, top - 1, -1):
                    results.append(matrix[i][left])
                left += 1
            if top > bottom or left > right: 
                return results
            direction = (direction + 1) % 4