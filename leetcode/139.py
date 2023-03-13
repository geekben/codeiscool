class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        ls = len(s)
        dp = [[False] * ls for _ in xrange(ls)]

        for i in xrange(ls):
            for j in xrange(i+1,ls+1):
                if s[i:j] in wordDict:
                    dp[i][j-1] = True
        
        for j in xrange(ls):
            if not dp[0][j]:
                for k in xrange(1,j+1):
                    if dp[0][k-1] and dp[k][j]:
                        dp[0][j] = True
        return dp[0][ls-1]
