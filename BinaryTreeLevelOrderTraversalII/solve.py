# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None: return []
        
        ans = []
        ans.append([root.val])
        
        stack = [(root.right, 1), (root.left, 1)]
        
        while stack:
            n, i = stack.pop()
            
            if n is None:
                continue
            
            if len(ans) == i:
                ans.append([])
            
            ans[i].append(n.val)
            
            if n.right is not None:
                stack.append((n.right,i+1))
            if n.left is not None:
                stack.append((n.left,i+1))
        
        return ans[::-1]
