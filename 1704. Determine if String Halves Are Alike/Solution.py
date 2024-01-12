class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a = len(s) // 2

        vowel = "aeiou"
        countera = 0
        counterb = 0

        for i in s[a:].lower():
            if i in vowel:
                countera+=1
                
        for i in s[:a].lower():
            if i in vowel:
                counterb+=1        

        if countera != counterb:
            return False
        else:
            return True    
                