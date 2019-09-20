# 思路
"""
常规解法
首先往头节点前加哑节点，这样头节点也可以当作普通节点对待
设置两个指针，一个当前节点，一个当前节点的前一个节点。
当前节点从头节点开始，若当前节点的值等于要删除的值，删除当前节点，并后移当前节点
若当前节点的值不等于要删除的值，当前节点和前一节点同时后移。
循环上述过程，直到当前节点为空
"""
# 代码


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeElements(self, head, val):
        dummyHead = ListNode(0)
        dummyHead.next = head
        pre = dummyHead
        cur = head
        while cur:
            if cur.val == val:
                temp = cur
                pre.next = cur.next
                cur = cur.next
                temp.next = None  # 清理野指针
            else:
                pre = pre.next
                cur = cur.next
        return dummyHead.next


if __name__  == "__main__":
    l = [2, 6, 3, 4, 5, 6]
    head = ListNode(1)
    temp = head
    for i in l:
        temp.next = ListNode(i)
        temp = temp.next

    s = Solution()
    val = 6
    res = s.removeElements(head, val)
    while res:
        print(res.val)
        res = res.next

