# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        else:
            return self.isSame(root.left, root.right)   
            
             
    def isSame(self, left, right):
        if left == None and right == None:
                return True
        if left == None or right == None:
                return False    
        if left.val != right.val:
            return False   
        # Return true if the values of root nodes are same and left as well as right subtrees are symmetric...
        return self.isSame(left.left, right.right) and  self.isSame(left.right, right.left) 
