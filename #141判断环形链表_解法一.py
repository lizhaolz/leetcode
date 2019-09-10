# 思路
"""
哈希表(集合)，每遍历一个节点，把他放在哈希表里，每次遍历时节点，判断哈希表中是否存在该节点，
如果存在，则代表有环。若退出循环，程序还未结束，则代表没有环
"""
# 代码

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype:ListNode
        """
        lookup = set()
        p = head
        while p:
            if p in lookup:
                return True
            else:
                lookup.add(p)
            p = p.next

        return False


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = head.next

    sol = Solution()
    res = sol.hasCycle(head)
    print(res)
