class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ret = 0
        idx = nums.index(k)
        dp = {}
        dp[0] = 1
        ts = 0

        for i,n in enumerate(nums):
            t = 0
            if n > k: t = 1
            elif n < k: t = -1
            ts += t
            if i < idx:
                if ts in dp:
                    dp[ts] += 1
                else:
                    dp[ts] = 1
            else:
                if ts in dp:
                    ret += dp[ts]
                if ts - 1 in dp:
                    ret += dp[ts-1]

        return ret
