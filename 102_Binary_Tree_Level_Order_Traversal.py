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
        # generate a queue class
        binary_tree = Queue.Queue()
        # put the value of root into the queue
        binary_tree.put(root)
        # level counters
        current_level = 1
        next_level = 0
        #level = 0  
        temp = []
        output_arrary =[]
        if root == None:
        	return output_arrary
        while binary_tree.empty() == false:
        	node = binary_tree.get()
        	temp =temp.extend(node.val)
        	if node.left != None:
        		binary_tree.put(node.left)
        		next_level = next_level + 1
        	if node.right != None:
        		binary_tree.put(node.right)
        		next_level = next_level + 1
        	current_level = current_level - 1
			if current_level ==0:
        		current_level = next_level
        		next_level = 0
        		output_arrary.append(temp)
        		temp = []
        return output_arrary
