class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def hasCycle(self, head):
        curr = head
        visited = set()
        while curr:
            if curr in visited:
                return True
            visited.add(curr)
            curr = curr.next
        return False

sol = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = head.next
res = sol.hasCycle(head)
print(res)

