# Problem: Step-By-Step Directions From a Binary Tree Node to Another - https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def findPath(node, target, path):
            if not node:
                return False
            if node.val == target:
                return True
            path.append('L')
            if findPath(node.left, target, path):
                return True
            path.pop()
            path.append('R')
            if findPath(node.right, target, path):
                return True
            path.pop()
            return False

        def findLCA(node):
            if not node or node.val in (startValue, destValue):
                return node
            left = findLCA(node.left)
            right = findLCA(node.right)
            if left and right:
                return node
            return left if left else right

        lca = findLCA(root)

        pathToStart = []
        pathToDest = []
        findPath(lca, startValue, pathToStart)
        findPath(lca, destValue, pathToDest)

        # Step 3: Convert pathToStart to 'U's and join with pathToDest
        return 'U' * len(pathToStart) + ''.join(pathToDest)