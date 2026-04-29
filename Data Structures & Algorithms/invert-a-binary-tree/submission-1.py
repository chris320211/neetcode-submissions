# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # given the root of a binary tree
        # for every parents left and right child is changed
        # return root which can get anythign via tree class
        # recursive 
        # depth first search

        # base case
        if root == None:
            return None

        # swap the children via tmp variable
        tmp = root.left
        root.left = root.right
        root.right = tmp
        
        # recursively call on the subtrees of origianl
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
        


