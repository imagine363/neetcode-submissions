class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode()
        dummy.next = head
        groupprev = dummy
        while True:
            temp = groupprev
            for _ in range(k):
                temp = temp.next
                if temp is None:
                    return dummy.next

            curr = groupprev.next
            oghead = curr
            prev=  None
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            oghead.next = curr
            groupprev.next = prev
            groupprev = oghead
        return dummy.next
        
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
k = 3
sol = Solution()

result = sol.reverseKGroup(head,k)

curr = result
while curr:
    print(curr.val, end=" -> ")
    curr = curr.next
print("None")



