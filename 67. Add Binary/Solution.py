class Solution:
    def addBinary(self, a: str, b: str) -> str:
        todecA = int(a,2)
        todecB = int(b,2)

        addDec = todecA + todecB

        toBin = bin(addDec)[2:]
        return str(toBin)
        