class Solution:
    """
    @param S: string S
    @param T: string T
    @return: Backspace String Compare
    """
    def backspaceCompare(self, S, T):
        rs, rt = len(S) - 1, len(T) - 1
        count_s = count_t = 0
        
        while rs >= 0 or rt >= 0:
            while rs >= 0:
                if S[rs] == '#':
                    count_s += 1
                    rs -= 1
                elif count_s:
                    count_s -= 1
                    rs -= 1
                else:
                    break
            
            while rt >= 0:
                if T[rt] == '#':
                    count_t += 1
                    rt -= 1
                elif count_t:
                    count_t -= 1
                    rt -= 1
                else:
                    break
                
            if rs < 0 or rt < 0:
                return rs == -1 and rt == -1
                
            if S[rs] != T[rt]:
                return False
            
            rs -= 1
            rt -= 1
        
        return True