class Solution:
    """
    @param nums: an array of integers
    @return: the product of all the elements of nums except nums[i].
    """
    def productExceptSelf(self, nums):
        n = len(nums)
        ans = [1] * n

        left_product = 1
        for i in range(n):
            ans[i] *= left_product
            left_product *= nums[i]

        right_product = 1
        for i in reversed(range(n)):
            ans[i] *= right_product
            right_product *= nums[i]

        return ans
