from ast import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
    

        # popping and inserting infront

        for i in range(k):
            a = nums.pop()
            nums.insert(0,a)

        