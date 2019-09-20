# 思路
"""
脑筋急转弯
只告诉你要删除的节点，问题可以转换为删除要删除节点的下一节点
可以把下一个节点的值赋值给要删除的节点，然后删除下一节点就行
"""

# 代码


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next  # 删除下一个节点

