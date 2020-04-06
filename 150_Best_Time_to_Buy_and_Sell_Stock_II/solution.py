class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        profit = 0
        expense = None
        for p in prices:
            if expense is not None and p > expense:
                profit += p - expense
            expense = p
        return profit