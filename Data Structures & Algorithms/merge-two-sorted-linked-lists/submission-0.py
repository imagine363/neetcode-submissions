class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        tail = dummy
        l1 = list1
        l2 = list2
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
                tail = tail.next
            else:
                tail.next = l2
                l2 = l2.next
                tail = tail.next
        if l1:
            tail.next = l1
        else:
            tail.next = l2
        return dummy.next
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(5)

sol = Solution()
merged = sol.mergeTwoLists(list1, list2)

curr = merged
while curr:
    print(curr.val, end=" -> " if curr.next else "\n")
    curr = curr.next
