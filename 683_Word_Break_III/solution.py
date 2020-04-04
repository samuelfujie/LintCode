class Solution:
    """
    @param: : A string
    @param: : A set of word
    @return: the number of possible sentences.
    """

    def wordBreak3(self, s, dict):
        lower_dict = set([word.lower() for word in dict ])
        n = len(s)
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        
        for i in range(n):
            count = 0
            for j in range(i + 1):
                if s[j: i + 1].lower() in lower_dict:
                    count += dp[j]
            dp[i + 1 ] = count
            
        return dp[-1]