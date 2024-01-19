
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:

        def checking(word, pattern):
            sets = set()
            maps = {}

            for w, p in zip(word, pattern):
                if w in maps:
                    
                    if maps[w] != p:
                        return False
                else:
                    if p in sets:
                        return False
                    
                    maps[w] = p
                    sets.add(p)
            return True     

        res = [word for word in words if checking(word, pattern)]   

        return res 



       