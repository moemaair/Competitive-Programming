class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:


        #--------brute force--------
        # counter = 0
     
        # for i in range(0, len(t)):    
        #     if s[counter] == t[i]:
        #        counter+=1 
        # return counter == len(s)        


        #--------optimized--------
        i = 0
        j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        if i == len(s):
            return True  
        else:
            return False           


        
