# 思路
"""
还是从中间反转链表，之后遍历两个链表，判断是否是回文链表
但是可以利用快慢指针找链表的中点
快指针每次走两步，慢指针每次走一步。当快指针走完整个链表
慢指针则刚走到链表中点的位置
"""
#代码


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        # 单节点链表后空链表一定为回文链表
        if head is None or head.next is None:
            return True
        else:
            # 快慢指针找链表中点
            fast = head
            slow = head
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next

            # 反转后半段链表
            pre = slow
            cur = slow.next
            temp_last = slow
            while cur:
                temp = cur.next
                cur.next = pre
                temp_last.next = temp
                pre = cur
                cur = temp

            temp_head = head
            while temp_head and pre:
                if temp_head.val == pre.val:
                    temp_head = temp_head.next
                    pre = pre.next
                else:
                    return False

            return True
