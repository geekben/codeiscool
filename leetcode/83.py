# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        i = head
        j = head.next
        while j:
            if i.val == j.val:
                j = j.next
            else:
                if i.next != j:
                    i.next = j
                i = j
                j = j.next
        i.next = None
        return head
