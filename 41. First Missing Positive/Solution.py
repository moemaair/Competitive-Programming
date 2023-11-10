class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        unique_number = set(x for x in nums if x > 0)
        current = 1

        while current in unique_number:
            current+=1
        return current  
        