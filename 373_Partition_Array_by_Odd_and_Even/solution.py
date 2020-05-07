class Solution:
    """
    @param: nums: an array of integers
    @return: nothing
    """
    def partitionArray(self, nums):
        if not nums:
            return nums

        odd, even = 0, len(nums) - 1

        while odd < even:
            while odd < even and nums[odd] % 2 == 1:
                odd += 1
            while odd < even and nums[even] % 2 == 0:
                even -= 1

            if odd < even:
                nums[odd], nums[even] = nums[even], nums[odd]
                odd += 1
                even -= 1
