class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        ls = len(s)
        dp = [False] * (ls + 1)
        dp[0] = True

        for i in xrange(ls):
            for j in xrange(0,i+1):
                if dp[j] and s[j:i+1] in wordDict:
                    dp[i+1] = True
        
        return dp[ls]
