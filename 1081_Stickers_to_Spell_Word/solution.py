import sys
class Solution:
    """
    @param stickers: a string array
    @param target: a string
    @return: the minimum number of stickers that you need to spell out the target
    """
    def minStickers(self, stickers, target):
        answer = sys.maxsize
        counter = collections.Counter(target)
        
        def dfs(collected, used, i):
            nonlocal answer, counter
            
            if i == len(target):
                answer = min(answer, used)
                return
            
            next_char = target[i]
            # if we have already collected next character
            if collected[next_char] >= counter[next_char]:
                dfs(collected, used, i + 1)
            elif used + 1 < answer:
                for sticker in stickers:
                    if next_char in sticker:
                        for char in sticker:
                            collected[char] += 1
                        dfs(collected, used + 1, i + 1)
                        # backtracking
                        for char in sticker:
                            collected[char] -= 1
        
        dfs(collections.defaultdict(int), 0, 0)
        return answer if answer < sys.maxsize else -1