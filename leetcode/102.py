# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        l = self.levelOrder(root.left)
        r = self.levelOrder(root.right)
        ll = len(l)
        lr = len(r)
        for i in xrange(ll):
            if i >= lr:
                break
            l[i] = l[i] + r[i]
        if ll < lr:
            l += r[ll:]

        return [[root.val]] + l
