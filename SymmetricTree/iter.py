# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None: return True 
        stack = [(root.left, root.right)]
        
        while stack:
            l, r = stack.pop()
            if l is None and r is None: continue
            if l is None or r is None or l.val != r.val: return False
            stack.append((l.left, r.right))
            stack.append((r.left, l.right))
        
        return True
