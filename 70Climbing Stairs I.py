class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ways = [1,1]
        if n == 1:
            return ways[1]
        else:
            for x in range(2,n+1):
                t = ways[x-1] + ways[x-2]
                ways.append(t)
        return ways[n]