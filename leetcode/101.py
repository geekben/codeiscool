# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def expandTreeLR(self, root):
        if root is None:
            return [None],[None]
        l, r = self.expandTreeLR(root.left)
        a = [root.val] + l + r
        l, r = self.expandTreeLR(root.right)
        b = [root.val] + r + l
        return a,b

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        elr,erl = self.expandTreeLR(root)
        if elr == erl:
            return True
        else:
            return False
