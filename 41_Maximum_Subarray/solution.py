class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        if nums is None or len(nums) == 0:
            return 
        
        max_sum = cur_sum = nums[0]
        for num in nums[1:]:
            if cur_sum <= 0:
                cur_sum = num
            else:
                cur_sum += num
            max_sum = max(cur_sum, max_sum)
            
        return max_sum