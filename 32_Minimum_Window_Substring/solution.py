from collections import Counter
class Solution:
    """
    @param source : A string
    @param target: A string
    @return: A string denote the minimum window, return "" if there is no such a string
    """
    def minWindow(self, source , target):
        if not source or not target or len(source) < len(target):
            return ""
            
        word_dict = dict(Counter(target))
        match_count = 0
        min_len = start_index = None
        slow = 0
        
        for fast in range(len(source)):
            char = source[fast]
            if char not in target:
                continue
            word_dict[char] -= 1
            
            # match a letter
            if word_dict[char] == 0:
                match_count += 1
            
            while match_count == len(word_dict):
                # find a valid string
                if min_len is None or min_len > fast - slow + 1:
                    min_len = fast - slow + 1
                    start_index = slow
                left_char = source[slow]
                slow += 1
                if left_char not in word_dict:
                    continue
                word_dict[left_char] += 1
                if word_dict[left_char] == 1:
                    match_count -= 1
        
        return "" if min_len is None else source[start_index: start_index + min_len]