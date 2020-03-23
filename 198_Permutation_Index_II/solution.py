import math
class Solution:
    """
    @param A: An array of integers
    @return: A long integer
    """
    def permutationIndexII(self, A):
        n = len(A)
        permutation_counter = 0
        counter = {}
        for i in reversed(range(n)):
            counter[A[i]] = counter.get(A[i], 0) + 1
            
            sml_ele_set = set([])
            for num in counter:
                if num < A[i]:
                    sml_ele_set.add(num)
            
            for sml_ele in sml_ele_set:
                counter[sml_ele] -= 1
                
                # the number of permutation with repetition:
                # n! / (n1!*n2!*...*nk!) where (1,2,...,k) is cardinality
                total_permutations = math.factorial(n - i - 1)
                for num in counter:
                    total_permutations //= math.factorial(counter[num])
                    
                permutation_counter+= total_permutations
                # back tracking
                counter[sml_ele] += 1
                
        return permutation_counter + 1