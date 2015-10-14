# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        if k == 1:
            return head
        # count numbers in the list
        n = 0
        cur = head
        while cur is not None:
            n += 1
            cur = cur.next
        times = n / k
        if times == 0:
            return head
        # last is the ending node of the previous nodes that have already been reversed
        last = ListNode(0)
        last.next = head
        initial_head = last
        pre = head
        cur = pre.next
        i = 1
        cur_time = 0
        while cur is not None:
            i += 1
            tmp_next = cur.next
            cur.next = pre
            if i == k:
                last.next.next = tmp_next
                tmp = last.next
                last.next = cur
                last = tmp
                cur_time += 1
                if cur_time == times:
                    break
                i = 1
                pre = tmp_next
                cur = pre.next
            else:
                pre = cur
                cur = tmp_next
        return initial_head.next