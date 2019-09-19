#  思路
"""
快慢指针（双指针）
1.先给列表添加哑节点dummyHead（头节点前添加一个节点），这样头节点也可以当作普通节点一样处理
2.设置两个指针，font（前指针）和back（后指针），都指向哑节点
3.前指针向前移动，使前后指针相隔n个节点
4.同时移动前后指针，直到前指针遍历结束，指向空。这时后指针所指的节点即为所要删除的导数第n个节点的前一个节点
5.将back.next=back.next.next即删除了倒数第n个节点
6。返回头节点，即哑节点dummyHead.next
"""
# 代码

# Definition for singly-linked list.


class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummyHead = ListNode(0)
        dummyHead.next = head
        font = dummyHead
        back = dummyHead

        for i in range(1, n+2):  # 要让两指针相差n，则前指针要往前移n+1步
            font = font.next

        # font不为空，同时移动前后指针直到font为空

        while font:
            font = font.next
            back = back.next

        # 删除倒数第n个节点
        back.next = back.next.next

        # 返回头节点
        return dummyHead.next


if __name__ == '__main__':

    head = ListNode(1)
    temp = head
    for i in range(2, 6):
        temp.next = ListNode(i)
        temp = temp.next

    c = Solution()
    n = 2
    result = c.removeNthFromEnd(head, n)
    while result:
        print(result.val)
        result = result.next




