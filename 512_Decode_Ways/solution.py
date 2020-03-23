class Solution:
    """
    @param s: a string,  encoded message
    @return: an integer, the number of ways decoding
    """
    def numDecodings(self, s):
        if not s or s[0] == '0':
            return 0
        
        prev_of_prev = 1
        prev = 1
        
        for i in range(1, len(s)):
            current = 0
            dp_i = i + 1
            
            # undecodable
            if s[i] == '0' and int(s[i - 1:i + 1])  not in range(10, 27):
                return 0
                
            if int(s[i]) in range(1,10):
                current += prev
            if int(s[i - 1:i + 1]) in range(10, 27):
                current += prev_of_prev
            
            prev_of_prev = prev
            prev = current
        
        return prev