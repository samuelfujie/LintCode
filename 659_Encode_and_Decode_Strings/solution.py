class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        if strs is None or len(strs) == 0:
            return chr(258)
        return chr(257).join(strs)

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        if str == chr(258):
            return []
        return str.split(chr(257))
