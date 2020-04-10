class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        numbers.sort()
        results = []
        
        for i in range(len(numbers) - 2):
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            
            target = 0 - numbers[i]
            j, k = i + 1, len(numbers) - 1
            
            while j < k:
                if numbers[j] + numbers[k] < target:
                    j += 1
                elif numbers[j] + numbers[k] > target:
                    k -= 1
                else:
                    results.append([numbers[i], numbers[j], numbers[k]])
                    j += 1
                    k -= 1
                    while j < k and numbers[j] == numbers[j - 1]:
                        j += 1
                    while j < k and numbers[k] == numbers[k + 1]:
                        k -= 1
                        
        return results