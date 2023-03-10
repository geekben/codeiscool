class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        ln = len(nums)
        st = {}

        dp = [[0 for _ in xrange(ln)] for _ in xrange(ln)]
        for i in xrange(ln):
            for j in xrange(i, ln):
                if i == j:
                    dp[i][j] = nums[i]
                else:
                    dp[i][j] = dp[i][j-1] + nums[j]
                d = dp[i][j] % p
                if d == 0:
                    continue
                if d in st:
                    st[d] = min(st[d], j-i+1)
                else:
                    st[d] = j-i+1

        if dp[0][ln-1] < p:
            return -1
        d = dp[0][ln-1] % p
        if d == 0:
            return 0
        if d in st:
            return st[d]
        else:
            return -1
