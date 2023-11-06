from ast import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # do in-place

        transposed = list(map(list, list(zip(*matrix)))) # Trasposed 
        matrix[::] = [row[::-1] for row in transposed] # reversed 