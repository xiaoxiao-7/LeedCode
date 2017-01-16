class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ways = [1,1,0]
        i = 2
        if n == 1:
            return 1
        else:
            while i < n+1:
                ways[2] = ways[0]+ways[1]
                ways[0] = ways[1]
                ways[1] = ways[2]
                i = i+1
            return ways[2]