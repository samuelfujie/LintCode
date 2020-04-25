import collections


class Solution:
    """
    @param nums: a list of integer
    @param k: an integer
    @return: return an integer, denote the number of continuous subarrays whose sum equals to k
    """
    def subarraySumEqualsK(self, nums, k):
        if not nums:
            return 0

        prefix_count = collections.defaultdict(int)
        current_prefix_sum = 0
        result = 0

        for num in nums:
            current_prefix_sum += num
            if current_prefix_sum == k:
                result += 1

            result += prefix_count[current_prefix_sum - k]
            prefix_count[current_prefix_sum] += 1

        return result
