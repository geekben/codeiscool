# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minVal(self, root):
        if root.left:
            root = root.left
        else:
            return root.val
        return self.minVal(root)

    def maxVal(self, root):
        if root.right:
            root = root.right
        else:
            return root.val
        return self.maxVal(root)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root.left:
            if self.maxVal(root.left) >= root.val:
                return False
            if not self.isValidBST(root.left):
                return False
        if root.right:
            if self.minVal(root.right) <= root.val:
                return False
            if not self.isValidBST(root.right):
                return False
        return True
