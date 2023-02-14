# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def expandTree(self, root):
        if root is None:
            return [None]
        l = self.expandTree(root.left)
        r = self.expandTree(root.right)
        # must not use middle expansion (l,n.val,r)
        return [root.val] + l + r
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        ep = self.expandTree(p)
        eq = self.expandTree(q)

        # print ep,eq
        if ep == eq:
            return True
        else:
            return False
