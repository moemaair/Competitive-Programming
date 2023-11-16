from ast import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = []
        for i in range(len(nums)):
            curr = nums[i][i] 
            if curr == '1':
               res.append("0")
            else:
                res.append("1")   
        return "".join(res)        


        