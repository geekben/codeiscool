# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if root is None:
            return False

        tsum = targetSum - root.val
        if root.left is None and root.right is None and tsum == 0:
            return True

        if root.left and self.hasPathSum(root.left, tsum):
            return True
        if root.right and self.hasPathSum(root.right, tsum):
            return True
        return False
