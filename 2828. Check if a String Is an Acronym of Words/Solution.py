class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:

        ls = []
        for i in range(len(words)):
            ls.append(words[i][0])

        if s == ''.join(ls):
           return True
        else:
            return False
                