from collections import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # WAY 1

        # space O(n)
        # x = Counter(nums)
        # for k, v in x.items():
        #     if v == max(x.values()):
        #         return k
       

        # WAY 2

        #space 0(1)

        nums.sort()
        mid = len(nums) //2

        return nums[mid]