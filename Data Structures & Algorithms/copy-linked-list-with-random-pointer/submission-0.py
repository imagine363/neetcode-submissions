class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
class Solution:
    def copyRandomList(self, head):
        old_to_new = {}

        curr = head
        while curr:
            copy = Node(curr.val)
            old_to_new[curr] = copy
            curr = curr.next
        curr = head
        while curr:
            copy = old_to_new[curr]
            copy.next = old_to_new.get(curr.next)
            copy.random = old_to_new.get(curr.random)
            curr = curr.next
        return old_to_new.get(head)
head = Node(3)
head.next = Node(7)
head.next.next = Node(4)
head.next.next.next = Node(5)

head.random = None
head.next.random = head.next.next.next
head.next.next.random = head
head.next.next.next.random = head.next

sol = Solution()
res = sol.copyRandomList(head)
while res:
    random_val = res.random.val if res.random else None
    print(f"val={res.val}, random={random_val}")
    res = res.next

    
        