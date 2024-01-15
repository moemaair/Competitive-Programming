class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
    
        res = list(zip(names,heights))

        sorted_res = sorted(res, key=lambda x: x[1], reverse = True)

        sol = []
        for i in sorted_res:
            sol.append(i[0])
        return sol    
    