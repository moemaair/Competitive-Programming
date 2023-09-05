from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        # push all val in a stack
        # check if every val is not equal to popped val
        # return bool

        stack = [] #to store all val
        current = head
        while current:
            stack.append(current.val)
            current = current.next

        # reassign to head    
        current = head  

    
        while current:
            # check if every val is not equal to popped value from stack
            if current.val != stack.pop():
                return False
            current = current.next
        return True          