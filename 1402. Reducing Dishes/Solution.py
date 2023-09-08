from collections import List
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse = True)
        total, res = 0 , 0

        for i in range(len(satisfaction)):
            if len(satisfaction) < 0:
                return 0
            else:
                total+=satisfaction[i]    
                if total < 0:
                    break
                else:
                    res+=total
        return res                