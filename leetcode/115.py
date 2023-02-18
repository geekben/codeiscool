class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        ls = len(s)
        lt = len(t)
        dp = [[0 for _ in xrange(ls+1)] for _ in xrange(lt)]
        dp = [[1 for _ in xrange(ls+1)]] + dp

        for i in xrange(1,lt+1):
            ct = t[i-1]
            for j in xrange(i,ls+1):
                cs = s[j-1]
                if cs == ct:
                    dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]

        return dp[lt][ls]
