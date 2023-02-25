# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalancedInner(self, root):
        if root is None:
            return 0
        ld = self.isBalancedInner(root.left)
        rd = self.isBalancedInner(root.right)
        if ld == -1 or rd == -1 or abs(ld-rd) > 1:
            return -1
        else:
            return 1 + max(ld, rd)
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isBalancedInner(root) >= 0
