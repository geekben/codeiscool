# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        c = right - left
        if c == 0:
            return head

        myhead = ListNode(next=head)
        t = myhead
        l = 0

        while t:
            if l == left - 1:
                break
            l += 1
            t = t.next

        s = t
        p = s.next
        q = p.next

        while q and c > 0:
            temp = q.next
            q.next = p
            p = q
            q = temp
            c -= 1

        temp = s.next
        s.next = p
        temp.next = q

        return myhead.next

