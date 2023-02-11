class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)
        if l1 + l2 != l3:
            return False

        dp = [[False for _ in xrange(l1+1)] for _ in xrange(l2+1)]
        dp[0][0] = True
        for i in xrange(1, l1+1):
            if s1[:i] == s3[:i]:
                dp[0][i] = True
        for i in xrange(1, l2+1):
            if s2[:i] == s3[:i]:
                dp[i][0] = True

        for i in xrange(1, l2+1):
            for j in xrange(1, l1+1):
                if dp[i-1][j] and s2[i-1] == s3[i+j-1]:
                    dp[i][j] = True
                elif dp[i][j-1] and s1[j-1] == s3[i+j-1]:
                    dp[i][j] = True

        return dp[l2][l1]
