# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if preorder == []:
            return None
        hv = preorder[0]
        hin = inorder.index(hv)
        l = self.buildTree(preorder[1:hin+1], inorder[:hin])
        r = self.buildTree(preorder[hin+1:], inorder[hin+1:])
        h = TreeNode(hv, l, r)

        return h
