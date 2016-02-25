# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.ans = []
        self.zigzagLevelOrderHelper(root, level=0)
        return self.ans

    def zigzagLevelOrderHelper(self, root, level=0):
        if not root:
            return

        if len(self.ans) <= level:
            self.ans.append([])

        if level % 2:
            self.ans[level].insert(0, root.val)
        else:
            self.ans[level].append(root.val)

        self.zigzagLevelOrderHelper(root.left, level+1)
        self.zigzagLevelOrderHelper(root.right, level+1)
            

# {3,9,20,#,#,15,7},
root = TreeNode(3)
r9 = TreeNode(9)
r20 = TreeNode(20)
r15 = TreeNode(15)
r7 = TreeNode(7)
root.left = r9
root.right = r20
r20.left=r15
r20.right=r7

print root, root.val
x = Solution()
print x.zigzagLevelOrder(root)

