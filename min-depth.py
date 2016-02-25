# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return self.minDepthHelper(root, 1)

    def minDepthHelper(self, root, height=0):
        if not root.left and not root.right:
            return height

        if root.left and root.right:
            return min(self.minDepthHelper(root.left, height+1),
                       self.minDepthHelper(root.right, height+1))

        if root.left:
            return self.minDepthHelper(root.left, height+1)

        return self.minDepthHelper(root.right, height+1)

        
# {3,9,20,#,#,15,7},

#root = TreeNode(3)
#r9 = TreeNode(9)
#r20 = TreeNode(20)
#r15 = TreeNode(15)
#r7 = TreeNode(7)
#root.left = r9
#root.right = r20
#r20.left=r15
#r20.right=r7

root = TreeNode(1)
r2 = TreeNode(2)
root.left = None
root.right = r2

x = Solution()
print x.minDepth(root)

