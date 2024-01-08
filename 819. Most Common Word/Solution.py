from ast import List
import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        maps = {}
        splitted_words = re.split("[,.!?;'\s]+", paragraph )

        alphabets_only = [''.join(char.lower() for char in word if char.isalpha()) for word in splitted_words]

        for i in alphabets_only:
            maps[i] = 1 + maps.get(i, 0)
            

        for key in list(maps.keys()):
            if key in banned:
                maps.pop(key)
            
        target_value = max(maps.values())        

        for k, v in maps.items():
            if v == target_value:
                if k != '':
                    return k
        