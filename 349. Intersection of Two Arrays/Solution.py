from ast import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

    #-------- bruteforce---------
    
        # uniq1 = list(set(nums1)) 
        # uniq2 = list(set(nums2)) 
        # l = []
        # for i in uniq1:
        #     for j in uniq2:
        #         if i == j:
        #             l.append(i)
        # return l   


        #-------- optimization---------

        uniq_nums1 = set(nums1)
        common_values = set()

        for i in nums2:
            if i in uniq_nums1:
               common_values.add(i)
        return  common_values    

