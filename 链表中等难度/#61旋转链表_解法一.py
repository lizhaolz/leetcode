# 思路
"""
不旋转节点，只平移节点里存的值,注意保存当前节点的值和下一个节点的值
"""

# 代码

# Definition for singly-linked list.


class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        else:

            phead = head
            length = 0
            while phead:
                length += 1
                phead = phead.next

            k = k % length  # 旋转长度大于length时，相当于旋转k % length

            loop = 1
            while loop <= k:
                valtemp = 0
                ptemp = head
                curvaltemp = ptemp.val  # 报存当前节点的值
                while ptemp and ptemp.next:
                    valtemp = ptemp.next.val  # 保存下一个节点的值
                    ptemp.next.val = curvaltemp  # 之后把当前节点的值赋值给下一个节点
                    curvaltemp = valtemp  # 然后把下一个节点的值保存为当前节点的值
                    ptemp = ptemp.next  # 指针后移
                head.val = valtemp  # 把最后一个节点的值给头节点
                loop += 1  # 下一趟移动
            return head


if __name__ =="__main__":
    head = ListNode(1)
    temp = head
    for i in range(2, 6):
        temp.next = ListNode(i)
        temp = temp.next

    s = Solution()
    k = 2
    pphead = s.rotateRight(head, k)
    while pphead:
        print(pphead.val)
        pphead = pphead.next
