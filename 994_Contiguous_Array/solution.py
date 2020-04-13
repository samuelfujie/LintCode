class Solution:
    """
    @param nums: a binary array
    @return: the maximum length of a contiguous subarray
    """
    def findMaxLength(self, nums):
        if not nums:
            return 0

        max_len = 0
        sum_to_first_index = {}
        sum = 0
        for i in range(len(nums)):
            sum += 1 if nums[i] == 1 else -1
            if sum == 0:
                max_len = i + 1
            elif sum in sum_to_first_index:
                max_len = max(max_len, i - sum_to_first_index[sum])
            else:
                sum_to_first_index[sum] = i

        return max_len
