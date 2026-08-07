class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head):
        s = head
        f = head
        if not head or not head.next:
            return None
        prev_s = None
        secondhalf = None
        while f and f.next:
            prev_s = s
            s = s.next
            f = f.next.next
        if f is None:
            prev_s.next = None
            secondhalf = s
        else:
            secondhalf = s.next
            s.next = None

        prev = None
        while secondhalf:
            nxt = secondhalf.next
            secondhalf.next = prev
            prev = secondhalf
            secondhalf = nxt
        curr = head
        while curr and prev:
            nxt = curr.next
            nxt2 = prev.next

            curr.next = prev
            prev.next = nxt

            curr = nxt
            prev = nxt2
        

        

head = ListNode(1)

sol = Solution()
sol.reorderList(head)
curr = head
while curr:
    print(curr.val, end = " ")
    curr = curr.next