class Solution(object):
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1] * 5
        for i in xrange(1,n):
            for j in xrange(0,5):
                dp[j] = sum(dp[j:])
        return sum(dp)
