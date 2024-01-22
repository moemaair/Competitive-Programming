class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        seen = set()
        missing = 1
        res = []

        while missing in nums:
            missing+=1    
        for num in nums:
            if num in seen:
                res.append(num)
            seen.add(num)
        res.append(missing)

        return res        

        