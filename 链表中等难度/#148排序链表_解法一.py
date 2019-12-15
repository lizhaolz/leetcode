"""
归并排序的思想 ，归并排序复杂度O（nlogn）,空间复杂度O(n)(对数组来说，且不用递归方法实现)
递归实现归并排序，但是由于是递归调用，所以空间复杂度其实是O(logn)
开辟的dummyHead在每一轮结束后会自动回收
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        slow, fast = head, head
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        mid, slow.next = slow.next, None
        # 递归分割
        left, right = self.sortList(head), self.sortList(mid)
        dummyHead = res = ListNode(0)
        while left and right:
            if left.val < right.val:
                dummyHead.next = left
                left = left.next
            else:
                dummyHead.next = right
                right = right.next
            dummyHead = dummyHead.next

        if left:
            dummyHead.next = left
        else:
            dummyHead.next = right
        return res.next


if __name__ == '__main__':
    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(3)
    res = Solution()
    result = res.sortList(head)
    while result:
        print(result.val)
        result = result.next
