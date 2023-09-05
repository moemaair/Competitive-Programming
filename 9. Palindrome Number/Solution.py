# using 2-pointer approach

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # to string
        string_x = str(x)
        left_pointer = 0
        right_pointer = len(string_x) - 1

        if len(string_x) < 0:
            return False

        while left_pointer < right_pointer:
            if not string_x[left_pointer] == string_x[right_pointer]:
                return False
            else:
                left_pointer+=1
                right_pointer-=1
        return True            
            