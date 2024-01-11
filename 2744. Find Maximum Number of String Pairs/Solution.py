class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        counter = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if words[i][::-1] == words[j]:
                    counter+=1 
        return counter            

        