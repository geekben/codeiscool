# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    d = {}
    def traveTree(self, t, h):
        if t == None:
            return None
        ht = TreeNode(val=t.val+h)
        ht.left = self.traveTree(t.left, h)
        ht.right = self.traveTree(t.right, h)
        return ht

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        d = self.d
        if n in d:
            return d[n]
        if n == 0:
            return [None]
        if n == 1:
            d[1] = [TreeNode(val=1)]
            return d[1]
        if n == 2:
            a = TreeNode(val=1)
            b = TreeNode(val=2)
            a.right = b
            c = TreeNode(val=1)
            e = TreeNode(val=2)
            e.left =  c
            d[2] = [a, e]
            return d[2]

        ret = []
        for h in xrange(1, n+1):
            lr = self.generateTrees(h-1)
            rt = self.generateTrees(n-h)
            rr = []
            for r in rt:
                rr.append(self.traveTree(r, h))
            for l in lr:
                for r in rr:
                    hr = TreeNode(val=h, left=l, right=r)
                    ret.append(hr)
        d[n] = ret
        return ret
