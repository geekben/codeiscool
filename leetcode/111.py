# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        q = [(root, 1)]

        while q:
            n,level = q.pop(0)
            if n.left is None and n.right is None:
                return level
            if n.left:
                q.append((n.left, level+1))
            if n.right:
                q.append((n.right, level+1))
