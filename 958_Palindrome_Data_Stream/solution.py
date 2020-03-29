class Solution:
    """
    @param s: The data stream
    @return: Return the judgement stream
    """
    def getStream(self, s):
        odd_number_set = set([])
        results = []
        for letter in s:
            if letter in odd_number_set:
                odd_number_set.discard(letter)
            else:
                odd_number_set.add(letter)
            results.append(1 if len(odd_number_set) < 2 else 0 )
        return results