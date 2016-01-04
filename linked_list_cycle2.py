# problem: https://leetcode.com/problems/linked-list-cycle/
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        nextval = None
        if self.next:
            nextval = self.next.val
        return str(self.val) + '\t' + str(nextval) + '\n'

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return None
        if not head.next:
            return None
        hare, tortoise = head, head
        cycle = False
        while not cycle:
            if not tortoise.next:
                return None
            if not hare.next:
                return None
            if not hare.next.next:
                return None
            tortoise = tortoise.next
            hare = hare.next.next
            if tortoise == hare:
                cycle = True

        # If we're here, there's a cycle
        # move slow to head, keep fast where it is, and loop till they match
        tortoise = head
        while hare != tortoise:
            hare = hare.next
            tortoise = tortoise.next
        return  hare


# Create some nodes
nodes = [ListNode(i) for i in range(10)]

# No cicle
for i in range(len(nodes) - 1):
    nodes[i].next = nodes[i+1]

a = Solution()
#print [x.val for x in nodes]
print a.detectCycle(nodes[0])

# has cycle
nodes[len(nodes)-1].next = nodes[len(nodes)/2]
print a.detectCycle(nodes[0])
