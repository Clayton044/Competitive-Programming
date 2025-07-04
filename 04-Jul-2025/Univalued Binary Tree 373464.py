# Problem: Univalued Binary Tree - https://leetcode.com/problems/univalued-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, val):
            if not node:
                return True
            if node.val != val:
                return False
            return dfs(node.left, val) and dfs(node.right, val)

        return dfs(root, root.val)