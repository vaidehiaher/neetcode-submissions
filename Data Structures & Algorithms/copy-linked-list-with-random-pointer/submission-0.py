class Solution:
    def copyRandomList(self, head):
        if not head:
            return None

        old_to_new = {}
        curr = head

        # Step 1: Create a copy of every node
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next

        # Step 2: Connect next and random pointers
        curr = head

        while curr:
            old_to_new[curr].next = old_to_new.get(curr.next)
            old_to_new[curr].random = old_to_new.get(curr.random)

            curr = curr.next

        # Step 3: Return the copied head
        return old_to_new[head]