from collections import Counter
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        
        # minimum of each row 
        # max of each elem
        lists = []

        for row in matrix:
            lists.append(min(row))
            
        for column in zip(*matrix):
            lists.append(max(column))

        count = Counter(lists)

        duplicates = [item for item, freq in count.items() if freq > 1]
       
        return duplicates