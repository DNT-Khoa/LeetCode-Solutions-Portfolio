# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = deque()
        node = root
        
        while node or stack:
            if node:
                stack.append(node)
                ans.append(node.val)
                node = node.left
            else:
                node = stack.pop()
                node = node.right
            
        return ans