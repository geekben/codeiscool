# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        t = targetSum - root.val
        if t == 0 and root.left is None and root.right is None:
            return [[root.val]]
        rt = []
        if root.left:
            for r in self.pathSum(root.left, t):
                rt.append([root.val] + r)
        if root.right:
            for r in self.pathSum(root.right, t):
                rt.append([root.val] + r)
        return rt
