# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    m = -1001
    def check(self, root):
        if root is None:
            return 0
        li = self.check(root.left)
        ri = self.check(root.right)
        hv = root.val
        i = max(hv+li, hv+ri, hv)
        self.m = max(i, hv+li+ri, self.m)
        
        return i

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.check(root)
        return self.m
