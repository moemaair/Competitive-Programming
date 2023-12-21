class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        splitt = s.split()
          
        my_maps = {}
        my_maps2 = {}

        if len(splitt) != len(pattern):
            return False
    
        for c, w in zip(pattern, splitt):
            my_maps[c] = w
            my_maps2[w] = c
            
        check1 = list(my_maps.keys())
        check2 = list(my_maps2.values())

        if check1 == check2:
            return True
        else:
            return False
