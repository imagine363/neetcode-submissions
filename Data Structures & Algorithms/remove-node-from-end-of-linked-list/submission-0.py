class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        f = dummy
        s = dummy
        fcount = 0
        while fcount < n+1:
            f=f.next
            fcount += 1
        while f :
            f = f.next
            s = s.next
        s.next = s.next.next
        return dummy.next

sol = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
n = 2
curr = sol.removeNthFromEnd(head,n)
while curr:
    print(curr.val, end = " ")
    curr = curr.next


