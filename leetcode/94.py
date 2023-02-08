# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        ret = []
        if root.left:
            ret += self.inorderTraversal(root.left)
        ret.append(root.val)
        if root.right:
            ret += self.inorderTraversal(root.right)

        return ret
