class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        #initialization
        dp = [[] for x in range(m)]
        dp[0].append(grid[0][0])
        for i in range(1,m):
            dp[i].append(dp[i - 1][0]+grid[i][0])
        for j in range(1,n):
            dp[0].append(dp[0][j - 1]+grid[0][j])
        #Recursion
        for i in range(1,m):
            for j in range(1, n):
                dp[i].append(min(dp[i-1][j], dp[i][j-1]) + grid[i][j])
        return dp[m - 1][n - 1]