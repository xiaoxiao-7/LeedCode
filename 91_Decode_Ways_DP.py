class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = len(s)
        if m == 0 or s[0] == '0':
            return 0
        dp = [0]* (max(m + 1,2))
        dp[0] = 1
        dp[1] = 1
        for i in range(2, m + 1):
            if s[i-2:i] == "10" or s[i-2:i] == "20":
                dp[i] = dp[i-2]
            elif s[i-2:i] > "10" and s[i-2:i] <= "26" and s[i-2:i] != "20":
                dp[i] = dp[i-1] + dp[i-2]
            elif s[i-1] != "0":
                dp[i] = dp[i -1]
            else:
                return 0
        return dp[m]