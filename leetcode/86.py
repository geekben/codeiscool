# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        t = ListNode(-201, head)
        l = t
        p = t.next

        q = None
        while p != None:
            if p.val >= x:
                if q == None:
                    q = l
            else:
                if q:
                    l.next = p.next
                    p.next = q.next
                    q.next = p
                    q = p
                    p = l.next
                    continue
            l = p
            p = p.next

        return t.next
