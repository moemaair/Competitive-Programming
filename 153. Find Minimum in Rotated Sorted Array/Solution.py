from ast import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = nums[0]

        while l <= r:
            # checks if the first index val is our output
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            # since our req is log(n) then binary search is our todo 🤖
            mid = (l+r) //2

            # if we have only 2 index [2,1] then we return the mid i.e 1 in this case
            res = min(res, nums[mid])

            
            if nums[mid] >= nums[l]:
                l = mid + 1
            elif nums[mid] <= nums[l]:
                r = mid - 1
        return res                

         


        