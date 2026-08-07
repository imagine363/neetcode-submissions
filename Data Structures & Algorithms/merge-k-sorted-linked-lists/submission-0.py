import heapq
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:    
    def mergeKLists(self, lists):
        heap = []
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(heap,(head.val,i,head))
        dummy = ListNode()
        tail = dummy
        while heap:
            value, i, node =   heapq.heappop(heap)
            tail.next = node
            tail = tail.next
            if node.next:
                heapq.heappush(heap,(node.next.val,i,node.next))
        tail.next = None

        return dummy.next
        

head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(4)

head2 = ListNode(1)
head2.next = ListNode(3)
head2.next.next = ListNode(5)

head3 = ListNode(3)
head3.next = ListNode(6)

lists = [head1,head2,head3]

sol = Solution()
merged = sol.mergeKLists(lists)
curr = merged
while curr:
    print(curr.val, end=" -> " if curr.next else "\n")
    curr = curr.next