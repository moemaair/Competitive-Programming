class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        res = []
        for s in strs:
            if s.isdigit():
                res.append(int(s))
            else:
                res.append(len(s))
        return max(res)
        