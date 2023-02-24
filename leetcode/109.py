# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def listToBST(self, nums):
        ll = len(nums)
        if ll == 0:
            return None
        hin = ll/2
        hv = nums[hin]
        lt = self.listToBST(nums[:hin])
        rt = self.listToBST(nums[hin+1:])
        return TreeNode(hv, lt, rt)

    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        ln = []
        while head:
            ln.append(head.val)
            head = head.next
        return self.listToBST(ln)
