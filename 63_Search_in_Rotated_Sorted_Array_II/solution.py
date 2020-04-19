class Solution:
    """
    @param A: an integer ratated sorted array and duplicates are allowed
    @param target: An integer
    @return: a boolean
    """
    def search(self, nums, target):
        if not nums:
            return False

        start, end = 0, len(nums) - 1

        while start + 1 < end:
            while start + 1 < end and nums[start] == nums[end]:
                start += 1

            mid = (start + end) // 2
            if nums[mid] == target:
                return True

            if nums[start] <= nums[mid]:
                if nums[start] <= target <= nums[mid]:
                    end = mid
                else:
                    start = mid
            else:
                if nums[mid] <= target <= nums[end]:
                    start = mid
                else:
                    end = mid

        return True if nums[start] == target or nums[end] == target else False
