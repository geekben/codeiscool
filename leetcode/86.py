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
                    if p.next == None or p.next.val >= x:
                        temp = l.next
                        l.next = p.next
                        p.next = q.next
                        q.next = temp
                        q = p
                        p = l.next
                        continue
                    p = p.next
                    continue
            l = p
            p = p.next

        return t.next
