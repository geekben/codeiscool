# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        l = len(nums)
        if l == 0:
            return None
        hin = l/2
        hv = nums[hin]
        lt = self.sortedArrayToBST(nums[:hin])
        rt = self.sortedArrayToBST(nums[hin+1:])
        return TreeNode(hv, lt, rt)
