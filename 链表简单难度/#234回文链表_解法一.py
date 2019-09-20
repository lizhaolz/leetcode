# 思路
"""
找到链表中点，将链表后半段反转
遍历两个链表，若反转后的链表后半段和原链表前半段在两个都不为空时
数据完全相等，则是回文链表，否则不是回文链表
时间复杂度：O(n)
空间复杂度: O(1)
有个问题，这会改变原链表，不可还可以改回去
"""
# 代码


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # 反转链表函数
    def reverseList(self, head):
        if head is None or head.next is None:
            return head
        else:
            pre = head
            temp_last = pre
            cur = head.next
            while cur:
                temp = cur.next
                cur.next = pre
                temp_last.next = temp
                pre = cur
                cur = temp
            return pre

    def isPalindrome(self, head):
        # 空链表和单节点链表属于回文链表
        if head is None or head.next is None:
            return True
        else:
            length = 0
            temp = head
            while temp:
                length += 1
                temp = temp.next
            if length % 2 == 0:
                # 长度为偶数
                cut = length / 2
            else:
                # 长度为奇数
                cut = length // 2
            t_head = head
            loop_i = 0
            while loop_i < cut:
                t_head = t_head.next
                loop_i += 1
            temp_head = self.reverseList(t_head)
            pre = head
            # 即使一个链表长度比另一个链表长度多一，在它两都不为空时若完全相等，则为回文链表
            while temp_head and pre:
                if temp_head.val == pre.val:
                    temp_head = temp_head.next
                    pre = pre.next
                else:
                    return False
            return True


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(1)
    s = Solution()
    res = s.isPalindrome(head)
    print(res)



