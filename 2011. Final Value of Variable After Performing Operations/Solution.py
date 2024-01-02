class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:

        # maps = {
        #     "++X": 1,
        #     "X++": 1,
        #     "--X": -1,
        #     "X--": -1
        # }

        # res = 0

        # for i in operations:
        #     if i in maps:
        #         res+=maps[i]
        # return res        

        # ---- SPACE 0(1)-----
        result = 0
        for i in range(len(operations)):
            if(operations[i] == '++X' or operations[i] == 'X++'):
                result = result + 1
            else:
                result = result - 1
        return result

               
       
                

        