class Solution:
    """
    @param nums: An array of integers
    @return: An integer
    """
    
    """
    Solution 1: In-place Swapping
    """
    # def findMissing(self, nums):
    #     if not nums:
    #         return 0
        
    #     index = 0
    #     while index < len(nums):
    #         position = nums[index]
    #         if position not in range(len(nums)) or position == index or position == nums[position]:
    #             index += 1
    #             continue
    #         nums[index], nums[position] = nums[position], nums[index]
            
    #     for i in range(len(nums)):
    #         if i != nums[i]:
    #             return i
    #     return len(nums)
    
    """
    Solution 2: Bit Operation
    """
    # def findMissing(self, nums):
    #     missing = len(nums)
    #     for i, n in enumerate(nums):
    #         missing ^= i ^ n
    #     return missing
    
    """
    Solution 3: Sum of an Arithmetic Series
    """
    def findMissing(self, nums):
        total = sum(nums)
        expect = len(nums) * (len(nums) + 1) // 2
        return expect - total