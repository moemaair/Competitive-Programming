from ast import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result = []
        visited = set()

        def backtrack(currentpath):
            if len(currentpath) == len(nums):
                result.append(currentpath)
            for i in range(len(nums)):
                if i not in visited:
                    visited.add(i)
                    backtrack(currentpath + [nums[i]])
                    visited.remove(i)
        backtrack([])

        return result      

                    

                 

        