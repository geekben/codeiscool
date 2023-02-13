# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def expandTree(self, root):
        if root is None:
            return [],[]
        lln,llv = self.expandTree(root.left)
        rln,rlv = self.expandTree(root.right)
        return lln+[root]+rln, llv+[root.val]+rlv

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        ln,lv = self.expandTree(root)
        slv = sorted(lv)
        a = -1
        b = -1
        for i in xrange(len(lv)):
            if lv[i] != slv[i] and a == -1:
                a = i
            if lv[i] != slv[i] and lv[a] == slv[i]:
                b = i
                break
        ln[a].val = slv[a]
        ln[b].val = slv[b]
