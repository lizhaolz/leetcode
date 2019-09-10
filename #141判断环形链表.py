# 思路
"""
快慢指针法，如果有环，两个最终会相遇
假设快指针每次走两步，慢指针每次走一步，如果有环，两个肯定会相遇
"""
# 代码


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head:ListNode
        :rtype: ListNode
        """
        fast = head
        slow = head
        if head is None or head.next is None:
            return False
        else:
            while fast and fast.next:  # 注意判读无环时fast.next.next 是否存在，即判断fast及fast.next是否存在
                fast = fast.next.next
                slow = slow.next
                if fast == slow:
                    return True
            return False


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = head.next

    sol = Solution()
    res = sol.hasCycle(head)
    print(res)
