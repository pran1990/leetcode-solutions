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
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        if not head.next:
            return False
        hare, tortoise = head, head
        cycle = False
        while not cycle:
            if not tortoise.next:
                return False
            if not hare.next:
                return False
            if not hare.next.next:
                return False
            tortoise = tortoise.next
            hare = hare.next.next
            if tortoise == hare:
                cycle = True
        return  True


# Create some nodes
nodes = [ListNode(i) for i in range(10)]

# No cicle
for i in range(len(nodes) - 1):
    nodes[i].next = nodes[i+1]

a = Solution()
#print [x.val for x in nodes]
print a.hasCycle(nodes[0])

# has cycle
nodes[len(nodes)-1].next = nodes[len(nodes)/2]
print a.hasCycle(nodes[0])

