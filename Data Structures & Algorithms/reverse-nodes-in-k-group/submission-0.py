class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head, k):
        temp = head
        for _ in range(k):
            if temp == None:
                return head
            temp = temp.next
        curr = head
        oghead = curr
        count = 0
        prev=  None
        while count < k:
            count += 1
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        oghead.next = self.reverseKGroup(curr,k)
        return prev




