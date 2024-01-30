class Solution:
    def oddString(self, words: List[str]) -> str:
        res = []
        for word in words:
            temp =[]
            for j in range(1, len(word)):
                diff = ord(word[j]) - ord(word[j-1])
                temp.append(diff)
            res.append(temp)    
        
        for i in range(len(res)):
            if res.count(res[i])==1:
                return words[i]