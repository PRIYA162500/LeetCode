
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def hasPathSum(self, root, targetSum):
        if root is None:
            return False

        # Check if this is a leaf node
        if root.left is None and root.right is None:
            return root.val == targetSum

        # Subtract the current node value and search children
        remaining = targetSum - root.val

        return (
            self.hasPathSum(root.left, remaining) or
            self.hasPathSum(root.right, remaining)
        )
