class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        value = str(int("".join(map(str, digits))) + 1)

        digits[::] = [int(x) for x in value]
        return digits


        