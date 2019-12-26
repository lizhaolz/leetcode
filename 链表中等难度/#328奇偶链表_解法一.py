# Definition for singly-linked list.
"""
思路：常规解法
循环指针每次指向奇数节点，只把下标为奇数节点全部链在一起，
这样偶数节点也就全部在一起了
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        else:
            tail = head
            pre = head.next
            p = head.next.next
            while p:
                if p.next and p.next.next:
                    pretemp = p.next
                    temp = p.next.next
                else:
                    pretemp = None
                    temp = None
                pre.next = p.next
                p.next = tail.next
                tail.next = p
                tail = p
                pre = pretemp
                p = temp
            return head



if __name__ == '__main__':

    head = ListNode(2)
    head.next = ListNode(1)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(5)
    head.next.next.next.next = ListNode(6)
    head.next.next.next.next.next = ListNode(4)
    head.next.next.next.next.next.next = ListNode(7)
    s = Solution()
    res = s.oddEvenList(head)
    while res:
        print(res.val)
        res = res.next
