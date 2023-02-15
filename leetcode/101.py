# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def expandTreeLR(self, root):
        if root is None:
            return [None]
        l = self.expandTreeLR(root.left)
        r = self.expandTreeLR(root.right)
        return [root.val] + l + r
    def expandTreeRL(self, root):
        if root is None:
            return [None]
        r = self.expandTreeRL(root.right)
        l = self.expandTreeRL(root.left)
        return [root.val] + r + l
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        elr = self.expandTreeLR(root)
        erl = self.expandTreeRL(root)
        if elr == erl:
            return True
        else:
            return False
