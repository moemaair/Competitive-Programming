from ast import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        unique_number = set(x for x in nums)

        if not unique_number:
            return 0
         
        current = 0

        while current in unique_number:
            current+=1
        return current   
        