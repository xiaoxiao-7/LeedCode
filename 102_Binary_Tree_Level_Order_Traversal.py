# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import Queue
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        binary_tree = Queue.Queue()
        binary_tree.put(root)
        current_level = 1
        next_level = 0
        temp = []
        output = []
        if root == None:
            return output
        while binary_tree.empty() == False:
            node = binary_tree.get()
            temp.extend([node.val])
            if node.left != None:
                binary_tree.put(node.left)
                next_level = next_level + 1
            if node.right != None:
                binary_tree.put(node.right)
                next_level = next_level + 1
                
            current_level = current_level - 1
            if current_level == 0:
                current_level = next_level
                next_level = 0
                output.append(temp)
                temp = []
        return output