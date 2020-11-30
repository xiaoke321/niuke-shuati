# TODO 反转链表
# 输入一个链表，反转链表后，输出新链表的表头
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def ReverseList(self, pHead):
        cur, node = None, pHead

        while node:
            temp = node.next
            node.next = cur
            cur = node
            node = temp

        return cur

if __name__ == '__main__':
    data = [1, 2, 3]
    l = ListNode(data)
    s = Solution()

    result = s.ReverseList(pHead=l)
    print(type(result))
    print(result)
    print(result.val)
    print(result.next)