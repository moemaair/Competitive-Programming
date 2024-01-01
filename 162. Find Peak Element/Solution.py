from ast import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # return nums.index(max(nums))

        maxi = float('-inf')

        for i in nums:
            maxi = max(maxi, i)
        return (nums.index(maxi))   

        
 

         

       
        