class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        total = 0
        for word in words:
            if Counter(word) <= Counter(chars):
                 total+=len(word)
                
        return total