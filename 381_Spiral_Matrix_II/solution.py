class Solution:
    """
    @param n: An integer
    @return: a square matrix
    """
    def generateMatrix(self, n):
        if not n:
            return []
            
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        number = 1
        top = left = 0
        bottom = right = n - 1
        direction = 0
        
        while True:
            if direction == 0:
                for i in range(left, right + 1):
                    matrix[top][i] = number
                    number += 1
                top += 1
            if direction == 1:
                for i in range(top, bottom + 1):
                    matrix[i][right] = number
                    number += 1
                right -= 1
            if direction == 2:
                for i in range(right, left - 1, -1):
                    matrix[bottom][i] = number
                    number += 1
                bottom -= 1
            if direction == 3:
                for i in range(bottom, top - 1, -1):
                    matrix[i][left] = number
                    number += 1
                left += 1
            if left > right or top > bottom:
                return matrix
            direction =(direction + 1) % 4