class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        res = []
        for i in jewels:
            res.append(stones.count(i))
        return sum(res)    


             