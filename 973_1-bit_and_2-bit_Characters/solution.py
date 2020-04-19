class Solution:
    """
    @param bits: a array represented by several bits.
    @return: whether the last character must be a one-bit character or not
    """
    def isOneBitCharacter(self, bits):
        if not bits:
            return False

        i = 0
        while i < len(bits) - 1:
            i += 1 if bits[i] == 0 else 2

        return i == len(bits) - 1
