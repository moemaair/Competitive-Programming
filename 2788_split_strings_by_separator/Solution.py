class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ls = [] 
        for data in words:
            word = data.split(separator)
            for data in word:
                if(data != ""):
                    ls.append(data)
        return ls