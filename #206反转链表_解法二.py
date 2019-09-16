# 思路
"""
迭代法
1. 设置三个指针，分别指向反转后头节点，当前节点，当前节点的下一个节点
并设置一个指针指向头节点，因为链表未反转的部分总是插在原来的头节点之后。
2. 将反转后头节点的值指向当前节点的下一节点，并将剩余未反转部分插入到原来头节点
3. 改变当前节点和反转后头节点的位置，继续遍历，直到当前节点为空。
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
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


if __name__ == "__main__":
    head = ListNode(1)
    temp = head
    for i in range(2, 6):
        temp.next = ListNode(i)
        temp = temp.next
    s = Solution()
    res = s.reverseList(head)
    while res:
        print(res.val)
        res = res.next
