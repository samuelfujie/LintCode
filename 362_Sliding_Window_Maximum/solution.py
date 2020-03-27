class Solution:
    """
    @param nums: A list of integers.
    @param k: An integer
    @return: The maximum number inside the window at each moving.
    """
    def maxSlidingWindow(self, nums, k):
        if not nums:
            return []
        if len(nums) <= k:
            return [max(nums)]
            
        results = []
        window = collections.deque([])
        for i in range(len(nums)):
            
            # 1) check if incoming element is greater or equal to previous element
            while window and nums[window[-1]] <= nums[i]:
                # why pop() instead of popleft()
                # e.g. [8, 4, 6, 3], k = 3
                window.pop()
            
            # 2) append this element index
            window.append(i)
            
            # 3) start to append result if window size is reached
            if i + 1 >= k:
                results.append(nums[window[0]])
            
            # 4) pop out the index that will go out of window in next loop
            if i + 1 - k >= window[0]:
                window.popleft()
                
        return results