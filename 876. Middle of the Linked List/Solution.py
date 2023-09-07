# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        #using slow-fast approach 

        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next # the moment is points to null slow will have gone half the list because its x1 and fast is x2 
        return slow    
            
        