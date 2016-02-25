# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        ans = []
        stk = []
        cur = root
        print 'here'
        while cur or stk:
            print 'herer1'
            while cur:
                stk.append(cur)
                cur = cur.left
            
            cur = stk.pop()
            ans.append(cur.val)
            cur = cur.right
            
        return ans
