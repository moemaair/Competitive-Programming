from ast import List


class Solution:
    def countBits(self, n: int) -> List[int]:

        y = []
        st = []
        
        for index in range(n+1):
           
            st.append(bin(index)[2:])         

        for i in st:
            if i == '0':
                y.append(int(i))
            else:
                y.append(i.count('1'))
        return y        
