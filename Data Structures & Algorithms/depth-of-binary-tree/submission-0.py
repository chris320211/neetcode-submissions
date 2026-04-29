# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # depth first search we go left subtree then right
        # recursion
        # check if left and right nodes are none
        # if one is good, depth is added 1

        # base case
        if root is None:
            return 0

        return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))


