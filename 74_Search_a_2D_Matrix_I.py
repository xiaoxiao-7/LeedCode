class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = len(matrix)
        if row == 0:
            return False
        col = len(matrix[0])
        r = 0
        c = col - 1
        while r< row and c>=0:
            if matrix[r][c] < target:
                r = r + 1
            elif matrix[r][c] > target:
                c = c - 1
            else:
                return True
        return False

# 右上角法则：
# 每次比较target和第一行最后一个元素y：
# 	如果target>y，删掉第一行；
# 	如果target<y，删掉最后一行；
# 	