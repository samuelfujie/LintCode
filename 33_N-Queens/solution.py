class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        results = []
        if n == 0:
            return results
        self.dfs(n, [], results)
        return results
        
    
    def dfs(self, n, solution, results):
        if len(solution) == n:
            results.append(list(solution))
            return
        
        for i in range(n):
            if self.is_valid(len(solution), i, solution):
                solution.append('.' * i + 'Q' + '.' * (n - 1 - i))
                self.dfs(n, solution, results)
                solution.pop()
    
    def is_valid(self, row, column, solution):
        for i in range(len(solution)):
            x = i
            y = solution[i].find('Q')
            if column == y:
                return False
            if abs(x - row) == abs(y - column):
                return False
        return True