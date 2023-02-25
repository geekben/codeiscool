# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    st = {}
    def maxDepth(self, root):
        if root is None:
            return 0
        if root in self.st:
            return self.st[root]
        ret = 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        self.st[root] = ret
        return ret
    def isBalancedInner(self, root):
        if root is None:
            return True
        ld = self.maxDepth(root.left)
        rd = self.maxDepth(root.right)
        if abs(ld-rd) > 1:
            return False
        else:
            return self.isBalancedInner(root.left) and self.isBalancedInner(root.right)
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.st = {}
        return self.isBalancedInner(root)
