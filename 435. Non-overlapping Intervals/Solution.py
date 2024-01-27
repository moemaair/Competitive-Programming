class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count= 0
        max_end = float('-inf')

        intervals.sort(key=lambda x: x[1])
        for start_val, end_val in intervals:
            if start_val >= max_end:
                max_end = end_val
            else:
                count+=1
        return count            