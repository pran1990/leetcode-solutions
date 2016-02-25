# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        answer = []
        q = [(root, 0)]
        while q:
            cur_node, cur_level = q.pop(0)
            if cur_node.left:
                q.append((cur_node.left, cur_level+1))
            if cur_node.right:
                q.append((cur_node.right, cur_level+1))
            if len(answer) <= cur_level:
                answer.append([])
            answer[cur_level].append(cur_node.val)
        answer.reverse()
        return answer
            

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
print x.levelOrderBottom(root)

