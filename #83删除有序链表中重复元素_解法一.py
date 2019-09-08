# 思路
"""
这是道简单题，直接解
设置指针cur，指向头节点，用cur遍历链表，如果cur的值和下一节点的值相等，则删除下一节点，
否则cur向后循环
注意：删除的节点（野节点）的清除
"""
# 代码
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head:ListNode
        :rtype: ListNode
        """
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                temp = cur.next
                cur.next = temp.next
                temp.next = None    # 清除野指针
            else:
                cur = cur.next

        return head


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(2)
    c = Solution()
    res = c.deleteDuplicates(head)
    while res:
        print(res.val)
        res = res.next
