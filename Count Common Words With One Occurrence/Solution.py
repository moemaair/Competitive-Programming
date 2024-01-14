class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        #return the keys that have 1 values in word1 and word2
        maps1 = {}
        maps2 = {}
        counter = 0

        for i in words1:
            maps1[i] = maps1.get(i,0) + 1
            
        for i in words2:
            maps2[i] = maps2.get(i,0) + 1
        
        for k in maps2.keys():
            if maps1.get(k) == maps2.get(k) == 1:
                counter += 1
        return counter   

         
       
                