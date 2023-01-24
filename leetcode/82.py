'''
[1,2,3,3,4,4,5]
[1,1,1,2,3]
[1,1,1,2,2]
[]
[1]
[1,2]
[1,2,3]
[1,1]
[1,1,1]
[1,2,2,2,2,2,3,3,3,3]
[1,2,2,3,3,4]
[1,2,3,3,3,3,3,3,3,3,3,3]
'''
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
        o = ListNode(-101, head)
        i = o
        j = o.next
        while j:
            k = j.next
            if k == None:
                if i.next == j:
                    break
                else:
                    i.next = None
                    break
            if j.val == k.val:
                j = k
            elif i.next == j:
                i = j
                j = k
            else:
                i.next = k
                j = k
        return o.next


