from ast import List
from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        A = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k','l'],
            6: ['m', 'n','o'],
            7: ['p', 'q','r', 's'],
            8: ['t', 'u','v'],
            9: ['w', 'x','y', 'z']
        }
        res = []
        if len(digits) < 1:
            return res 

        temp = [int(x) for x in digits] 

        capture = []
        for k in temp:
            if k in A:
                capture.append(A[k]) 

        for combination in product(*capture):
            res.append("".join(combination))
        return res      

      


                
               



            


                