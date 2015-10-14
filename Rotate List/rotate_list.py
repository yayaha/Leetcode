# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return head
        pos = head
        cur = head
        for i in xrange(k):
            if pos.next is None:
                k = k % (i + 1)
                break
            else:
                pos = pos.next
        while pos.next is not None:
            pos = pos.next
            cur = cur.next
        pos.next = head
        head = cur.next
        cur.next = None
        return head