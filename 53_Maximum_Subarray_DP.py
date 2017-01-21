class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = len(nums)
        dp = []
        #initialization
        dp.append(nums[0])
        ans = dp[0]
        #recursion
        for i in range(1, m):
            dp.append(max(nums[i],nums[i] + dp[i-1]))
            ans = max(dp[i],ans)
        return ans