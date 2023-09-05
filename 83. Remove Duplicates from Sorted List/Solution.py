# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if curr is None:
            return head
        
        curr = head # assign to current
        while curr and curr.next: # while both not None 
            if curr.val == curr.next.val: # check if curr node's.val and next's val equality if true
                curr.next = curr.next.next # skip the dublicate value to its next 
            else:
                curr = curr.next # if false then continue traversing
        return head  # return head