import string
import sys


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not(root):
            return root

        x, y = root.left if root.left else None, root.right if root.right else None
        root.left = y
        root.right = x
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

t4 = TreeNode(4)
t2 = TreeNode(2)
t7 = TreeNode(7)
t1 = TreeNode(1)
t3 = TreeNode(3)
t6 = TreeNode(6)
t9 = TreeNode(9)

t4.left = t2
t4.right = t7

t2.left = t1
t2.right = t3

t7.left = t6
t7.right = t9


def inorder(root):
    if not root:
        return
    if root.left:
        inorder(root.left)
    print root.val,
    if root.right:
        inorder(root.right)

inorder(t4)
print '\n'
x = Solution()
t = x.invertTree(t4)
inorder(t)
print '\n'
