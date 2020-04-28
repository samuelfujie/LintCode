import collections


class Solution:
    """
    @param nums: a continuous stream of numbers
    @param number: a number
    @return: returns the first unique number
    """
    def firstUniqueNumber(self, nums, number):
        num_counter = collections.defaultdict(int)

        for num in nums:
            num_counter[num] += 1
            if num == number:
                break
        else:
            return -1

        for num in nums:
            if num_counter[num] == 1:
                return num
            if num == number:
                break

        return -1
