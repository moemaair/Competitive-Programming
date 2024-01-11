class Solution:
    def firstUniqChar(self, s: str) -> int:
        counterr = {}
        for i in range(len(s)):
            counterr[s[i]] = counterr.get(s[i],0)+1

        for k, v in counterr.items():
            if v == 1:
                return s.index(k)
        return -1     

            
        