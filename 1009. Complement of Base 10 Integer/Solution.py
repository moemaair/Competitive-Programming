class Solution:
    def bitwiseComplement(self, n: int) -> int:
        nToBin =list(bin(n)[2:])

        for i in range(len(nToBin)):
            if nToBin[i] == '1':
                nToBin[i] = '0'
            elif nToBin[i] == '0':
                nToBin[i] = '1'
        return int(''.join(nToBin), 2)

            