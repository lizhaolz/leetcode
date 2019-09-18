# 思路
"""
快慢指针。
两个指针同时从头节点开始遍历，快指针每次走两步，慢指针每次走一步
当快指针走到链表尾部时，慢指针正好走到链表中点的位置
"""
# 代码


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def middleNode(self, head):
        if head.next is None:
            return head

        else:
            fast = head
            slow = head
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            return slow
