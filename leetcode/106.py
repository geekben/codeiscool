# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if postorder == []:
            return None
        h = postorder[-1]
        hin = inorder.index(h)
        l = self.buildTree(inorder[:hin], postorder[:hin])
        r = self.buildTree(inorder[hin+1:], postorder[hin:-1])
        return TreeNode(h, l, r)
