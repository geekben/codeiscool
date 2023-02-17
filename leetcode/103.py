# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagTree(self, root, level):
        if root is None:
            return []

        l = self.zigzagTree(root.left, level+1)
        r = self.zigzagTree(root.right, level+1)

        ll = len(l)
        lr = len(r)
        for i in xrange(ll):
            if i >= lr:
                break
            if (level + i) % 2 == 0:
                l[i] = l[i] + r[i]
            else:
                l[i] = r[i] + l[i]
        if ll < lr:
            l += r[ll:]

        return [[root.val]] + l

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        return self.zigzagTree(root, 1)
