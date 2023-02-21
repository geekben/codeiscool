# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def check(self, root):
        if root is None:
            return -1001,-1001
        lm, li = self.check(root.left)
        rm, ri = self.check(root.right)
        hv = root.val
        i = max(hv+li, hv+ri, hv)
        m = max(i, hv+li+ri, lm, rm)
        
        return m,i

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        m,i = self.check(root)
        return m
