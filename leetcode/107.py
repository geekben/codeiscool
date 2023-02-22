# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        q = [root]
        ret = []
        while q:
            l = len(q)
            tr = []
            for _ in xrange(l):
                n = q.pop(0)
                tr.append(n.val)
                if n.left: q.append(n.left)
                if n.right: q.append(n.right)
            ret = [tr] + ret
        return ret
