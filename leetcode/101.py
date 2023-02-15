# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def compareTree(self, l, r):
        if l is None and r is None:
            return True
        if l is None or r is None:
            return False
        if l.val != r.val:
            return False
        return self.compareTree(l.left, r.right) and \
            self.compareTree(l.right, r.left)
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.compareTree(root.left, root.right)
