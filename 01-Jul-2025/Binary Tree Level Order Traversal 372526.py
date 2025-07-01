# Problem: Binary Tree Level Order Traversal - https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ans = [[root.val]]
        q = deque([root])
        q2 = deque()

        while q:
            node = q.popleft()

            if node.left:
                q2.append(node.left)

            if node.right:
                q2.append(node.right)

            if not q:
                if q2:
                    ans.append([n.val for n in q2])
                q = q2
                q2 = deque()
        
        return ans

                
                    