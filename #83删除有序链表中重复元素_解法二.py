# 思路
"""
递归法：
递归删除头节点下一个节点中的重复元素，之后判断头节点和已经删除重复元素的子链的头节点元素是否相等，
如果想等，删除子链头节点，注意清除野指针
递归终止条件：头节点为空，或者只有一个节点
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
        :rtype:ListNode
        """
        if head is None or head.next is None:
            return head

        else:
            head.next = self.deleteDuplicates(head.next)
            if head.next and head.next.val == head.val:
                child = head.next
                head.next = child.next
                child.next = None  # 清除野指针

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



